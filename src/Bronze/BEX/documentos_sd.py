import pandas as pd
import numpy as np


def main_df():

    file_sd_23 = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Documentos SD 23.xlsx'
    file_sd_24 = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Documentos SD 24.xlsx'

    df_23 = pd.read_excel(file_sd_23)
    df_24 = pd.read_excel(file_sd_24)
      
    df = pd.concat([df_23, df_24], axis = 0)

    header = {
        'Nº pedido do cliente': 'Pedido SalesForce',
        'Centro': 'Id Centro',
        'Unnamed: 5': 'Centro',
        'Rua' : 'Endereço Centro',
        'CNPJ empresa/LocNeg.': 'CNPJ Centro',
        'Local de Expedição': 'Id Local Exp.',
        'Unnamed: 9': 'Local Expedição',
        'Cidade': 'Origem',
        'Estado': 'UF Origem',
        'Unnamed: 12': 'Nome UF Origem',
        'Recebedor Mercadoria': 'Id Cliente',
        'Unnamed: 14': 'Cliente',
        'CNPJ  Raiz': 'CNPJ Raiz Cliente',
        'Estado.1': 'UF Destino',
        'Unnamed: 17': 'Nome UF Destino',
        'Cidade.1': 'Destino',
        'Material': 'Id Produto',
        'Unnamed: 24': 'Produto',
        'UM básica': 'Unid. Produto',
        'Moeda Documento' : 'Moeda',
        'Item Contr Venda SD': 'Item Contrato',
        'CNPJ (Local Expedição)': 'CNPJ Local Exp.',
        'Código de Controle': 'NCM Produto',
        'Data Entrega': 'Data Fim Entrega',
        'Data Retirada': 'Data Início Entrega',
        'Tipo Doc. Venda': 'Tipo Documento',
        'Contrato - Qtde': 'Qtde Contrato',
        'Contrato - $ Valor': 'Valor Contrato',
        'Documento de vendas': 'OV',
        'Item Doc Vendas': 'Item OV',
        'OV - Qtde': 'Qtde OV',
        'OV - $ Valor': 'Valor OV',
        'CNPJ (Cliente)': 'CNPJ Cliente',
        'CPF (Cliente)': 'CPF Cliente',
        'Inscrição Estadual (Cliente)': 'Ins. Est. Cliente',
        'Inscrição Municipal': 'Ins. Mun. Cliente',
        'Itinerário': 'Id Itinerário',
        'Unnamed: 36': 'Itinerário',
        'Motivo de Recusa': 'Id Mot. Rec.',
        'Unnamed: 39': 'Motivo de Recusa',
        'Distância': 'Distância KM',
        'BP Parceiro (Loca  Expedição)': 'BP Local Expedição',
        'Data de Criação' : 'Data da OV',
        'Data de criação' : 'Data do Contrato',
        'Contrato - Peso Líquido' : 'Peso Liq. Contrato',
        'OV - Peso Líquido' : 'Peso Liq. OV',
        'Ctg. Doc. SD' : 'Categoria Documento',
        'Contrato Venda SD' : 'Contrato Venda'
    }

    df.rename(columns=header, inplace=True)

    ordem_colunas = [
        'Contrato Venda',
        'Item Contrato',
        'OV',
        'Item OV',
        'Pedido SalesForce',
        'Categoria Documento',
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
        'Requisição Compra',
        'Id Centro',
        'Centro',
        'CNPJ Centro',
        'Endereço Centro',
        'Id Local Exp.',
        'Local Expedição',
        'BP Local Expedição',
        'CNPJ Local Exp.',
        'UF Origem',
        'Nome UF Origem',
        'Origem',
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
