import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.load_workbook('dvd.xlsx')
wb2 = openpyxl.Workbook()

ws = wb.worksheets[0]
ws2 = wb2.create_sheet(title='Sheet1', index=0)

upc_list = []
upc_set = ()

for i in range(1, 13):
    if ws.cell(2, i).value == 'UPC':
        j = 3
        while ws.cell(j, i).value is not None:
            upc_list.append(ws.cell(j, i).value)
            j += 1

upc_set = set(upc_list)

ws2.cell(1, 1).value = 'UPC'
ws2.cell(1, 2).value = 'Count'
j = 2
for i in upc_set:
    ws2.cell(j, 1).value = i
    ws2.cell(j, 1).number_format = '0'
    if upc_list.count(i) != 1:
        ws2.cell(j, 2).value = 'x' + str(upc_list.count(i))
        ws2.cell(j, 2).alignment = Alignment(horizontal='right')
    j += 1

ws2.column_dimensions['A'].width = 18.22

wb2.save('output.xlsx')
