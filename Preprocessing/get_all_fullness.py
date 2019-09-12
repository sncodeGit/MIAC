# -*- coding: utf-8 -*-
"""
Вывод процентов пропусков по всем столбцам
@author: inter000
"""

import pymssql
import pandas as pd

length = 892489 # Количество записей в выгрузке

df = pd.read_excel('top1.xlsx') # top1.xlsx - файл с названиями столбцов (см. Google диск)
ser = pd.Series(df.columns) # Можно использовать для целочисленного перебора по номерам столбцов 
#Ex: (ser[0] - название первого столбца и тд)

conn = pymssql.connect(host='localhost', user='sa', 
                       password='your_passw', database='test_regiz') # заменить your_passw
cur = conn.cursor()

for i in range(247): # Можно заменить на конкретные столбцы
    counter = 0
    
    req = 'SELECT ' + ser[i] + ' FROM dbo.Запрос2'
    cur.execute(req)
    ans = cur.fetchall()
    
    for j in range(length):
        if (ans[j][0] is None):
            counter += 1
    
    print(ser[i], " : ", counter/length*100)
