import openpyxl, pprint

print('Opening Workbook.....')
wb = openpyxl.load_workbook('L1.xlsx')
#type(wb)
#wb.get_sheet_names()
sheet = wb.get_sheet_by_name(wb['Master'])
Inventry = {}

print('Reading rows........')
for row in range(2, sheet.max_row + 1):
    Name = sheet['B' + str(row)].value
    Department = sheet['C' + str(row)].value
    