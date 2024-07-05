import pandas as pd
import numpy as np


def formar_tabela_nota_fiscal():

    file_nf = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Nota Fiscal.xlsx'

    nf = pd.read_excel(file_nf)

    header = {
        'Contrato Venda SD': 'Contrato Venda',
        'Nº pedido do cliente' : 'Pedido SalesForce',
        'Tp.doc.faturamento': 'Tipo',
        'Fornecimento': 'Remessa',
        'Nº NF 9 posições': 'Nº NF',
        'Item Contr Venda SD': 'Item Contrato',
        'Ordem de vendas': 'OV',
        '\nValor': 'Valor',
        '\nQtd NF': 'Quantidade',
        '\nVlr COFINS (NF)': 'Cofins',
        '\nVlr ICMS (NF)': 'ICMS',
        '\nVlr PIS (NF)': 'PIS',
        '\nPeso Líquido NF': 'Peso KG',
        'Material' : 'Id Produto',
        'Unnamed: 17' : 'Produto',
        'Centro' : 'Id Centro',
        'Unnamed: 19' : 'Centro'  
    }

    nf.rename(columns=header, inplace=True)

    ordem_colunas = [
        'Contrato Venda',
        'Item Contrato',
        'Pedido SalesForce',
        'OV',
        'Item OV',
        'Data criação',
        'Hora da criação',
        'Tipo',
        'Código status NFe',
        'NF-e: Status Doc',
        'Id Centro',
        'Centro',
        'Remessa',
        'Item Rem',
        'Grupo de mercadorias',
        'Id Produto',
        'Produto',
        'Lote',
        'Incoterms',
        'Nº NF',
        'Chave de Acesso - NF',
        'Quantidade',
        'Valor',
        'Cofins',
        'ICMS',
        'PIS',
        'Peso KG'
    ]

    nf = nf.loc[:, ordem_colunas]

    nf.replace('#', np.nan, inplace=True)
    nf.replace('Não atribuído', np.nan, inplace=True)

    return nf
