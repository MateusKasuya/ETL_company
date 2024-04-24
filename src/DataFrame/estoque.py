import pandas as pd
import numpy as np

def main_estoque():

    file_estoque = 'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/Estoque.xlsx'
    
    estoque = pd.read_excel(file_estoque)
    
    header = {
                'Centro' : 'Id Centro',
                'Grupo de mercadorias' : 'Id Grupo Merc.',
                'Unnamed: 2' : 'Grupo de Mercadorias',
                'Material' : 'Id Produto',
                'Unnamed: 4' : 'Produto',
                'Cliente' : 'Id Cliente',
                '\nUtilização Livre' : 'Estoque Livre',
                '\n\nEstoque bloqueado' : 'Estoque Bloqueado',
                '\n\nQtd.estq.consignação' : 'Estoque Consignado'
        }
    
    estoque.rename(columns = header, inplace = True)
    
    ordem_colunas = [
                'Id Centro',
                'Id Grupo Merc.',
                'Grupo de Mercadorias',
                'Id Produto',
                'Produto',
                'Lote',
                'Data Vencimento',
                'Data Última EM',
                'Texto Cabeç Doc',
                'Id Cliente',
                'Estoque Livre',
                'Estoque Bloqueado',
                'Estoque Consignado'
        ]
    
    estoque = estoque.loc[:, ordem_colunas]
    
    estoque.replace('#', np.nan, inplace = True)

    return estoque

def formar_tabela_estoque(colunas_uteis):
    
    estoque = main_estoque()
    
    tabela_estoque = estoque.loc[:, colunas_uteis]
    
    tabela_estoque.drop_duplicates(inplace = True)
    
    tabela_estoque.dropna(subset = [tabela_estoque.columns[0]], inplace = True)
    
    tabela_estoque.index = tabela_estoque[colunas_uteis[0]]
    
    return tabela_estoque