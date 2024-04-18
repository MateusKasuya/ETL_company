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

uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dUF.csv', index = False, decimal = ',', encoding = 'latin-1')


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

cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcidade.csv', index = False, decimal = ',', encoding = 'latin-1')


# Local de Expedição

colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'CNPJ Local Exp.', 'Id UF Origem', 'Origem', 'Zona Transp. Origem',]

local_exp = formar_tabela_dim(colunas_uteis = colunas_local_exp)

trocar_local_exp = {
    'Id UF Origem' : 'Id UF',
    'Origem' : 'Cidade',
    'Zona Transp. Origem' : 'Zona de Transporte'
    }

local_exp.rename(columns = trocar_local_exp, inplace = True)

local_exp = local_exp.merge(cidade, on = ['Cidade', 'Id UF'], how = 'left')

local_exp.drop(['Cidade'], axis = 1, inplace = True)

local_exp = local_exp.loc[:, ['Id Local Exp.', 'Local Expedição', 'CNPJ Local Exp.', 'Id UF', 'Id Cidade', 'Zona de Transporte']]

local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dlocal_expedição.csv', index = False, decimal = ',', encoding = 'latin-1')


# Cliente

colunas_clientes = ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente', 'CNPJ Cliente', 'CPF Cliente', 'Ins. Est. Cliente', 'Ins. Mun. Cliente', 'Id UF Destino', 'Destino', 'Zona Transp. Destino']

cliente = formar_tabela_dim(colunas_uteis = colunas_clientes)

trocar_cliente = {
    'Id UF Destino' : 'Id UF',
    'Destino' : 'Cidade',
    'Zona Transp. Destino' : 'Zona de Transporte'
    }

cliente.rename(columns = trocar_cliente, inplace = True)

cliente = cliente.merge(cidade, on = ['Cidade', 'Id UF'], how = 'left')

cliente.drop(['Cidade'], axis = 1, inplace = True)

cliente = cliente.loc[:, ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente', 'CNPJ Cliente','CPF Cliente', 'Ins. Est. Cliente', 'Ins. Mun. Cliente', 'Id UF', 'Id Cidade', 'Zona de Transporte']]

cliente.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcliente.csv', index = False, decimal = ',', encoding = 'latin-1')
