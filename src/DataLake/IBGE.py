import requests
import pandas as pd

# Município


def municipio():

    url_municipio = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

    request_municipio = requests.get(url_municipio)

    lista_mun = request_municipio.json()

    municipio = pd.DataFrame()

    municipio['Id'] = [i['id'] for i in lista_mun]

    municipio['Município'] = [i['nome'] for i in lista_mun]

    municipio['Id Microrregião'] = [i['microrregiao']['id'] for i in lista_mun]
    
    municipio.index = municipio['Id']

    municipio.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/IBGE/dmunicipio.csv',
                     index=False, decimal=',', encoding='latin-1')

    return municipio

# Microrregião


def microrregiao():

    url_micro = 'https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes'

    request_micro = requests.get(url_micro)

    lista_micro = request_micro.json()

    micro = pd.DataFrame()

    micro['Id'] = [i['id'] for i in lista_micro]

    micro['Microrregião'] = [i['nome'] for i in lista_micro]

    micro['Id Mesorregião'] = [i['mesorregiao']['id'] for i in lista_micro]
    
    micro.index = micro['Id']

    micro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/IBGE/dmicrorregiao.csv',
                 index=False, decimal=',', encoding='latin-1')

    return micro
# Mesorregião


def mesorregiao():

    url_meso = 'https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes'

    request_meso = requests.get(url_meso)

    lista_meso = request_meso.json()

    meso = pd.DataFrame()

    meso['Id'] = [i['id'] for i in lista_meso]

    meso['Mesorregião'] = [i['nome'] for i in lista_meso]

    meso['Id UF'] = [i['UF']['id'] for i in lista_meso]
    
    meso.index = meso['Id']

    meso.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/IBGE/dmesorregiao.csv',
                index=False, decimal=',', encoding='latin-1')

    return meso

# UF


def uf():

    url_uf = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

    request_uf = requests.get(url_uf)

    lista_uf = request_uf.json()

    uf = pd.DataFrame()

    uf['Id'] = [i['id'] for i in lista_uf]

    uf['UF'] = [i['nome'] for i in lista_uf]

    uf['Id Regiao'] = [i['regiao']['id'] for i in lista_uf]
    
    uf.index = uf['Id']

    uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/IBGE/dUF.csv',
              index=False, decimal=',', encoding='latin-1')

    return uf

# Região


def regiao():

    url_reg = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes'

    request_reg = requests.get(url_reg)

    lista_reg = request_reg.json()

    regiao = pd.DataFrame()

    regiao['Id'] = [i['id'] for i in lista_reg]

    regiao['Região'] = [i['nome'] for i in lista_reg]
    
    regiao.index = regiao['Id']

    regiao.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/IBGE/dregiao.csv',
                  index=False, decimal=',', encoding='latin-1')

    return regiao
