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
