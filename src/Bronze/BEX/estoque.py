import pandas as pd


def formar_tabela_estoque():

    file_estoque = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/BEX/Estoque.xlsx'

    estoque = pd.read_excel(file_estoque)

    header = {
        'Centro': 'Id Centro',
        'Unnamed: 1' : 'Centro',
        'Material': 'Id Produto',
        'Unnamed: 4': 'Produto',
        'Cliente': 'Id Cliente',
        'Unnamed: 9' : 'Cliente',
        '\nUtilização Livre': 'Estoque Livre',
        '\n\nEstoque bloqueado': 'Estoque Bloqueado',
        '\n\nQtd.estq.consignação': 'Estoque Consignado'
    }

    estoque.rename(columns=header, inplace=True)

    estoque.replace('#', None, inplace=True)
    
    estoque.drop_duplicates(inplace=True)

    return estoque
