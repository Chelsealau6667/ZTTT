import openpyxl
import os

REVIEW_DIR = "/Users/a/Desktop/ZT/FSSC/R406/invoice/发票模版-评审"

def verify_file(filepath, name):
    print(f"\n{'='*60}")
    print(f"VERIFY: {name}")
    print(f"{'='*60}")
    wb = openpyxl.load_workbook(filepath)
    ws = wb.worksheets[0]
    
    if "加拿大" in name:
        rows = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    elif "温哥华" in name:
        rows = [28, 29, 30, 31, 32, 33, 34, 35, 36]
    elif "澳洲" in name:
        rows = [14, 24, 25, 26, 27]
    elif "日本" in name:
        rows = [21]
    elif "深圳" in name or "香港" in name:
        rows = list(range(17, 25))
    else:
        rows = []
        print(f"  No rows selected for {name}")
    
    for row in rows:
        for col in range(1, 8):
            cell = ws.cell(row=row, column=col)
            if cell.value:
                color = None
                if cell.font and cell.font.color:
                    color = str(cell.font.color.rgb)
                print(f"  [{row},{col}] '{cell.value}' color={color}")

# Verify key files
for fname in [
    "FBU-加拿大谷仓发票模版-HST税率13%（正数）.xlsx",
    "FBU-加拿大谷仓发票模版-HST税率13%（负数）.xlsx", 
    "FBU-温哥华模版-GST税率(0%、5%）正数.xlsx",
    "FBU-澳洲谷仓开票模板.xlsx",
    "FBU-日本谷仓开票模版.xlsx",
    "ABU-深圳云颂开票模板.xlsx",
]:
    filepath = os.path.join(REVIEW_DIR, fname)
    verify_file(filepath, fname)
