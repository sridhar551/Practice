import pandas as pd


nfp = pd.read_csv("/home/sree/Downloads/Personal/S1.csv", parse_dates=[0], infer_datetime_format=True)
temp = pd.DatetimeIndex(nfp['col2'])
nfp['Date'] = temp.date
nfp['Time_In'] = temp.time
del nfp['col2']
temp1 = pd.DatetimeIndex(nfp['col3'])
#nfp['Date_Out'] = temp1.date
nfp['Time_Out']= temp1.time
del nfp['col3']

#nfp['Date_In']=pd.to_datetime(nfp.Date_In)
#nfp.sort_values(by=['Date_In'])
nfp.to_csv('/home/sree/Downloads/Personal/S3.csv',index=False)

print('Cogratulations!!! Date and time devided')

