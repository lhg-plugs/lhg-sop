<!-- About 简介（推送后填写到仓库 About 栏）：
SOP沉淀专家：流程访谈提纲→SOP文档生成→检查清单→版本管理 ｜ 一键安装：/plugin marketplace add lhg-plugs/lhg-sop
-->
<!-- topics（推送后打）：claude-code, claude-plugin, agent-skills, sop, process, checklist, documentation -->

# lhg-sop：SOP沉淀专家

> **一句话介绍**：给 AI 写作助手装上"SOP 流水线"——流程访谈提纲→标准 SOP 文档→可验证检查清单→版本管理，17 条确定性规则把"写出来没人能用"的 SOP 提前消灭。
>
> **一键安装**：在 Claude Code 里运行
> ```
> /plugin marketplace add lhg-plugs/lhg-sop
> /plugin install lhg-sop@lhg-plugs
> ```

## 它是什么

`lhg-sop` 是一个 Claude Code 插件（plugin 为主、skill 为辅）：

- **4 个命令**（小白入口）：`sop` 沉淀主流程，`interview` 流程访谈提纲，`checklist` 执行检查清单提取，`audit` SOP 完整性审计
- **4 个平台中立 skill**（方法论，可移植到豆包/Workbuddy 等 agent 平台）：流程访谈、SOP 写作、检查清单设计、评审与版本管理
- **2 个专家 agent**：SOP 撰写、SOP 审计
- **2 个硬门 hooks**：commit 前 SOP 审计拦截、SOP 文档变更版本提醒（均可一键豁免）
- **17 条确定性审计规则**：步骤编号/责任人/检查项可验证性/版本日期/术语一致性全覆盖，纯 Python、零第三方依赖

## 4 个命令用法

| 命令 | 作用 | 示例 |
|---|---|---|
| `/lhg-sop:sop` | 访谈→写文档→提清单→审计，一次把经验沉淀成 SOP | `/lhg-sop:sop 客户退款流程 --interview` |
| `/lhg-sop:interview` | 生成五要素访谈提纲，把老员工脑子里的经验掏出来 | `/lhg-sop:interview 设备点检` |
| `/lhg-sop:checklist` | 从 SOP 提取一线执行用的一页纸检查清单 | `/lhg-sop:checklist sops/SOP-001.md` |
| `/lhg-sop:audit` | SOP 完整性审计（脚本 + 新人试读） | `/lhg-sop:audit sops/` |

## 自查说明

自查 = 确定性脚本（机器）+ 人工试读（人）：

1. 先跑 `scripts/audit/sop_audit.py`（17 条规则），零 LLM 成本；
2. 发现分三级：**blocker**（缺版本/日期/责任人、步骤跳号、无责任人，必须修，commit 前 hook 会拦截）、**warning**（修或写豁免理由）、**nit**（顺手修）；
3. 再找个**没做过这个流程的人**试读一遍——这是 SOP 唯一的真金标准，脚本查的是结构，试读查的是"人能不能照着做出来"。

blocker 清零 + 试读零卡点才算可用；为清零改规则算作弊，不许。

## 目录结构

```
lhg-sop/
├── .claude-plugin/          # plugin.json（插件清单）+ marketplace.json（本仓即市场）
├── commands/                # 4 个命令：sop / interview / checklist / audit
├── skills/                  # 4 个平台中立 skill（interview/writing/checklist/audit）
├── agents/                  # 2 个专家 agent（sop-writer / sop-auditor）
├── hooks/                   # 2 个硬门（commit 前审计拦截 / SOP 变更版本提醒）+ 豁免说明
├── scripts/audit/           # 17 条确定性审计规则（零第三方依赖）
├── fixtures/                # 冒烟测试用例（坏/好对照）
├── smoke_test.py            # 一键冒烟测试
├── ATTRIBUTION.md           # 灵感来源与许可声明
└── LICENSE                  # MIT
```

## 什么时候用 / 什么时候不用（FAQ）

**什么时候用：**

- 团队里"只有老员工会做"的流程，你想沉淀成新人照着能做的文档时 → 用 `/lhg-sop:sop --interview`
- 已经有 SOP 但没人按它做、你怀疑它脱离实际时 → `/lhg-sop:interview` 还原实际做法 + `/lhg-sop:audit` 审旧版
- 一线抱怨"SOP 太长，干活时没法看"时 → `/lhg-sop:checklist` 提一页纸清单
- 你想给团队立"无版本不发布、发布前必审计"的纪律时 → 它的 hooks 硬门开箱即用

**什么时候不用：**

- 流程只做一次、以后不再重复 → 写 SOP 是浪费，记个备忘就行（skill 里有"什么值得写 SOP"判定）
- 你只是想要个通用 SOP 模板 → 网上模板够了，本插件的价值在"访谈→写作→审计"全流程
- 你希望 AI 自由发挥、不接受任何硬门 → 它的 commit 拦截会让你烦（可关，但那就别装它）

## 诚实声明

- 本插件的方法论是对通用 SOP 写作实践的独立整理（目的/范围/角色/步骤/检查/版本），**不针对任何特定行业法规**；医疗、金融、航空等强监管行业的 SOP 请以贵单位合规要求为准。
- 审计脚本检查的是**文档结构**（编号/责任人/版本/术语等），"流程本身对不对"只能靠访谈和试读，人来把关。
- 本插件不承诺"按此流程写出的 SOP 一定好用"——它消灭的是结构性硬伤，业务正确性它管不着。

## lhg-plugs 插件矩阵

| 插件 | 一句话 | 安装 |
|---|---|---|
| [lhg-sop](https://github.com/lhg-plugs/lhg-sop) | SOP沉淀专家：流程访谈→SOP文档→检查清单→版本管理 | `/plugin install lhg-sop@lhg-plugs` |
| [lhg-sci-figure](https://github.com/lhg-plugs/lhg-sci-figure) | 学术图表专家：数据→期刊规范→图表生成→规范校验，投稿前一次过关 | `/plugin install lhg-sci-figure@lhg-plugs` |
| [lhg-fullstack](https://github.com/lhg-plugs/lhg-fullstack) | 小白一句话 → 高质量全栈应用 | `/plugin install lhg-fullstack@lhg-plugs` |
| [lhg-weekly-review](https://github.com/lhg-plugs/lhg-weekly-review) | 周报复盘专家：记录→结构化周报→亮点→风险预警 | `/plugin install lhg-weekly-review@lhg-plugs` |
| [lhg-biz-report](https://github.com/lhg-plugs/lhg-biz-report) | 商业分析专家：数据到图文报告一键生成 | `/plugin install lhg-biz-report@lhg-plugs` |
| *（更多插件见 [lhg-plugs/marketplace](https://github.com/lhg-plugs/marketplace)）* | | |

## 自检与反馈

本插件自带质检：每次使用后可跑 `python3 smoke_test.py` 一键验证（JSON 合法、skill/command/agent 完整性、17 条规则、fixtures 命中、hooks 行为）。

发现 bug 或有改进建议，以 `[QC] <一句话问题>` 为标题提交到 https://github.com/lhg-plugs/lhg-sop/issues，正文写清"复现步骤 → 实际表现 → 期望表现"。

## 出品：刘洪光

本插件由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 抖音：搜「刘老师讲AI实战」
- 微信：lhgsmsw
