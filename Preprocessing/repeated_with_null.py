# -*- coding: utf-8 -*-
"""
Поиск всех столбцов совпадающих полостью за исключение NULL-ов. (с отношением РОДИТЕЛЬ <-> РЕБЁНОК)
Условно есть стобец ID1. Он заполнен для всех записей. Также есть ID2 в блоке со случаями госпитализации. 
ID2 всегда дублирует ID1, но только в случаях, которые закончились госпитализацией.
Используются такие столбцы для связи различный таблиц в БД, но в выгрузке этот факт не может быть отображён.
@author: PapernyukAlex
"""
import pandas as pd
import numpy as np

def getDuplicateColumns_with_null(df):
    duplicateColumnNames = []
    for x in range(df.shape[1]):
        print x
        for y in range(x + 1, df.shape[1]):
            a = np.where(np.invert(pd.isnull(df.iloc[:, y])))
            b = np.where(np.invert(pd.isnull(df.iloc[:, x])))
            c = np.intersect1d(a,b)
            if c.size != 0:
                if np.array_equal(df.iloc[c, x].values, df.iloc[c, y].values):
                    duplicateColumnNames.append((df.columns.values[x], df.columns.values[y]))
    return duplicateColumnNames
