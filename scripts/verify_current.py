import openpyxl
import os

REVIEW_DIR = "/Users/a/Desktop/ZT/FSSC/R406/invoice/发票模版-评审"
filepath = os.path.join(REVIEW_DIR, "FBU-加拿大谷仓发票模版-HST税率13%（正数）.xlsx")
wb = openpyxl.load_workbook(filepath)
ws = wb.worksheets[0]

for row in range(26, 37):
    for col in range(1, 6):
        cell = ws.cell(row=row, column=col)
        if cell.value:
            color = None
            if cell.font and cell.font.color:
                color = str(cell.font.color.rgb)
            print(f"  [{row},{col}] '{cell.value}' color={color}")
