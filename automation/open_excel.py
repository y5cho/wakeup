from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active
print(wb.sheetnames)
ws2 = wb["sheet2"]

for x in range(1, ws2.max_row +1):
    for y in range(1, ws2.max_column +1):
        print(ws2.cell(row=x, column=y).value, end=" ")
    print()

