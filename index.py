from alpha_vantage.timeseries import TimeSeries

import os
import time


#Chave de Api
#key = 'S41GDLHL4C6MJSHN'
key = 'KSOIPCQCA47QFSTI'

#Formato de output
ts = TimeSeries(key, output_format='pandas')

#Setando as páginas que serão criadas
sitescriados = ['itau.html', "brad.html", "bb.html", "ambev.html", "san.html", "vale.html", "jbs.html",
         "petrobras.html","oi.html", "csn.html"]

#Função para chamar os dados diários da bovespa
def bovespa_daily():
    data, meta_data = ts.get_daily(symbol='^BVSP', outputsize='full')
    print('os dados de hoje da bovespa são:')
    x = str(data.head(1))
    #Transformando em strings para poder filtrar melhor
    y = str.split(x)
    print(y)

    #Pegando os dados importantes para levar ao site
    date = y[11]
    abriu = y[12]
    alta = y[13]
    baixa = y[14]
    fechou = y[15]


    #Removendo os sites que possam ter sido criados anteriormente
    diretorio = os.listdir('./')
    for i in range(9):
        if sitescriados[i] in diretorio:
            os.remove(sitescriados[i])
    if "index.html" in diretorio:
        os.remove('index.html')

    #Criando a página que vai conter o conteúdo do index
    time.sleep(5)
    arquivo = open('index.html', 'w')
    arquivo.write('''<html>
    <head>
        <title>Exibindo Relatorio</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <h1 style="text-align: center;">Olá, a cotação do dia da bovespa é:</h1>
        <ul class="list-group">

            <li class="list-group-item">
                Data: ''' + date +  '''
            </li>
            <li class="list-group-item">
                Valor de abertura: '''+ abriu +  '''
            </li>
            <li class="list-group-item">
                Valor de alta: '''+ alta +  '''
            </li>
            <li class="list-group-item">
                Valor de baixa: '''+ baixa +  '''
            </li>
            <li class="list-group-item">
                Valor de fechamento: '''+ fechou +  '''
            </li>     
            <h2 style="text-align: center;">Escolha uma das empresas para ver dados:</h2>
        </ul>
            <ul class="list-group">
            <li class="list-group-item">
                <a href="./itau.html">Itaú Unibanco</a>
            </li>
            <li class="list-group-item">
                <a href="./brad.html">Bradesco</a>
            </li>
            <li class="list-group-item">
                <a href="./bb.html">Banco do Brasil</a>
            </li>
            <li class="list-group-item">
                <a href="./ambev.html">Ambev</a>
            </li>
            <li class="list-group-item">
                <a href="./san.html">Santander</a>
            </li>
            <li class="list-group-item">
                <a href="./vale.html">Vale</a>
            </li>
            <li class="list-group-item">
                <a href="./jbs.html">JBS</a>
            </li>
            <li class="list-group-item">
                <a href="./petrobras.html">Petrobras</a>
            </li> 
            <li class="list-group-item">
                <a href="./oi.html">OI</a>
            </li>
            <li class="list-group-item">
                <a href="./csn.html">CSN</a>
            </li>            
        </ul>
    </body>
</html>'''
        )
    arquivo.close()


#Lista com as maiores empresas brasileiras que serão chamadas logo abaixo

maiores_empresas = [
                    ('Itaú Unibanco', "ITUB"),
                    ('Bradesco', "BBDC"),
                    ('Banco do Brasil', "BDORY"),
                    ('Ambev', "ABEV"),
                    ('Santander', "SAN"),
                    ('Vale S.A.', "VALE"),
                    ('JBS', "JBSS"),
                    ('Petrobrás', "PBR"),
                    ('OI', "OIBRQ"),
                    ('CSN', "SID"),
                    ]


#Função para escolher a empresa que se deseja obter as informações
def brcompanyinfo():
    indice = 0
    print('Tive que colocar delay na função, pois a api só limita a 5 requisições por minuto.')
    print('por isso, deve demorar cerca de 1 minuto para essa função')
    for i in range(9):
        symbolca = maiores_empresas[indice][1]#Pegando o simbolo de cada empresa
        nome = maiores_empresas[indice][0]#Pegando o nome de cada empresa
        site = open(sitescriados[i], 'w')#Criando o site
        data, meta_data = ts.get_daily(symbol=symbolca, outputsize='full')
        print('os dados de hoje de ' + nome + ' :')
        x = str(data.head(1))
        y = str.split(x)#Transformando em lista de strings
        time.sleep(10)

        print(y)
        # Pegando os dados importantes para levar ao site
        date = y[11]
        hour = y[12]
        abriu = y[13]
        alta = y[14]
        baixa = y[15]
        fechou = y[16]

        site.write('''<html>
            <head>
                <title>Exibindo Relatorio</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            </head>
            <body>
                <h1 style="text-align: center;">Olá, a cotação do dia da ''' + nome +''' é:</h1>
                <ul class="list-group">
                    <li class="list-group-item">
                        A data: ''' + date + '''
                    </li>
                    <li class="list-group-item">
                        Abriu a: ''' + hour +  '''
                    </li>
                    <li class="list-group-item">
                        Valor mais alto: '''+ abriu +  '''
                    </li>
                    <li class="list-group-item">
                        Valor mais baixo: ''' + alta +  '''
                    </li>
                    <li class="list-group-item">
                        Fechou a: ''' + baixa +  '''
                    </li>
                    <li class="list-group-item">
                        Volume: ''' + fechou + '''
                    </li>     
            </body>
        </html>'''
                      )
        indice = indice + 1
        site.close()
    print("Todas as páginas HTML geradas, abra o index.html.")



#ESSA FUNÇÃO TEM DELAY POIS A API SÓ ACEITA 5 REQUISIÇOES POR MINUTO
bovespa_daily()

#ESSA FUNÇÃO TEM DELAY POIS A API SÓ ACEITA 5 REQUISIÇOES POR MINUTO
brcompanyinfo()
#FIM
