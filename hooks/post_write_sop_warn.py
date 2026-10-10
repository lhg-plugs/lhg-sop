#!/usr/bin/env python3
"""lhg-sop 硬门②：写入 SOP 文档后，提醒同步版本/日期/修订历史。

触发：PostToolUse / Write|Edit。只对疑似 SOP 文档的文件生效
（路径含 sop/ 或文件名含 sop/规范/流程/清单），其他文件 0 开销直接放行。

逃生方式：LHG_SOP_HOOKS_OFF=1（单次豁免本次 hook）。

设计原则：只做提醒（additionalContext），不拦截；内部出错 fail-open；
零第三方依赖。
"""

import json
import os
import sys

SOP_HINTS = ("sop", "规范", "流程", "清单", "checklist")


def main() -> int:
    if os.environ.get("LHG_SOP_HOOKS_OFF") == "1":
        return 0

    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        return 0  # fail-open

    tool_input = payload.get("tool_input", {}) or {}
    path = tool_input.get("file_path", "") or ""
    low = path.lower()

    if not low.endswith((".md", ".mdx", ".txt")):
        return 0
    if not any(h in low for h in SOP_HINTS):
        return 0

    msg = (
        "lhg-sop 提醒：检测到 SOP 文档变更 %s。请确认版本纪律："
        "① 版本号升了吗（小改 v1.1 / 步骤变更 v2.0）；"
        "② 日期与修订历史同步了吗；"
        "③ 对应的执行检查清单同步评审了吗；"
        "④ 跑一遍 /lhg-sop:audit 确认 blocker 为 0。"
        % os.path.basename(path)
    )
    out = {"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                 "additionalContext": msg}}
    sys.stdout.write(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
