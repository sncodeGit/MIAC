# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 03:17:10 2019
Поиск хотя бы одного примера записи
@author: inter000
"""

import pymssql
import pandas as pd

length = 892489 # Количество записей в выгрузке

df = pd.read_excel('top1.xlsx') # top1.xlsx - файл с названиями столбцов (см. Google диск)
ser = pd.Series(df.columns)

conn = pymssql.connect(host='localhost', user='sa', 
                       password='your_passw', database='test_regiz') # заменить your_passw
cur = conn.cursor()

for i in ('IdAmbResult',): # Столбец или список столбцов
    req = 'SELECT ' + i + ' FROM dbo.Запрос2'
    cur.execute(req)
    ans = cur.fetchall()
    
    for j in range(length):
        if (ans[j][0] is not None):
            print(i, ': ', ans[j][0])
            break
