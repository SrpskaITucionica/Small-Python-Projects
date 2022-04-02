'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''


from openpyxl import Workbook
import sqlite3

'''
    This part of code converts SQL table into Excel file.
    Database name, table name and excel file name are generic.
    DB should be in the same folder as main.py module, or any module that runes this code
'''

###################### WORKING WITH SQL PART ######################

con = sqlite3.connect('database_name.db')
cursor = con.cursor()

get_data_from_table_sql = "SELECT * FROM table_name"
cursor.execute(get_data_from_table_sql)
# GET TABLE DATA
rows = cursor.fetchall()

# GET COLUMN NAMES
cursor2 = con.execute('SELECT * FROM table_name')
names = list(map(lambda x: x[0], cursor.description))

###################### WORKING WITH EXCEL PART ######################

wb = Workbook()
ws = wb.active
ws.title = 'Worksheet name'

ws.append(names)
for row in rows:
    ws.append(list(row))

wb.save('excel_file_name.xlsx')
