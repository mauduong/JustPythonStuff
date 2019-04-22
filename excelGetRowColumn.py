#! /usr/bin/python3
# excelGetRowColumn.py
# mauduong
# 21/04/2019

import openpyxl

workBook = openpyxl.load_workbook('example.xlsx')

# Method 1
sheet = workBook.['Sheet1']
tuple(sheet['A1':'C3'])

for cellObjectRow in sheet['A1':'C3']:
    for cellObjectColumn in cellObjectRow:
        print(cellObjectColumn.coordinate, cellObjectColumn.value)
    print('End of Row')


# Method 2
sheet = workBook.active
sheet.columns[1]
for cellObjectRow in sheet.columns[1]:
    print(cellObjectRow.value)
