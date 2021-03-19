import openpyxl
from openpyxl.styles import Alignment
import os

upc_list = []
upc_set = ()

print(type(os.listdir('sheets')))

for i in os.listdir('F:\\Github\\upc_availability_ebay\\sheets'):
    wb = openpyxl.load_workbook('F:\\Github\\upc_availability_ebay\\sheets\\' + i)
    ws = wb.worksheets[0]
    print(ws)
