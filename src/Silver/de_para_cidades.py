import pandas as pd
from thefuzz import process

file_ibge = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Gold/IBGE Municípios.xlsx'

ibge = pd.read_excel(file_ibge)

ibge = ibge.loc[:, ['Id Município', 'Município', 'UF']]

ibge['Chave'] = ibge['Município'] + '-' + ibge['UF']

# XML CTE

def fazer_de_para_cte():

    file_cte = 'Data/Output/Silver/XML/dcidade.csv'
    
    cte = pd.read_csv(file_cte, encoding = 'latin1', decimal= ',')
    
    cte['Chave'] = cte['Cidade'] + '-' + cte['UF']
    
    # process.extract("new york jets", choices, limit=2)
    
    de_para_cte = pd.DataFrame()
    
    de_para_cte['De'] = cte['Chave']
    
    lista_score = []
    
    for cidade_cte in cte['Chave']:
        match = process.extractOne(cidade_cte, ibge['Chave'])
        lista_score.append(match)
    
    lista_cidade = list(zip(*lista_score))[0]
    lista_score = list(zip(*lista_score))[1]
    
    de_para_cte['Para'] = lista_cidade
    de_para_cte['Score'] = lista_score
    
    for index, row in de_para_cte.iterrows():
        if row['De'] == 'Exterior-EX':
            de_para_cte.at[index, 'Para'] = 'Exterior-EX'
    
    de_para_cte.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/De Para Cidades/de_para_cte.csv',
                       index=False, decimal=',', encoding='latin-1')
    
    return de_para_cte


# BEX SAP

def fazer_de_para_bex():

    file_cidade = 'Data/Output/Silver/BEX/dcidade.csv'
    
    bex = pd.read_csv(file_cidade, decimal=',', encoding='latin-1')
    
    bex['Chave'] = bex['Cidade'] + '-' + bex['UF']
    
    de_para_bex = pd.DataFrame()
    
    de_para_bex['De'] = bex['Chave']
    
    lista_score = []
    
    for cidade_bex in bex['Chave']:
        match = process.extractOne(cidade_bex, ibge['Chave'])
        lista_score.append(match)
    
    lista_cidade = list(zip(*lista_score))[0]
    lista_score = list(zip(*lista_score))[1]
    
    de_para_bex['Para'] = lista_cidade
    de_para_bex['Score'] = lista_score
    
    for index, row in de_para_bex.iterrows():
        if row['De'] == 'URUÇUI-PA':
            de_para_bex.at[index, 'Para'] = 'Uruçuí-PI'
        elif row['De'] == 'FORTALEZA DO TABOCAO-TO':
            de_para_bex.at[index, 'Para'] = 'Tabocão-TO'
            
    def splitar_cidade_uf(cidade_uf: str):
        
        splitar_cidade_uf = cidade_uf.rsplit('-', 1)
        
        return pd.Series(splitar_cidade_uf)
    
    de_para_bex[['De-Cidade', 'De-UF']] = de_para_bex['De'].apply(splitar_cidade_uf)
    de_para_bex[['Para-Cidade', 'Para-UF']] = de_para_bex['Para'].apply(splitar_cidade_uf)
    
    de_para_bex = de_para_bex.loc[:, ['De-Cidade', 'De-UF', 'Para-Cidade', 'Para-UF', 'Score']]
    
    de_para_bex.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/De Para Cidades/de_para_bex.csv',
                       index=False, decimal=',', encoding='latin-1')
    
    return de_para_bex
