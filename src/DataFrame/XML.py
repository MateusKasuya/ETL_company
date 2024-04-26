from bs4 import BeautifulSoup
import os
import pandas as pd

# Diretório

path = r'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/ETL/Bases/XML/abr24'

file_list = os.listdir(path)

# Funções

def appendar_xml_lista(tag = str):

    lista_xml = []
    
    for file in file_list:
        
        file_path = os.path.join(path, file)
        
        with open(file_path, encoding='utf-8') as f:
            
            data = f.read()
           
            soup = BeautifulSoup(data, 'xml')
            
            var = soup.find_all(tag)
            
            lista_xml.append(var)
            
    return lista_xml

def splitar_lista_xml(lista_xml):
            
    lista_xml = str(lista_xml)
    
    lista_xml = lista_xml.split('], [')
    
    return lista_xml

def nested_tag(lista_xml, nest_tag = str):

    lista_xml_conteudo = []
    
    for xml in lista_xml:
        
        if xml:
            
            for conteudo in xml:
                
                sub_conteudo = conteudo.find_all(nest_tag)
                
                lista_xml_conteudo.append(sub_conteudo)
        
        else:
            
            lista_xml_conteudo.append([])

    return lista_xml_conteudo

def tratar_nested_tag(lista_xml_conteudo, nest_tag = str):

    lista_xml_conteudo = str(lista_xml_conteudo)
    
    lista_xml_conteudo = lista_xml_conteudo.split('], [')
    
    lista_xml_conteudo = [i.replace(nest_tag,'') for i in lista_xml_conteudo]
    
    lista_xml_conteudo = [i.replace('<','') for i in lista_xml_conteudo]
    
    lista_xml_conteudo = [i.replace('>','') for i in lista_xml_conteudo]
    
    lista_xml_conteudo = [i.replace('/','') for i in lista_xml_conteudo]
    
    lista_xml_conteudo = [i.replace('[','') for i in lista_xml_conteudo]
    
    lista_xml_conteudo = [i.replace(']','') for i in lista_xml_conteudo]
       
    return lista_xml_conteudo

# Separando CTE de NFE

separar_cte = appendar_xml_lista('CTe')

splitar_cte = splitar_lista_xml(separar_cte)

lista_zip = list(zip(file_list, splitar_cte))

lista_zip = [(fl, sc) for fl, sc in lista_zip if len(sc) > 0]

file_list, splitar_cte = zip(*lista_zip)

# Criando DataFrame

cte = pd.DataFrame()

# XML

cte['XML'] = file_list

# Expedidor

expedidor = appendar_xml_lista('exped')

nome_expedidor = nested_tag(expedidor, 'xNome')

nome_expedidor_tratado = tratar_nested_tag(nome_expedidor, 'xNome')

cte['Expedidor'] = nome_expedidor_tratado

cte['Expedidor'] = cte['Expedidor'].str.title()
            
# Origem

origem = nested_tag(expedidor, 'xMun')

origem_tratado = tratar_nested_tag(origem, 'xMun')

cte['Origem'] = origem_tratado

cte['Origem'] = cte['Origem'].str.title()

# UF Origem

uf_origem = nested_tag(expedidor, 'UF')

uf_origem_tratado = tratar_nested_tag(uf_origem, 'UF')

cte['UF Origem'] = uf_origem_tratado

cte['UF Origem'] = cte['UF Origem'].str.upper()

# Recebedor

recebedor = appendar_xml_lista('receb')

nome_recebedor = nested_tag(recebedor, 'xNome')

nome_recebedor_tratado = tratar_nested_tag(nome_recebedor, 'xNome')

cte['Recebedor'] = nome_recebedor_tratado

cte['Recebedor'] = cte['Recebedor'].str.title()
            
# Destino

destino = nested_tag(recebedor, 'xMun')

destino_tratado = tratar_nested_tag(destino, 'xMun')

cte['Destino'] = destino_tratado

