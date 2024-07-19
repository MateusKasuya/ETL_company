import pandas as pd

def formar_gerencial_frete():

    file = 'Data/Input/BEX/Gerencial_Frete.xlsx'
    df = pd.read_excel(file)
    
    trocar_nome = {
        'Contrato Venda SD': 'Contrato Venda',
        'Item Contr Venda SD': 'Item Contrato',
        'Documento Vendas' : 'OV',
        'Item Documento Venda' : 'Item OV',
        'Classe Contas Orígeo': 'Classe Contas',
        '\nFreight - BRL': 'Frete',
        '\nVolume Receita': 'Volume Receita',
        '\nGross Sales Value - BRL': 'Gross Sales',
        '\nNet Sales Value - BRL': 'Net Sales'
    }
    df.rename(columns=trocar_nome, inplace=True)
    
    colunas_agrupadoras = ['Contrato Venda', 'Item Contrato', 'OV', 'Item OV', 'Data de lançamento',
                           'Data Compensação', 'Data Vencimento', 'Grupo de Mercadorias',
                           'Classe Contas', 'Documento Contábil', 'Item Doc Contábil', 'Incoterms',
                           ]
    df = df.groupby(by=colunas_agrupadoras, as_index=False, dropna=False).agg(
        {'Frete': 'sum', 'Volume Receita': 'sum', 'Gross Sales': 'sum', 'Net Sales': 'sum'})
    
    ordem_colunas = [
        'Contrato Venda',
        'Item Contrato',
        'OV',
        'Item OV',
        'Grupo de Mercadorias',
        'Incoterms',
        'Frete',
        'Volume Receita',
        'Gross Sales',
        'Net Sales',
        'Classe Contas',
        'Documento Contábil',
        'Item Doc Contábil',  
        'Data de lançamento',
        'Data Compensação',
        'Data Vencimento'      
        ]
    df = df.loc[:, ordem_colunas]
    
    df.replace('#', None, inplace=True)
    df.replace('Não atribuído', None, inplace=True)
    
    return df
