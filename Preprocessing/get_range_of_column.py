# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 03:32:57 2019
Поиск диапазона значений
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

for i in ('IdCaseType1',): # Список столбцов или столбец
    req = 'SELECT ' + i + ' FROM dbo.Запрос2'
    cur.execute(req)
    ans = cur.fetchall()
    
    data_range = []
    for j in range(length):
        if (ans[j][0] is not None):
            flag = 0
            for k in range(len(data_range)):
                if (data_range[k] == ans[j][0]):
                    flag = 1
            if (flag == 0):
                data_range.append(ans[j][0])
            if (len(data_range) > 100):
                break
        
    print(i, ': ', sorted(data_range))
