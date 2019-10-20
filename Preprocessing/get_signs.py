import pandas as pd
import csv

# Функция проверки на пустое поле (NaN)
def isNaN(num):
     return num != num

# Функция для определения признаков. На вход подается одномерный dataframe. Возвращает список, первым элементом которого id больницы. Осталные элементы - признаки в диапозоне [0, 1]
def def_sign(df):
     lst = ['IdCase1', 'IdLpu1', 'IdCase2', 'IsActive', 'IdCase3', 'AIDSMark', 'IdStep1', 'SystemGuid2', 'IdStep2', 'IdHospitalDepartment', 'IdStep3', 'IdVisitPurpose', 'IdPaymentType2', 'RecordCreated2', 'IdAddress1', 'RecordCreated3', 'IdAddress2', 'RecordCreated4', 'IdRCasePaymentType', 'Name2', 'IDDoctor3', 'IdLpu2', 'IdSpeciality2', 'RecordCreated6', 'IdRVisitPlace', 'Name4', 'IdRVisitPurpose', 'Name5', 'IdCaseResult2', 'RecordCreated7', 'IdMedDocument2', 'IdDocumentMis', 'IdAmbulanceInfo', 'IdMedDocument3', 'IdHospReferral', 'IdTargetLpu', 'Idl1', 'Active_l1', 'Idl2', 'Active_l2', 'IdIntoxicationType2', 'RecordCreated9', 'IdRHospitalizationOrder', 'Name9', 'IdRHospitalizationPrimacy2', 'Name10', 'IdTypeFromDiseaseStart2', 'RecordCreated10', 'IdDiagnosis', 'RecordCreated11', 'IdDiagnosisType2', 'RecordCreated12', 'IdRDiseaseType', 'Name13', 'IdRDispensaryState2', 'Name14', 'IdRTraumaType2', 'Name15', 'IdRHospResult', 'Name16', 'IdSickList', 'IdCareGiver', 'IdService', 'Status_srv', 'IdServiceType2', 'RecordCreated15', 'IdPrescribedMedication', 'Status_prem', 'IdMedDocumentType2', 'FhirCode', 'IdRTraumaType1', 'Name18', 'IdCaseType2', 'Parent_Id', 'IdCase', 'IdRTFORMSMedicalStandard', 'IdRTFORMSMedicalStandard2', 'Children']
     signs = []
     #signs.append(df['Index']) раскомментировать, при добавление индексов в исходную выборку
     signs.append(df['IdLpu1'])
     for j in range(0, len(lst), 2):
          number_not_Nan = 0
          number = 0
          for i in (df.loc[lst[j]:lst[j+1]]):
               number += 1
               if isNaN(i) == False:
                    number_not_Nan += 1
          signs.append(number_not_Nan / number)
     return signs


# Считывание больниц одного направления из текстового файла и занесение их в список
f = open('hospitals', 'r')
hospitals = []
for line in f:
     hospitals.append(line[:-1])

# Считывание csv файла всей выборки
df = pd.read_csv(r"/home/jason/Downloads/top100.xlsx - sheet1.csv")

# Фильтрация нужных больниц из всей выборки
df = df.loc[df['IdLpu1'].isin(hospitals)]

# Создание названия столбцов для выходного csv файла
name_of_blocks = []
#name_of_blocks.append('Index') раскомментировать, при добавление индексов в исходную выборку
name_of_blocks.append('IdHospital')
for i in range(39):
    name_of_blocks.append('block_' + str(i))

# Присваивание признаков
signs = []
signs.append(name_of_blocks)
for i in df.index:
     signs.append(def_sign(df.loc[i]))

# вывод признаков в файл csv
with open('signs.csv', 'w') as f:
     wtr = csv.writer(f, dialect="excel")
     wtr.writerows(signs)
