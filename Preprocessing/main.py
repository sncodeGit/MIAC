import pandas as pd


def isNaN(num):
    return num != num

k = 3 # параметр, показывающий максимальное кол-во столбцов, по которым строки различаются
num = 0 # количество удаленных строк
df = pd.read_csv(r"/home/jason/Downloads/top100.xlsx - sheet1.csv")


for row in range(df.shape[0] - 1, 0, -1):
    for i in range(1, row):
        j = 0
        f = False
        for col in df:
            if df.loc[row][col] != df.loc[row - i][col] and isNaN(df.loc[row][col]) == False:
                j += 1
            if j > k:
                break
        if j <= k:
            num += 1
            df = df.drop(row)
            f = False
            break
        if f == False:
            break




print("number of repetitions = ", num)
print("shape df:")
print(df.shape)
