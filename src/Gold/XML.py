import pandas as pd
import numpy as np


def formar_tabela_cidade_cte_gold():

    file_cidade_xml = 'Data/Output/Silver/XML/dcidade.csv'
    file_ibge = 'Data/Output/Silver/De Para Cidades/de_para_cte.csv'

    cidade_xml = pd.read_csv(file_cidade_xml, encoding='latin-1', decimal=',')
    cidade_ibge = pd.read_csv(file_ibge, encoding='latin-1', decimal=',')

    cidade_xml = cidade_xml.merge(cidade_ibge, left_on=['Cidade', 'UF'], right_on=[
                                  'De-Cidade', 'De-UF'], how='left')

    cidade_xml = cidade_xml.loc[:, ['Cidade', 'UF', 'Para-Cidade']]

    cidade_xml.rename(columns={'Para-Cidade': 'Cidade IBGE'}, inplace=True)

    cidade_xml.to_excel('Data/Output/Gold/Municípios CTE.xlsx',
                        index=False)

    return cidade_xml


def formar_tabela_cte_gold():

    file_cte = 'Data/Output/Silver/XML/fCTE.csv'
    file_cidade = 'Data/Output/Gold/Municípios CTE.xlsx'

    cte = pd.read_csv(file_cte, encoding='latin-1', decimal=',')
    cidade = pd.read_excel(file_cidade)

    cte = cte.merge(cidade, left_on=['Origem Expedidor', 'UF Origem Expedidor'], right_on=[
                    'Cidade', 'UF'], how='left')
    cte.drop(['Origem Expedidor', 'UF', 'Cidade'], axis=1, inplace=True)
    cte.rename(columns={'Cidade IBGE': 'Origem Expedidor'}, inplace=True)

    cte = cte.merge(cidade, left_on=['Origem Remetente', 'UF Origem Remetente'], right_on=[
                    'Cidade', 'UF'], how='left')
    cte.drop(['Origem Remetente', 'UF', 'Cidade'], axis=1, inplace=True)
    cte.rename(columns={'Cidade IBGE': 'Origem Remetente'}, inplace=True)

    cte = cte.merge(cidade, left_on=['Destino Recebedor', 'UF Destino Recebedor'], right_on=[
                    'Cidade', 'UF'], how='left')
    cte.drop(['Destino Recebedor', 'UF', 'Cidade'], axis=1, inplace=True)
    cte.rename(columns={'Cidade IBGE': 'Destino Recebedor'}, inplace=True)

    cte = cte.merge(cidade, left_on=['Destino Destinatário', 'UF Destino Destinatário'], right_on=[
                    'Cidade', 'UF'], how='left')
    cte.drop(['Destino Destinatário', 'UF', 'Cidade'], axis=1, inplace=True)
    cte.rename(columns={'Cidade IBGE': 'Destino Destinatário'}, inplace=True)
    
    cte = cte[~cte['XML'].isna()]
    
    list_grupo_merc = []
    
    for i in cte['Produto']:
        if isinstance(i, str):
            if "KCL" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "SHENZI" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "00" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "FERTILIZANTE" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "LT" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "ADUBO" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "AGR" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "CLORETO" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "FOSFATO" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "MAMONA" in i:
                list_grupo_merc.append('Sementes - Outros')
            elif "MAP" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "X" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "PRIMOLEO" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "QUIMICOS" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "SAM" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "SEMENTE" in i:
                list_grupo_merc.append('Sementes - Outros')
            elif "SSP" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "SUBSTANCIA" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "SULFATO" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            elif "TRUNFO" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "UNIZEB" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "UPL" in i:
                list_grupo_merc.append('Defensor Agri Outros')
            elif "UREIA" in i:
                list_grupo_merc.append('Fertilizantes Outros')
            else:
                list_grupo_merc.append('Outros')
        else:
            list_grupo_merc.append('Outros')
            
    cte['Grupo de Mercadorias'] = list_grupo_merc
    
    dict_tipo_cte = {
        0 : 'Normal',
        1 : 'Complementar',
        3 : 'Substituição'
        }
    
    cte['Tipo CTE'] = cte['Tipo CTE'].map(dict_tipo_cte)
    
    cte = cte.loc[:, ['XML', 'Expedidor', 'Origem Expedidor', 'UF Origem Expedidor', 'Remetente',
                      'UF Origem Remetente', 'Origem Remetente', 'Recebedor', 'Destino Recebedor', 'UF Destino Recebedor',
                      'Destinatário', 'Destino Destinatário', 'UF Destino Destinatário', 'Transportadora', 'Data',
                      'Chave NF', 'NF', 'CTE', 'Peso Volume', 'Valor Frete Total', 'Produto','Grupo de Mercadorias',
                      'Tipo CTE']]
            
    cte.to_excel('Data/Output/Gold/CTE.xlsx', index=False)

    return cte
