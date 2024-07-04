import pandas as pd

def formar_tabela_transf():

    file = 'Data/Input/BEX/Transferência.xlsx'
    
    df = pd.read_excel(file)
    
    df.drop(['Unnamed: 5', 'Unnamed: 9', 'Qtd Pedido'], axis = 1, inplace = True)
    
    trocar_nomes = {
        'Número do Pedido de compras' : 'Pedido Transf.',
        'Data do pedido/recebimento' : 'Data',
        'Centro Fornecedor' : 'Expedidor',
        'Cidade' : 'Origem',
        'Estado' : 'UF Origem',
        'Centro' : 'Recebedor',
        'Cidade.1' : 'Destino',
        'Estado.1' : 'UF Destino'
        }
    
    df.rename(columns = trocar_nomes, inplace = True)
    
    return df