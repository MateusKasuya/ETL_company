import pandas as pd
import numpy as np


def main_dt():

    file_dt = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/DT.xlsx'

    dt = pd.read_excel(file_dt)

    header = {
        'Doc. Transporte': 'DT',
        'Agente de frete': 'Id Transportador',
        'Unnamed: 2': 'Transportador',
        'Tipo de transporte': 'Id Categoria',
        'Unnamed: 4': 'Categoria',
        'Fornecimento': 'Remessa',
        'Qtd Fornecida UMV': 'Quantidade',
        'Valor Frete Lote': 'Valor Frete Total',
        'Pes Bruto Ordem Vend': 'Peso KG'
    }

    dt.rename(columns=header, inplace=True)

    ordem_colunas = [
        'DT',
        'Remessa',
        'Item Rem',
        'Data de criação',
        'Quantidade',
        'Valor Frete Total',
        'Peso KG',
        'Item Superior',
        'Id Categoria',
        'Categoria',
        'Id Transportador',
        'Transportador'
    ]

    dt = dt.loc[:, ordem_colunas]

    dt.replace('#', np.nan, inplace=True)
    dt.replace('Não atribuído', np.nan, inplace=True)

    return dt


def formar_tabela_dt(colunas_uteis):

    dt = main_dt()

    tabela_dt = dt.loc[:, colunas_uteis]

    tabela_dt.drop_duplicates(inplace=True)

    tabela_dt.dropna(subset=[tabela_dt.columns[0]], inplace=True)

    return tabela_dt
