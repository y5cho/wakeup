from openpyxl import load_workbook
from random import *

from openpyxl.workbook.workbook import Workbook

wb = load_workbook("Book1.xlsx")
sheets = wb.sheetnames
Sheet1 = wb[sheets[0]]
Sheet2 = wb.create_sheet("Sheet2")
Sheet1.cell(row = 2, column = 4).value = 5 



wb.save("Book1.xlsx")