import pandas as pd


def formar_tabela_conta_frete():

    file_conta_frete = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Conta Frete.xlsx'

    conta_frete = pd.read_excel(file_conta_frete)

    header = {
        'Contrato Venda SD': 'Contrato Venda',
        'Item Contr Venda SD': 'Item Contrato',
        'Frete Provisionado': 'Valor Frete Pedido'
    }

    conta_frete.rename(columns=header, inplace=True)
    
    conta_frete.replace('#', None, inplace=True)

    return conta_frete
