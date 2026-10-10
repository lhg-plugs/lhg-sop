---
description: 主流程：流程访谈提纲→SOP文档生成→执行检查清单→版本管理，一次把经验沉淀成可执行的文档。
argument-hint: <流程主题或岗位> [--interview]
---

# /lhg-sop:sop —— SOP 沉淀主流程

用户输入在 `$ARGUMENTS` 中：`<流程主题或岗位> [--interview]`。带 `--interview` 时先做结构化访谈再写文档。

## 流程（加载 sop-interview / sop-writing / sop-checklist / sop-audit 全程指导）

### 1. 访谈（把人脑里的流程掏出来）
- 用 `/lhg-sop:interview` 生成访谈提纲，或直接按 sop-interview 第 3 节提问。
- 目标：拿到"触发条件 → 步骤序列 → 分支判断 → 异常处理 → 交付物"五要素。
- **五要素不全，不动手写 SOP。**

### 2. 写文档（按模板，不许自由发挥）
按 sop-writing 第 4 节模板生成 `sops/<编号>-<主题>.md`，必须包含：
文档头（标题/编号/版本/日期/责任人）→ 目的 → 范围 → 角色职责 → 前置条件 →
步骤（编号连续、每步有责任人）→ 检查清单 → 例外与升级 → 修订历史。

### 3. 提检查清单
用 `/lhg-sop:checklist` 从 SOP 提取一线执行用的检查清单（可验证的检查项）。

### 4. 审计（脚本 + 人工）
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/audit/sop_audit.py --target sops/ --format text
```
blocker 必须清零；再按 sop-audit 第 5 节做人工评审（找个没做过的人试读）。

## 硬规则
- 没访谈、靠脑补写 SOP → 不许。
- 步骤无责任人、编号跳号 → 不许交付。
- 检查项不可验证（含"仔细""及时"等模糊词）→ 不许。
- 无版本号/日期 → 不许（版本管理是 SOP 的生命线）。
- blocker 未清零就说"可以用了" → 不许。
