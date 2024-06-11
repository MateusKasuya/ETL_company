import pandas as pd

def consolidar_cidades_IBGE():

    path = 'C:\\Users\\O1000246\\BUNGE\\Dados Supply Origeo - Documentos\\Projeto_Dados\\Data\\Output\\Silver\\IBGE'
    
    mun = pd.read_csv(path+'\\dmunicipio.csv', decimal=',', encoding='latin-1')
    micro = pd.read_csv(path+'\\dmicrorregiao.csv',
                        decimal=',', encoding='latin-1')
    meso = pd.read_csv(path+'\\dmesorregiao.csv', decimal=',', encoding='latin-1')
    uf = pd.read_csv(path+'\\dUF.csv', decimal=',', encoding='latin-1')
    
    
    ibge = mun.merge(micro, left_on='Id Microrregião', right_on='Id', how='inner')
    
    ibge = ibge.merge(meso, left_on='Id Mesorregião', right_on='Id', how='inner')
    
    ibge.rename(columns={'Id_x': 'Id Município'}, inplace=True)
    
    ibge = ibge.loc[:, ['Id Município', 'Município',
                        'Microrregião', 'Mesorregião', 'Id UF']]
    
    ibge = ibge.merge(uf, left_on='Id UF', right_on='Id', how='inner')
    
    ibge = ibge.loc[:, ['Id Município', 'Município',
                        'Microrregião', 'Mesorregião', 'UF']]
    
    ufs_brasil = {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins': 'TO'
    }
    
    ibge['UF'] = ibge['UF'].map(ufs_brasil)
    
    ibge.to_excel('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Gold/IBGE Municípios.xlsx',
                  index=False)
    
    return ibge
