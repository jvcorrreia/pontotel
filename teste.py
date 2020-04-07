'''import os

diretorio = os.listdir('./')
if "index.html" in diretorio:
    os.remove('index.html')

arquivo = open('index.html','w')
arquivo.write("<html><body>olaa<body><html>")
arquivo.close()'''
from alpha_vantage.timeseries import TimeSeries
key = 'S41GDLHL4C6MJSHN'
ts = TimeSeries(key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='^BVSP', outputsize='full')
print('os dados de hoje da bovespa são:')
print((data.head(1)))

#('Banco do Brasil', "BDORY"),
#('Vale S.A.', "VALE"),
#('Petrobrás', "PBR"),
#('Santander', "SAN")
#('JBS', "JBSS"),
#('CSN', "SID"),