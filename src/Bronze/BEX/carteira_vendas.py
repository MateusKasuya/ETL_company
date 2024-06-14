import pandas as pd
import numpy as np


def main_df():

    file_carteira = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Carteira Vendas.xlsx'

    df = pd.read_excel(file_carteira)

    header = {
        'Pedido do Cliente': 'Pedido SalesForce',
        'Centro': 'Id Centro',
        'Unnamed: 5': 'Centro',
        'CNPJ empresa/LocNeg.': 'CNPJ Centro',
        'Local Expedição': 'Id Local Exp.',
        'Unnamed: 8': 'Local Expedição',
        'Cidade': 'Origem',
        'Estado': 'UF Origem',
        'Unnamed: 11': 'Nome UF Origem',
        'Recebedor Mercadoria': 'Id Cliente',
        'Unnamed: 13': 'Cliente',
        'CNPJ  Raiz': 'CNPJ Raiz Cliente',
        'Estado.1': 'UF Destino',
        'Unnamed: 16': 'Nome UF Destino',
        'Cidade.1': 'Destino',
        'Material': 'Id Produto',
        'Unnamed: 23': 'Produto',
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
        'Inscr. Estadual (Cliente Recebedor)': 'Ins. Est. Cliente',
        'Inscrição Municipal': 'Ins. Mun. Cliente',
        'Itinerário': 'Id Itinerário',
        'Unnamed: 35': 'Itinerário',
        'Motivo de Recusa': 'Id Mot. Rec.',
        'Unnamed: 38': 'Motivo de Recusa',
        'Distância': 'Distância KM',
        'BP Parceiro (Loca  Expedição)': 'BP Local Expedição',
        'Data Criação OV/Fatura' : 'Data da OV',
        'Data de criação' : 'Data do Contrato',
        '\nPeso Liquido - Contrato' : 'Peso Liq. Contrato',
        '\nPeso Liquido - OV' : 'Peso Liq. OV'
    }

    df.rename(columns=header, inplace=True)

    ordem_colunas = [
        'Contrato Venda',
        'Item Contrato',
        'OV',
        'Item OV',
        'Pedido SalesForce',
        'Tipo Documento',
        'Data do Contrato',
        'Data da OV',
        'Data Início Entrega',
        'Data Fim Entrega',
        'Qtde Contrato',
        'Valor Contrato',
        'Peso Liq. Contrato',
        'Qtde OV',
        'Valor OV',
        'Peso Liq. OV',
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
        'UF Origem',
        'Nome UF Origem',
        'Origem',
        'Zona Transp. Origem',
        'Id Cliente',
        'Cliente',
        'CNPJ Raiz Cliente',
        'CNPJ Cliente',
        'CPF Cliente',
        'Ins. Est. Cliente',
        'UF Destino',
        'Nome UF Destino',
        'Destino',
        'Id Itinerário',
        'Itinerário',
        'Distância KM',
        'Incoterms',
        'Grupo de Mercadorias',
        'Id Produto',
        'Produto',
        'Unid. Produto',
        'NCM Produto',
        'Obs N. Fiscal (text)',
        'Obs Ped.Niv.Cab(txt)',
        'Rot Entrega (texto)'
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

    return tabela_dimensao
