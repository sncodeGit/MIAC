# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:00:04 2019
Вывод количества записей разных типов мед. учреждений в выгрузке

Необходимо:
файл manual_MO.xlsx, выгрзку в excel из справочника МО
файл num_of_hosp_records формата id_МО:количество_записей_в_выгрузке

Вывод:
файлы count_of_rows_by_medorgtype.txt и count_of_rows_by_medobjtype.txt
формата code_of_MO_type:количество_записей_в_выгрузке

Вывод поделён на два файла в связи с наличием двух непересекающихся типов
классификации больниц (по medobjtype и medorgtype)
@author: inter000
"""

import openpyxl
from openpyxl.utils import column_index_from_string

MAX_ROW = 1834 # Количество строк в manual_MO

# Вывод в file_name записей в формате code_of_MO_type:количество_записей_в_выгрузке
def write_code_count(column_name, file_name):
    column_ind = column_index_from_string(column_name)
    mo_code_ind = column_index_from_string('AJ') # AJ - код столбца 'Код' (код МО)
    codes_count = {} # key - код типа МО, value - количество записей с этим типом
    
    for i in range(2, MAX_ROW + 1):
        elem = main_sheet.cell(row = i, column = column_ind).value
        elem_mo_code = main_sheet.cell(row = i, column = mo_code_ind).value
        if (elem_mo_code in MO_count) and (elem is not None):
            if elem in codes_count:
                codes_count[elem] += MO_count[elem_mo_code]
            else:
                codes_count[elem] = MO_count[elem_mo_code]                  
                
    file = open(file_name, 'w')
    for code in codes_count.keys():
        file.write(code + ':' + str(codes_count[code]) + '\n')
    file.close()

file = open('num_of_hosp_records', 'r')
lines = file.readlines()

MO_count = {} # key - код МО, value - количество записей этой больницы
for line in lines:
    split_line = line.split(':') # MO_code:count_of_rows
    MO_count[split_line[0]] = int(split_line[1].replace('\n',''))

file.close()

wb = openpyxl.load_workbook('manual_MO.xlsx') # Открываем файл xlsx
main_sheet = wb['Reference data'] # Выбираем таблицу файла

# Y - код столбца 'medorgtype, codes' 
write_code_count('Y','count_of_rows_by_medorgtype.txt')
# AE - код столбца 'medobjtype, codes' 
write_code_count('AE','count_of_rows_by_medobjtype.txt')
