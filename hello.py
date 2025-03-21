import openpyxl as xl
wb = xl.load_workbook('transaction.xlsx')
sheet = wb['Sheet1']
cell1 = sheet['a1']
cell2 = sheet.cell(1,1)
print(cell.value)