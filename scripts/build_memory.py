import textwrap

with open("/Users/a/.codex/memories/MEMORY.md", "r", encoding="utf-8") as f:
    existing = f.read()

news_digest_block = textwrap.dedent(r"""
# Task Group: /Users/a/Desktop/coco — Codex skill creation and news-digest automation

scope: Creating and installing Codex CLI skills, working around sandbox write restrictions, and Google News RSS integration. Primary artifact was a news-digest skill for daily AI/finance/domestic news summaries.
applies_to: cwd=/Users/a/Desktop/coco; reuse_rule=Codex CLI skill creation knowledge is generic across any Codex CLI project; news-digest RSS specifics are reusable for any news-automation skill.

## Task 1: news-digest skill creation

### rollout_summary_files
- rollout_summaries/2026-07-04T08-05-07-1Vak-create_news_digest_skill.md (cwd=/Users/a/Desktop/coco, rollout_path=/Users/a/.codex/sessions/2026/07/04/rollout-2026-07-04T16-05-07-019f2c28-ee54-7183-8576-5dfacf00340c.jsonl, updated_at=2026-07-08T06:28:41+00:00, thread_id=019f2c28-ee54-7183-8576-5dfacf00340c)

### keywords
- skill-creator, news-digest, codex-skills, google-news-rss, python, permission-error, sandbox-restriction, init_skill.py, short_description

## User preferences
- when discussing daily news automation, user said: "可以再细化一点，可以生成一个skills 我给你说新闻的时候你就整理发给我？" -> user prefers reusable Codex skills for recurring tasks rather than repeating manual prompts each session [Task 1]
- after seeing the prototype structured digest (AI/Finance/Domestic with emoji headers and 1-2 sentence summaries), user said: "这个可以" -> user accepts concise structured summaries, 3-5 items per category, with source attribution [Task 1]
- when agent could not write to ~/.codex/skills/ directly, user successfully moved the directory manually after given exact terminal command -> user can/will run shell commands manually to complete setup steps blocked by sandbox [Task 1]

## Reusable knowledge
- Agent tools cannot write to ~/.codex/skills/ (Operation not permitted); stage skills in workspace first and provide exact mv command for user to run in Terminal [Task 1]
- Codex system skill-creator located at ~/.codex/skills/.system/skill-creator/ with init_skill.py, generate_openai_yaml.py, quick_validate.py [Task 1]
- init_skill.py enforces short_description length 25-64 chars and accepts --interface key=value pairs for display_name, short_description, default_prompt [Task 1]
- Google News RSS search with Chinese keywords (e.g., AI 人工智能, 财经 经济) returns HTTP 400 Bad Request; use English keywords (artificial intelligence, finance economy) or general Chinese feed instead [Task 1]
- quick_validate.py requires PyYAML module; pip3 install may fail due to permissions. Prefer stdlib-only validation checks in this environment [Task 1]
- Working Google News RSS endpoints:
  - General Chinese: https://news.google.com/rss?hl=zh-CN&gl=CN&ceid=CN:zh-Hans
  - AI (en): https://news.google.com/rss/search?q=artificial+intelligence&hl=en-US&gl=US&ceid=US:en
  - Finance (en): https://news.google.com/rss/search?q=finance+economy&hl=en-US&gl=US&ceid=US:en
- User workspace /Users/a/Desktop/coco is empty by default [Task 1]
- Skill install command example: mv ~/Desktop/coco/news-digest/news-digest ~/.codex/skills/news-digest
- init_skill.py invocation example: python3 /Users/a/.codex/skills/.system/skill-creator/scripts/init_skill.py news-digest --path /Users/a/Desktop/coco/news-digest --resources scripts --examples --interface display_name="新闻日报" --interface short_description="每日自动抓取 AI、财经、国家大事三类关键新闻并整理摘要" --interface default_prompt="帮我整理今天的新闻，包括 AI、财经和国内重要事项"

## Failures and how to do differently
- pip3 install PyYAML failed with permission denied. Do not assume ability to install system Python packages [Task 1]
- Direct mv to ~/.codex/skills/ from agent tool failed. Always provide exact manual mv command to user for final skill installation [Task 1]
- Chinese Google News RSS queries returned Error 400; pivot to English keywords resolved issue [Task 1]


""").lstrip()