cte['Destino'] = cte['Destino'].str.title()

# UF Destino

uf_destino = nested_tag(recebedor, 'UF')

uf_destino_tratado = tratar_nested_tag(uf_destino, 'UF')

cte['UF Destino'] = uf_destino_tratado

cte['UF Destino'] = cte['UF Destino'].str.upper()

# Transportadora

emissor = appendar_xml_lista('emit')

transportadora = nested_tag(emissor, 'xNome')

transportadora_tratado = tratar_nested_tag(transportadora, 'xNome')

cte['Transportadora'] = transportadora_tratado

cte['Transportadora'] = cte['Transportadora'].str.title()


# Data Emissão
lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('dhEmi')
        lista.append(var)
lista = str(lista)
lista = lista.split('</dhEmi>], [<dhEmi>')
lista = [i.replace('[[<dhEmi>','') for i in lista]
lista = [i.replace('</dhEmi>]]','') for i in lista]
df['Data Hora Emissão'] = lista
df['Data Hora Emissão'] = [i.split('T') for i in df['Data Hora Emissão']]
df['Data Hora Emissão'] = [i[0] for i in df['Data Hora Emissão']]
df['Data Hora Emissão'] = pd.to_datetime(df['Data Hora Emissão'])
df['Data Hora Emissão'] = df['Data Hora Emissão'].dt.strftime('%d/%m/%Y')
# Chave NF

lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('chave')
        lista.append(var)
lista = str(lista)
lista = lista.split('</chave>], [<chave>')
lista = [i.replace('[[<chave>','') for i in lista]
lista = [i.replace('</chave>]]','') for i in lista]
df['Chave NF'] = lista

# NF

df['NF'] = [i[29:34] if i[28:34][0] == '0' else i[28:34] for i in df['Chave NF']]
df['NF'] = df['NF'].str.lstrip('0')

# CTE

lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('nCT')
        lista.append(var)
lista = str(lista)
lista = lista.split('</nCT>], [<nCT>')
lista = [i.replace('[[<nCT>','') for i in lista]
lista = [i.replace('</nCT>]]','') for i in lista]
df['CTE'] = lista

# Peso Volume
lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('qCarga')
        lista.append(var)
lista = str(lista)
lista = lista.split('</qCarga>], [<qCarga>')
lista = [i.replace('<qCarga>','') for i in lista]
lista = [i.replace('</qCarga>','') for i in lista]
lista = [i.replace('[','') for i in lista]
lista = [i.replace(']','') for i in lista]
lista = [i.split(', ') for i in lista]
lista = [[float(j) for j in i] for i in lista]
lista = [sorted(i) for i in lista]
lista = [i[-1] if len(i) > 1 else i[0] for i in lista]
df['Peso Volume'] = lista
# Valor Frete
lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('vRec')
        lista.append(var)
lista = str(lista)
lista = lista.split('</vRec>], [<vRec>')
lista = [i.replace('[[<vRec>','') for i in lista]
lista = [i.replace('</vRec>]]','') for i in lista]
df['Valor Frete'] = lista
# Produto
lista = []
for file in file_list:
    file_path = os.path.join(path, file)
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'xml')
        var = soup.find_all('proPred')
        lista.append(var)
lista = str(lista)
lista = lista.split('</proPred>], [<proPred>')
lista = [i.replace('[[<proPred>','') for i in lista]
lista = [i.replace('</proPred>]]','') for i in lista]
df['Produto'] = lista
df['Produto'] = df['Produto'].str.title()

# Placa
# lista = []
# for file in file_list:
#     file_path = os.path.join(path, file)
#     with open(file_path, encoding='utf-8') as f:
#         data = f.read()
#         soup = BeautifulSoup(data, 'xml')
#         var = soup.find_all('xObs')
#         lista.append(var)
# lista = str(lista)
# lista = lista.split('], [')
# # lista = [i.replace('[','') for i in lista]
# # lista = [i.replace('</xObs>]]','') for i in lista]
# lista = [i.upper() for i in lista]
# lista = [i.split('PLACA')[1].strip() if len(i.split('PLACA')) > 1 else i for i in lista]
# df['Placa'] = lista
# df['Placa'] = df['Placa'].str.title()

