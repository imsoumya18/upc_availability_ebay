import os
import openpyxl
import glob
from openpyxl.styles import Alignment

for file in os.listdir('sheets'):
    wb = openpyxl.load_workbook()
    ws = wb.worksheets[0]
    print(ws)