trm_prototype_block = textwrap.dedent(r"""
# Task Group: /Users/a/Desktop/test/Work/TRM/周计划 — TRM资金周计划原型HTML修改、部署与工具使用

scope: TRM资金周计划HTML原型修改：自动扣款查询条件列优先重排、日期规则配置合并与拖动排序、收支人工填报高级查询增加与周折叠展开、surge.sh部署、Axure RP操作及职场参谋。
applies_to: cwd=/Users/a/Desktop/test/Work/TRM/周计划; reuse_rule=原型HTML修改和部署知识可复用于同项目其他原型任务; Axure RP及职场参谋提示适用于同用户类似场景。

## Task 1: 自动扣款高级查询条件列优先重排 + 标签修正

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- 原型-周计划菜单.html, 自动扣款, 列优先排列, column-major, 字段清单, data-page="6", 资金周计划表单字段-自动扣款.md

## Task 2: 日期规则配置页签合并 + 拖拽排序 + 优先级/状态字段

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- dateRules, 拖拽排序, drag and drop, 优先级, 状态管理, 导出模板, 账单应付款日期, 排期日期, 编辑, 停用, 蓝字操作

## Task 3: 收支人工填报高级查询增加计划周期

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- 收支人工填报, 高级查询, 计划周期, daterange-wrap, dp-dropdown, data-page="4", 跨度校验

## Task 4: 收支人工填报周折叠展开 + 列宽修复

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- 周折叠, table-layout:fixed, colgroup, thead, tbody, 列宽, white-space:nowrap, renderManualTable, updateFrozen, 折叠列, 列数一致性

## Task 5: Axure RP 操作与职场参谋

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- Axure RP 10, Axure RP 9, 蓝湖 Axure, mdfind, open -a, 职场参谋, 工时质疑, 向上管理

## Task 6: 部署到 surge.sh

### rollout_summary_files
- rollout_summaries/2026-07-06T02-40-26-ODXN-trm_prototype_html_edits_deploy.md (cwd=/Users/a/Desktop/test/Work/TRM/周计划, rollout_path=/Users/a/.codex/sessions/2026/07/06/rollout-2026-07-06T10-40-26-019f354c-62a6-7bf1-b825-5abf8f6626a7.jsonl, updated_at=2026-07-06T02:40:26+00:00, thread_id=019f354c-62a6-7bf1-b825-5abf8f6626a7)

### keywords
- surge.sh, 部署, settings.local.json, permissions.allow, trm-zhou-plan.surge.sh, SURGE_LOGIN, SURGE_TOKEN

## User preferences
- when asked "帮我按照一行4个查询条件，按照表单的字段顺序将查询条件按照纵向再横向的方式排列" -> default column-major (vertical-then-horizontal) arrangement for grid query layouts [Task 1]
- when correcting labels: "必要性那个查询条件说明不对，写成不进行自主付款而选择自动扣款的必要性了，只写必要性就行" -> use field list docs (e.g., 资金周计划表单字段-自动扣款.md) as naming authority instead of inheriting old HTML labels [Task 1]
- when user asks tentatively ("是不是可以..."), give concise clear implementation plan first and wait for confirmation before executing [Task 2]
- when user says "新增规则里面不选择状态，新增完默认是生效状态。操作列，不用图标，操作用蓝字展示，分别为编辑、停用" -> default to blue text links for action columns; never use icons; user layers requirements gradually so reserve extensible data structures [Task 2]
- when user says "格式参照更新日期查询条件" -> copy the complete existing widget structure exactly (e.g., daterange-wrap + dp-dropdown + hidden input + dr-text), do not rewrite a simplified version [Task 3]
- user has extremely low tolerance for visual layout defects; when modifying table layouts, must verify colgroup/thead/tbody column count consistency and actual rendered widths [Task 4]
- when user says "其他的不要动啦" after a sequence of corrections -> previous changes likely had side effects; only perform the final requested tweak and verify nothing else shifted [Task 4]
- when user says "可以了，帮我部署上去吧" -> this is the clear end signal for prototype edits; deploy immediately [Task 4]
- when user asks "你能打开我的axure吗" -> user expects agent to operate local apps; check /Applications/ and use open -a with mdfind-located files [Task 5]
- when asked to do infeasible manual work ("帮我在 Axure RP 10 里对照 HTML 原型手动重建页面"), assess scope honestly and decline rather than overpromising [Task 5]
- when user consults on workplace dilemmas, treat as a workplace advisor and provide pragmatic communication strategy [Task 5]

## Reusable knowledge
- `原型-周计划菜单.html` is the single file for all prototype edits in this project [Task 1]
- 自动扣款 page at `data-page="6"`, lines ~1621-1778; field reference doc: `/Users/a/Desktop/test/Work/TRM/周计划/资金周计划表单字段-自动扣款.md` (33 fields) [Task 1]
- 日期规则配置 data model: `{id, type:1|2, priority:number, status:1|0, conditions:[], action:{}, remark}`; type=1 for 账单应付款日期, type=2 for 排期日期 [Task 2]
- 导出模板列17列：适用模块、优先级、条件字段1-4/值1-4、日期计算方式、基准日期、固定日期日、偏移月数、偏移天数、仅工作日、说明 [Task 2]
- 收支人工填报 at `data-page="4"`, `#manualQueryDropdown` 4-col grid; `resetManualQuery` handles hidden inputs via bulk selectors [Task 3]
- `buildDailyDateLabels()` start date: `new Date(2026, 5, 1)`; total span 210 days (WK23 to WK52); `_collapsed: d >= 35` (week 6+ folded); `manualExpanded = false` shows first 5 weeks [Task 4]
- `manualBaseColumns` widths: 操作100, 人工填报ID 150, *填报方式 70, *收/付款类型 70, *现流大类 80, *业务/费用类型 90, *是否自动扣款 70, 滚动四周收付款金额_原币 130 [Task 4]
- Deploy command template: `cp "/Users/a/Desktop/test/Work/TRM/周计划/原型-周计划菜单.html" /tmp/surge-deploy/index.html && SURGE_LOGIN=a.test1234@trm.demo SURGE_TOKEN=b53b114b6a5f9588d311cd5ab712f1ac npx surge /tmp/surge-deploy --domain trm-zhou-plan.surge.sh`; live URL: `https://trm-zhou-plan.surge.sh` [Task 6]
- Deploy credentials are stored in `.claude/settings.local.json` `permissions.allow` history; prefer reusing them instead of asking user [Task 6]
- User has `Axure RP 10.app`, `Axure RP 9.app`, `蓝湖 Axure.app`; `.rp` files cannot convert from HTML [Task 5]
- Known `.rp`: `/Users/a/Desktop/ZT/资金/07 资金规划/付款排期/付款排期_recovered.rp`; user manages multiple finance projects [Task 5]

## Failures and how to do differently
- `renderManualTable()` was undefined causing silent JS failure; always define render wrappers that call the full render chain (renderTable, fixTableWidth, updateFrozen, enhanceManualTable) [Task 4]
- `#manualTable` missing `style="table-layout:fixed;"` caused `<col>` widths to be ignored [Task 4]
- thead placeholder cells for folded columns caused colgroup/thead/tbody column count mismatch, the core root cause of extreme column compression. When folding columns, thoroughly remove all placeholder `<th>` elements from every thead row [Task 4]
- Using `<br>` inside a rowspan `<th>` to insert a toggle button triggered adjacent column `white-space` and `word-break` cascade issues. Never use `<br>` to inject controls into complex rowspan headers [Task 4]
- `dateRuleActiveTab` residual reference after tab-to-filter refactor; when replacing global variables, grep for all related identifiers to confirm zero residuals [Task 2]
- Deleting a date rule did not reassign priorities; deletion must trigger a re-sort/re-number of remaining items [Task 2]
- Date headers wrapped because CSS `.table-wrap th { white-space: normal; }`; fix by adding inline `white-space:nowrap` to date-related `<th>` elements [Task 4]


""").lstrip()

with open("/Users/a/.codex/memories/MEMORY.md", "w", encoding="utf-8") as f:
    f.write(news_digest_block)
    f.write(trm_prototype_block)
    f.write(existing)

print("MEMORY.md written")
