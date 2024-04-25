import pandas as pd
import numpy as np


def main_df():

    file_carteira = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/Carteira Vendas.xlsx'

    df = pd.read_excel(file_carteira)

    header = {
        'Nº pedido do cliente': 'Pedido SalesForce',
        'Centro': 'Id Centro',
        'Unnamed: 5': 'Centro',
        'CNPJ empresa/LocNeg.': 'CNPJ Centro',
        'Local Expedição': 'Id Local Exp.',
        'Unnamed: 8': 'Local Expedição',
        'Cidade': 'Origem',
        'Estado': 'Id UF Origem',
        'Unnamed: 11': 'UF Origem',
        'Recebedor Mercadoria': 'Id Cliente',
        'Unnamed: 13': 'Cliente',
        'CNPJ  Raiz': 'CNPJ Raiz Cliente',
        'Estado.1': 'Id UF Destino',
        'Unnamed: 16': 'UF Destino',
        'Cidade.1': 'Destino',
        'Material': 'Id Produto',
        'Unnamed: 24': 'Produto',
        'UM básica': 'Unid. Produto',
        'Item Contr Venda': 'Item Contrato',
        'CNPJ (Local Expedição)': 'CNPJ Local Exp.',
        'Código de controle': 'NCM Produto',
        'Data Entrega': 'Data Fim Entrega',
        'Data Retirada': 'Data Início Entrega',
        'Tipo Doc. Venda': 'Tipo Documento',
        'Zona Transp (Local Expedição)': 'Zona Transp. Origem',
        'Zona Transp. (Cliente Recebedor)': 'Zona Transp. Destino',
        '\nQtde Contrato': 'Qtde Contrato',
        '\n$ Valor Contrato': 'Valor Contrato',
        'Documento Vendas': 'OV',
        'Item Doc Vendas': 'Item OV',
        '\nQtde OV': 'Qtde OV',
        '\n$ Valor OV': 'Valor OV',
        'CNPJ (Cliente)': 'CNPJ Cliente',
        'CPF (Cliente)': 'CPF Cliente',
        'Inscrição Estadual (Cliente)': 'Ins. Est. Cliente',
        'Inscrição Municipal': 'Ins. Mun. Cliente',
        'Grupo de Mercadorias': 'Id Grupo Merc.',
        'Unnamed: 22': 'Grupo de Mercadorias',
        'Itinerário': 'Id Itinerário',
        'Unnamed: 37': 'Itinerário',
        'Motivo de Recusa': 'Id Mot. Rec.',
        'Unnamed: 40': 'Motivo de Recusa',
        'Distância': 'Distância KM',
        'BP Parceiro (Loca  Expedição)': 'BP Local Expedição'
    }

    df.rename(columns=header, inplace=True)

    ordem_colunas = [
        'Contrato Venda',
        'Item Contrato',
        'OV',
        'Item OV',
        'Pedido SalesForce',
        'Tipo Documento',
        'Data de criação',
        'Data Início Entrega',
        'Data Fim Entrega',
        'Qtde Contrato',
        'Valor Contrato',
        'Qtde OV',
        'Valor OV',
        'Moeda',
        'Id Mot. Rec.',
        'Motivo de Recusa',
        'Requisição de compra',
        'Id Centro',
        'Centro',
        'CNPJ Centro',
        'Id Local Exp.',
        'Local Expedição',
        'BP Local Expedição',
        'CNPJ Local Exp.',
        'Id UF Origem',
        'UF Origem',
        'Origem',
        'Zona Transp. Origem',
        'Id Cliente',
        'Cliente',
        'CNPJ Raiz Cliente',
        'CNPJ Cliente',
        'CPF Cliente',
        'Ins. Est. Cliente',
        'Ins. Mun. Cliente',
        'Id UF Destino',
        'UF Destino',
        'Destino',
        'Zona Transp. Destino',
        'Id Itinerário',
        'Itinerário',
        'Distância KM',
        'Incoterms',
        'Id Grupo Merc.',
        'Grupo de Mercadorias',
        'Id Produto',
        'Produto',
        'Unid. Produto',
        'NCM Produto'
    ]

    df = df.loc[:, ordem_colunas]

    df.replace('#', np.nan, inplace=True)
    df.replace('Não atribuído', np.nan, inplace=True)

    return df


def formar_tabela_dim(colunas_uteis):

    df = main_df()

    tabela_dimensao = df.loc[:, colunas_uteis]

    tabela_dimensao.drop_duplicates(inplace=True)

    tabela_dimensao.dropna(subset=[tabela_dimensao.columns[0]], inplace=True)

    tabela_dimensao.index = tabela_dimensao[colunas_uteis[0]]

    return tabela_dimensao
