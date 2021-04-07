import openpyxl
from openpyxl.styles import Alignment
import os

upc_list = []
upc_set = ()
print(os.getcwd() + '\\sheets')
for file in os.listdir(os.getcwd() + '\\sheets'):
    wb = openpyxl.load_workbook(os.getcwd() + '\\sheets\\' + file)
    wb2 = openpyxl.Workbook()

    ws = wb.worksheets[0]
    ws2 = wb2.create_sheet(title='Sheet1', index=0)

    for i in range(1, 100):
        if ws.cell(2, i).value == 'UPC':
            j = 3
            while ws.cell(j, i).value is not None:
                upc_list.append(ws.cell(j, i).value)
                j += 1

upc_set = set(upc_list)

ws2.cell(1, 1).value = 'UPC'
ws2.cell(1, 2).value = 'Total Count'
ws2.cell(1, 3).value = 'Boxes'

j = 2
for i in upc_set:
    ws2.cell(j, 1).value = i
    ws2.cell(j, 1).number_format = '0'
    if upc_list.count(i) != 1:
        ws2.cell(j, 2).value = 'x' + str(upc_list.count(i))
        ws2.cell(j, 2).alignment = Alignment(horizontal='right')
    for k in range(1, 100):
        if ws.cell(2, k).value == 'UPC':
            l = 3
            while ws.cell(l, k).value is not None:
                if ws.cell(l, k).value == i:
                    if ws2.cell(j, 3).value is not None:
                        ws2.cell(j, 3).value += ws.cell(1, k).value[-1] + '   '
                    else:
                        ws2.cell(j, 3).value = ws.cell(1, k).value[-1] + '   '
                # break
                l += 1
    j += 1

ws2.column_dimensions['A'].width = 18.22
ws2.column_dimensions['B'].width = 18.22
ws2.column_dimensions['C'].width = 40

wb2.save('output.xlsx')
