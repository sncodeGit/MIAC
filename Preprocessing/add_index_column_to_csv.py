# -*- coding: utf-8 -*-
"""
Добавление в конец csv-файла FILE_NAME любого размера столбца Index, содержащего нумерацию строк с номера act_ind
@author: inter000
"""

import pandas as pd

CHUNK_SIZE = 10000 # Количество обрабатываемых за одну итерацию строк
FILE_NAME = 'test_regiz.csv' # Имя изначального файла. Измененные данные будут записаны в файл с префиксом ind_

act_ind = 0 # Значение первого индекса в каждой (в т.ч. и в первой) итерации
for chunk in pd.read_csv(FILE_NAME, low_memory=False, chunksize=CHUNK_SIZE):
    chunk['Index'] = [i for i in range(act_ind, len(chunk.index) + act_ind)]
    if act_ind == 0:
        # index=False - не включает в файл индекы, присваемые Pandas-ом автоматически.
        chunk.to_csv('ind_' + FILE_NAME, mode='w', index=False)
    else:
        # header=None - не включает в файл дубли header-а (записан в первой итерации). 
        # mode='a' - запись в конец файла
        chunk.to_csv('ind_' + FILE_NAME, header=None, mode='a', index=False)
    act_ind += chunk_size
