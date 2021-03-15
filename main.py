import openpyxl

wb = openpyxl.load_workbook('dvd.xlsx')
ws = wb.worksheets[0]

upc_list = []
upc_set = ()

for i in range(1, 13):
    if ws.cell(2, i).value == 'UPC':
        j = 3
        while ws.cell(j, i).value is not None:
            upc_list.append(ws.cell(j, i).value)
            j += 1

upc_set = set(upc_list)

print(len(upc_list))
print(len(upc_set))

wb.save('dvd2.xlsx')
