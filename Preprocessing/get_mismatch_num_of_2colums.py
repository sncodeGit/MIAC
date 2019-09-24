# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:55:46 2019
Поиск количества несовпадающих значений (не считая при None хотя бы в одном из столбцов) в столбцах (COLUMN1 и COLUMN2)
и вывод первых EXAMPLE_NUM из них (индексация строк с нуля)
@author: inter000
"""

import pymssql

LENGTH = 892489 # Количество записей в выгрузке
EXAMPLE_NUM = 10 # Количество выводимых примеров несовпадений в столбцах
COLUMN1 = 'IdDoctor2'
COLUMN2 = 'IdDiagnosedDoctor'

conn = pymssql.connect(host='localhost', user='sa', 
                       password='173bcm248fa4Z', database='test_regiz') # заменить your_passw
cur = conn.cursor()

req = 'SELECT ' + COLUMN1 + ' FROM dbo.Запрос2'
cur.execute(req)
column1_req = cur.fetchall()

req = 'SELECT ' + COLUMN2 + ' FROM dbo.Запрос2'
cur.execute(req)
column2_req = cur.fetchall()

mismatch_count = 0
example_count = 0
for i in range(LENGTH):
    if ( (column1_req[i][0] is not None) and (column2_req[i][0] is not None) ):
        if (column1_req[i][0] != column2_req[i][0]):
            mismatch_count += 1
            if (example_count < EXAMPLE_NUM):
                example_count += 1
                print('Номер строки:', i)
                print(COLUMN1, ': ', column1_req[i][0])
                print(COLUMN2, ': ', column2_req[i][0])
                print('-------')
                
print('Number of mismatches between', COLUMN1, 'and', COLUMN2, ':', mismatch_count)
