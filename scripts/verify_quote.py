import textwrap

c = textwrap.dedent(r"""
- 部署等凭据优先从历史权限（如`.claude/settings.local.json`的`permissions.allow`）复用
""").lstrip()

with open("/Users/a/Desktop/ZT/FSSC/invoice/quote_test.txt", "w", encoding="utf-8") as f:
    f.write(c)
print("written")