# df['Flag Dest'] = [True if 'Origeo' in i else False for i in df['Destinatário']]
# df = df[df['Flag Dest'] == False]
# df = df.drop(['Flag Dest'], axis = 1)

list_prod = []
for i in df['Produto']:
    if 'Fertilizante' in i:
        z = True
        list_prod.append(z)
    elif 'Map' in i:
        z = True
        list_prod.append(z)
    elif 'Adubo' in i:
        z = True
        list_prod.append(z)
    elif 'Sam' in i:
        z = True
        list_prod.append(z)
    elif 'Fosfato' in i:
        z = True
        list_prod.append(z)
    elif 'Formulado' in i:
        z = True
        list_prod.append(z)
    elif 'Kcl' in i:
        z = True
        list_prod.append(z)
    elif 'Nk' in i:
        z = True
        list_prod.append(z)
    elif 'Nps' in i:
        z = True
        list_prod.append(z)
    elif 'Ssp' in i:
        z = True
        list_prod.append(z)
    elif 'Tsp' in i:
        z = True
        list_prod.append(z)
    elif 'Ureia' in i:
        z = True
        list_prod.append(z)
    elif 'Shenzi' in i:
        z = False
        list_prod.append(z)
    elif '00' in i:
        z = True
        list_prod.append(z)
    elif 'Sulfato' in i:
        z = True
        list_prod.append(z)
    elif 'Cloreto' in i:
        z = True
        list_prod.append(z)
    else:
        z = False
        list_prod.append(z)
df['Flag Prod'] = list_prod
df_prod = df[df['Flag Prod'] == False]
print(df_prod['Produto'].unique())
df = df[df['Flag Prod'] == True]
print(df['Produto'].unique())
df = df.drop(['Flag Prod'], axis = 1)

df = df[df['UF Recebedor'] != 'EX']

df['Peso Volume'] = [i / 1000 if len(str(i)) >= 5 else i for i in df['Peso Volume']]

df['Valor Frete'] = df['Valor Frete'].astype(float)
df['Frete Unit'] = df['Valor Frete'] / df['Peso Volume']

df['Data Hora Emissão'] = pd.to_datetime(df['Data Hora Emissão'], format = '%d/%m/%Y')

locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
df['Mês'] = df['Data Hora Emissão'].dt.strftime('%B').str.lower()
df['Mês'] = [i[:3] for i in df['Mês']]
df['Ano'] = df['Data Hora Emissão'].dt.strftime('%y')
df['Mês'] = df['Mês'] + '/' + df['Ano']
df['Semana'] = df['Data Hora Emissão'].dt.strftime('%W')

df = df[[
    'Doc',
    'Natureza Operação',
    'Expedidor',
    'Município Expedidor',
    'UF Expedidor',
    'Recebedor',
    'Município Recebedor',
    'UF Recebedor',
    'Transportadora',
    'Data Hora Emissão',
    'Mês',
    'Semana',
    'Chave NF',
    'NF',
    'CTE',
    'Peso Volume',
    'Valor Frete',
    'Frete Unit',
    'Produto'
    ]]

df = df.rename(columns = {'Município Expedidor' : 'Origem',
                          'UF Expedidor' : 'UF Origem',
                          'Município Recebedor' : 'Destino',
                          'UF Recebedor' : 'UF Destino'})

df_jan = pd.read_excel(file_cte_jan24)
df_fev = pd.read_excel(file_cte_fev24)
df_mar = pd.read_excel(file_cte_mar24)

df = pd.concat([df, df_jan, df_fev, df_mar], axis = 0)

df.to_excel(r'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Fertilizantes/CTE_Fertilizantes.xlsx', index = False)
