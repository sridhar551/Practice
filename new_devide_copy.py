import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter


nfp = pd.read_excel("/home/sree/Downloads/Personal/S2.xlsx", parse_dates=[0], infer_datetime_format=True)
temp = pd.DatetimeIndex(nfp['IN'])
nfp['Date'] = temp.date
nfp['In'] = temp.time
del nfp['IN']
temp1 = pd.DatetimeIndex(nfp['OUT'])
#nfp['Date_Out'] = temp1.date
nfp['Out']= temp1.time
del nfp['OUT']

#nfp['Date_In']=pd.to_datetime(nfp.Date_In)
#nfp.sort_values(by=['Date_In'])
nfp.to_excel('/home/sree/Downloads/Personal/S5.xlsx',index=False)

print('Cogratulations!!! Date and time devided')

path = r"/home/sree/Downloads/Personal/S5.xlsx"

book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

x3 = np.random.randn(0,0)
df3 = pd.DataFrame(x3)

x4 = np.random.randn(0,0)
df4 = pd.DataFrame(x4)

df3.to_excel(writer, sheet_name = 'x3')
df4.to_excel(writer, sheet_name = 'x4')

writer.save()

#writer = reader[reader['Date']=='2018-03-01']
#writer.close()

print('Congratulations!!! New sheests created')

reader = pd.read_excel('/home/sree/Downloads/Personal/S4.xlsx')
df = pd.DataFrame(reader)
writer = pd.ExcelWriter('/home/sree/Downloads/Personal/S5.xlsx', engine = 'xlsxwriter')
select1 = reader[reader['Date'] == '2018-03-02']
df.to_excel(writer,sheet_name='x3')
writer.save()
writer.close()

'''reader = pd.read_excel('/home/sree/Downloads/Personal/S4.xlsx')
df = pd.DataFrame(reader)
writer = pd.ExcelWriter('/home/sree/Downloads/Personal/S5.xlsx', engine = 'xlsxwriter')
select2 = reader[reader['Date']=='2018-03-02']
df.to_excel(writer,sheet_name='x4')

writer.save()
writer.close()'''