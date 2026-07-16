
content = open('/Users/a/.codex/memories/memory_summary.md').read()
content = content.replace("部署等凭据优先从历史权限（如的）复用", "部署等凭据优先从历史权限（如`.claude/settings.local.json`的`permissions.allow`）复用")
content = content.replace("Claude Code skills必须使用子目录格式，flat文件不被识别", "Claude Code skills必须使用子目录格式`.claude/skills/<skill-name>/SKILL.md`，flat文件不被识别")
content = content.replace("TRM业务规则分散在子目录（如）中", "TRM业务规则分散在`sibling`子目录（如`周计划/`）中")
content = content.replace("HTML表格使用控制列宽时，必须在设置，并保证colgroup/thead/tbody列数严格一致", "HTML表格使用`<col>`控制列宽时，必须在`<table>`设置`table-layout:fixed`，并保证colgroup/thead/tbody列数严格一致")
content = content.replace("不要在rowspan表头内用插入控件", "不要在rowspan表头内用`<br>`插入控件")
content = content.replace("surge.sh部署命令和凭据可从的中查找历史记录", "surge.sh部署命令和凭据可从`.claude/settings.local.json`的`permissions.allow`中查找历史记录")
content = content.replace("Codex CLI无法直接写入（Operation not permitted）；需在workspace中staging skill，然后提供精确命令让用户手动执行", "Codex CLI无法直接写入`~/.codex/skills/`（Operation not permitted）；需在workspace中staging skill，然后提供精确`mv`命令让用户手动执行")
content = content.replace("init_skill.py强制要求 25-64字符，并通过传display_name/short_description/default_prompt", "init_skill.py强制要求`short_description` 25-64字符，并通过`--interface`传display_name/short_description/default_prompt")
content = content.replace("复杂表格折叠列时，必须彻底移除thead所有行中的占位，colgroup/thead/tbody列数失配是列宽压缩的根因", "复杂表格折叠列时，必须彻底移除thead所有行中的占位`<th>`，colgroup/thead/tbody列数失配是列宽压缩的根因")
content = content.replace("未定义会导致JS静默失败；任何新渲染函数必须定义完整调用链", "`renderManualTable()`未定义会导致JS静默失败；任何新渲染函数必须定义完整调用链")
content = content.replace("文件无法从HTML自动转换，必须在Axure中手工重建", "`.rp`文件无法从HTML自动转换，必须在Axure中手工重建")
content = content.replace("用户机器安装了、、", "用户机器安装了`Axure RP 10.app`、`Axure RP 9.app`、`蓝湖 Axure.app`")
# fix TRM monitoring learnings
content = content.replace("业务规则分散在等sibling目录中", "业务规则分散在`sibling`子目录中")
with open('/Users/a/.codex/memories/memory_summary.md', 'w') as f:
    f.write(content)
print("fixed")
