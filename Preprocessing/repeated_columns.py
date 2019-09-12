import pandas as pd
import numpy as np

def getDuplicateColumns(df):
    duplicateColumnNames = []
    for x in range(df.shape[1]):
        col = df.iloc[:, x]
        for y in range(x + 1, df.shape[1]):
            otherCol = df.iloc[:, y]
            if col.equals(otherCol):
                duplicateColumnNames.append((df.columns.values[y], df.columns.values[x]))
    return duplicateColumnNames

def makeListOfPairs(same_columns):
    columns = []
    for i, j in same_columns:
        exist = 0
        iter_ = 0
        for ind in columns:
            if j in ind:
                if i not in ind:
                    columns[iter_].append(i)
                exist = 1
                break
            iter_ = iter_ + 1
        if not exist:
            columns.append([j, i])
    return columns

df1 = pd.read_excel (r'C:\\top3000.xlsx')
df = pd.read_csv(r'C:\\Users\\paper\\Downloads\\test_regiz.csv', sep=';', error_bad_lines=False,header = None,names=df1.columns)
df_new = df.drop([u'CityName',
u'PostalCode',
u'IdSourceLpu_M1',
u'TreatmentDays',
u'PrescriptionNo',
u'Status_prem',
u'IdTargetLpu_M1',
u'IdCareGiver',
u'IdRVisitPaymentType',
u'PrescriptionSeries',
u'Status_srv',
u'Country',
u'ModificationDate',
u'IdRPaymentStatus',
u'Tariff',
u'ReferralId',
u'IdRMedicineType',
u'IdComponent_l1',
u'DayDose',
u'SystemGuid2',
u'Region',
u'IdIntoxicationType1',
u'IdIntoxicationType2',
u'GeoData',
u'RecordCreated9',
u'Quantity',
u'IdRMedicineUseWay',
u'IdLpu_M12',
u'IdLpu_M11',
u'IdRHealthCareUnit',
u'Name8',
u'RelatedId'], axis= 1)#Выкидываю пустые колонки

same_columns = getDuplicateColumns(df_new)
same_col_list = makeListOfPairs(same_columns)
print same_col_list
