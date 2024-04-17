import pandas as pd
from src.DataFrame.carteira_vendas import formar_tabela_dim

# Motivo de Recusas

colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']

motivo_recusa = formar_tabela_dim(colunas_uteis = colunas_mot_rec)

motivo_recusa.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dmotivo_recusa.csv', index = False, decimal = ',', encoding = 'latin-1')


# Centro

colunas_centro = ['Id Centro', 'Centro', 'CNPJ Centro']

centro = formar_tabela_dim(colunas_uteis = colunas_centro)

centro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcentro.csv', index = False, decimal = ',', encoding = 'latin-1')


# UF

colunas_uf_origem = ['Id UF Origem', 'UF Origem']

uf_origem = formar_tabela_dim(colunas_uteis = colunas_uf_origem)

trocar_nome_uf_origem = {
    'Id UF Origem' : 'Id UF',
    'UF Origem' : 'UF'
    }

uf_origem.rename(columns = trocar_nome_uf_origem, inplace = True)

colunas_uf_destino = ['Id UF Destino', 'UF Destino']

uf_destino = formar_tabela_dim(colunas_uteis = colunas_uf_destino)

trocar_nome_uf_destino = {
    'Id UF Destino' : 'Id UF',
    'UF Destino' : 'UF'
    }

uf_destino.rename(columns = trocar_nome_uf_destino, inplace = True)

uf = pd.concat([uf_origem, uf_destino], axis = 0)

uf.drop_duplicates(inplace = True)

uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/UF.csv', index = False, decimal = ',', encoding = 'latin-1')


# Cidade

colunas_origem = ['Origem', 'Id UF Origem']

origem = formar_tabela_dim(colunas_uteis = colunas_origem)

trocar_nome_origem = {
    'Origem' : 'Cidade',
    'Id UF Origem' : 'Id UF'
    }

origem.rename(columns = trocar_nome_origem, inplace = True)

colunas_destino = ['Destino', 'Id UF Destino']

destino = formar_tabela_dim(colunas_uteis = colunas_destino)

trocar_nome_destino = {
    'Destino' : 'Cidade',
    'Id UF Destino' : 'Id UF',
    }

destino.rename(columns = trocar_nome_destino, inplace = True)

cidade = pd.concat([origem, destino], axis = 0)

cidade.drop_duplicates(inplace = True)

cidade.reset_index(drop = True, inplace = True)

cidade.index = cidade.index + 1

cidade['Id Cidade'] = cidade.index

cidade = cidade.loc[:, ['Id Cidade', 'Cidade', 'Id UF']]

cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Cidade.csv', index = False, decimal = ',', encoding = 'latin-1')

# Zona de Transp

colunas_zt_origem = ['Zona Transp. Origem', 'Id UF Origem']

zt_origem = formar_tabela_dim(colunas_uteis = colunas_zt_origem)

trocar_nome_zt_origem = {
    'Zona Transp. Origem' : 'Zona de Transporte',
    'Id UF Origem' : 'Id UF'
    }

zt_origem.rename(columns = trocar_nome_zt_origem, inplace = True)

colunas_zt_destino = ['Zona Transp. Destino', 'Id UF Destino']

zt_destino = formar_tabela_dim(colunas_uteis = colunas_zt_destino)

trocar_nome_zt_destino = {
    'Zona Transp. Destino' : 'Zona de Transporte',
    'Id UF Destino' : 'Id UF'
    }

zt_destino.rename(columns = trocar_nome_zt_destino, inplace = True)

zt = pd.concat([zt_origem, zt_destino], axis = 0)

zt.drop_duplicates(inplace = True)

zt.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Zona de Transporte.csv', index = False, decimal = ',', encoding = 'latin-1')

# Local de Expedição

colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'CNPJ Local Exp.', 'Zona Transp. Origem']

local_exp = formar_tabela_dim(colunas_uteis = colunas_local_exp)

local_exp.rename(columns = {'Zona Transp. Origem' : 'Zona de Transporte'}, inplace = True)

local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Local de Expedição.csv', index = False, decimal = ',', encoding = 'latin-1')