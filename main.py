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
print(upc_list)
print(upc_set)

ws.cell(1, 1).value = 'UPC'
j = 2
for i in upc_set:
    ws.cell(j, 13).value = str(i)
    j += 1

# rows = ws.max_row
# for i in range(1, 13):
#     ws.delete_cols(idx=i)
# ws.move_range(cell_range='M1:M' + str(rows), cols=-12)

wb.save('dvd2.xlsx')
