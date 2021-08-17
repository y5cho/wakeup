from openpyxl import Workbook 

#-----------------sheet-------------
wb = Workbook() 
ws = wb.active 
ws2 = wb.create_sheet("mysheet")
w3 = wb.create_sheet("newsheet", 1)

ws.title = "sheesh"

ws2.sheet_properties.tabColor = "ff66ff" #RGB color 

print(wb.sheetnames)

sheet1 = wb["mysheet"]
sheet1["A1"] = "Test"
target = wb.copy_worksheet(sheet1)
target.title = "copied sheet"


#-----------------sheet-------------




wb.save("sample.xlsx")
wb.close()


