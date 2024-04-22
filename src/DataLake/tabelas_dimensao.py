import pandas as pd
from src.DataFrame.carteira_vendas import formar_tabela_dim
from src.DataFrame.nota_fiscal import nota_fiscal

# Motivo de Recusas

colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']

motivo_recusa = formar_tabela_dim(colunas_uteis = colunas_mot_rec)

trocar_mot_rec = {'Id Mot. Rec.' : 'Id'}

motivo_recusa.rename(columns = trocar_mot_rec, inplace = True)

motivo_recusa.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dmotivo_recusa.csv', index = False, decimal = ',', encoding = 'latin-1')


# Centro

colunas_centro = ['Id Centro', 'Centro', 'CNPJ Centro']

centro = formar_tabela_dim(colunas_uteis = colunas_centro)

trocar_centro = {
    'Id Centro' : 'Id',
    'CNPJ Centro' : 'CNPJ'
    }

centro.rename(columns = trocar_centro, inplace = True)

centro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcentro.csv', index = False, decimal = ',', encoding = 'latin-1')


# UF

colunas_uf_origem = ['Id UF Origem', 'UF Origem']

uf_origem = formar_tabela_dim(colunas_uteis = colunas_uf_origem)

trocar_nome_uf_origem = {
    'Id UF Origem' : 'Id',
    'UF Origem' : 'UF'
    }

uf_origem.rename(columns = trocar_nome_uf_origem, inplace = True)

colunas_uf_destino = ['Id UF Destino', 'UF Destino']

uf_destino = formar_tabela_dim(colunas_uteis = colunas_uf_destino)

trocar_nome_uf_destino = {
    'Id UF Destino' : 'Id',
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

cidade['Id'] = cidade.index

cidade = cidade.loc[:, ['Id', 'Cidade', 'Id UF']]

cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcidade.csv', index = False, decimal = ',', encoding = 'latin-1')


# Local de Expedição

colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'CNPJ Local Exp.', 'Id UF Origem', 'Origem', 'Zona Transp. Origem',]

local_exp = formar_tabela_dim(colunas_uteis = colunas_local_exp)

local_exp = local_exp.merge(cidade, left_on = ['Origem', 'Id UF Origem'], right_on = ['Cidade', 'Id UF'], how = 'left')

local_exp = local_exp.loc[:, ['Id Local Exp.', 'Local Expedição', 'CNPJ Local Exp.', 'Id UF Origem', 'Id', 'Zona Transp. Origem']]

trocar_local_exp = {
    'Id UF Origem' : 'Id UF',
    'Zona Transp. Origem' : 'Zona de Transporte',
    'CNPJ Local Exp.' : 'CNPJ',
    'Id' : 'Id Cidade',
    'Id Local Exp.' : 'Id'
    }

local_exp.rename(columns = trocar_local_exp, inplace = True)

local_exp.index = local_exp['Id']

local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dlocal_expedição.csv', index = False, decimal = ',', encoding = 'latin-1')


# Cliente

colunas_clientes = ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente', 'CNPJ Cliente', 'CPF Cliente', 'Ins. Est. Cliente', 'Ins. Mun. Cliente', 'Id UF Destino', 'Destino', 'Zona Transp. Destino']

cliente = formar_tabela_dim(colunas_uteis = colunas_clientes)

cliente = cliente.merge(cidade, left_on = ['Destino', 'Id UF Destino'], right_on = ['Cidade', 'Id UF'], how = 'left')

cliente = cliente.loc[:, ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente', 'CNPJ Cliente','CPF Cliente', 'Ins. Est. Cliente', 'Ins. Mun. Cliente', 'Id UF Destino', 'Id', 'Zona Transp. Destino']]

trocar_cliente = {
    'Id UF Destino' : 'Id UF',
    'Zona Transp. Destino' : 'Zona de Transporte',
    'CNPJ Raiz Cliente' : 'CNPJ Raiz',
    'CNPJ Cliente' : 'CNPJ',
    'CPF Cliente' : 'CPF',
    'Ins. Est. Cliente' : 'Inscrição Estadual',
    'Ins. Mun. Cliente' : 'Inscrição Municipal',
    'Id' : 'Id Cidade',
    'Id Cliente' : 'Id'
    }

cliente.rename(columns = trocar_cliente, inplace = True)

cliente.index = cliente['Id']

cliente.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcliente.csv', index = False, decimal = ',', encoding = 'latin-1')


# Grupo de Mercadorias

colunas_mercadoria = ['Id Grupo Merc.', 'Grupo de Mercadorias']

grupo_mercadoria = formar_tabela_dim(colunas_uteis = colunas_mercadoria)

trocar_mercadoria = {'Id Grupo Merc.' : 'Id'}

grupo_mercadoria.rename(columns = trocar_mercadoria, inplace = True)

grupo_mercadoria.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dgrupo_mercadoria.csv', index = False, decimal = ',', encoding = 'latin-1')


# Produto

colunas_produto = ['Id Produto', 'Produto', 'Unid. Produto', 'NCM Produto', 'Id Grupo Merc.']

produto = formar_tabela_dim(colunas_uteis = colunas_produto)

trocar_produto = {
    'Id Produto' : 'Id',
    'Unid. Produto' : 'Unidade',
    'NCM Produto' : 'NCM'
    }

produto.rename(columns = trocar_produto, inplace = True)

produto.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dproduto.csv', index = False, decimal = ',', encoding = 'latin-1')


# Itinerário

colunas_itinerario = ['Id Itinerário', 'Itinerário', 'Distância KM']

itinerario = formar_tabela_dim(colunas_uteis = colunas_itinerario)

itinerario.rename(columns = {'Id Itinerário' : 'Id'}, inplace = True)

itinerario.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/ditinerario.csv', index = False, decimal = ',', encoding = 'latin-1')

# Contrato

colunas_contrato = [
            'Contrato Venda',
            'Item Contrato',
            'Pedido SalesForce',
            'Tipo Documento',
            'Data de criação',
            'Data Início Entrega',
            'Data Fim Entrega',
            'Qtde Contrato',
            'Valor Contrato',
            'Moeda',
            'Incoterms', 
            'Id Mot. Rec.',
            'Id Centro',
            'Id Local Exp.',
            'Id UF Origem',
            'Origem',
            'Id Cliente',
            'Id UF Destino',
            'Destino',
            'Id Itinerário',
            'Id Grupo Merc.',
            'Id Produto',
    ]

contrato = formar_tabela_dim(colunas_uteis = colunas_contrato)

trocar_contrato = {
    'Tipo Documento' : 'Tipo',
    'Qtde Contrato' : 'Quantidade',
    'Valor Contrato' : 'Valor'
    }

contrato.rename(columns = trocar_contrato, inplace = True)

contrato = contrato[contrato['Quantidade'] > 0]

contrato = contrato.merge(cidade, left_on = ['Origem', 'Id UF Origem'], right_on = ['Cidade', 'Id UF'], how = 'left')

contrato = contrato.merge(cidade, left_on = ['Destino', 'Id UF Destino'], right_on = ['Cidade', 'Id UF'], how = 'left')

trocar_contrato_final = {
    'Id_x' : 'Id Origem',
    'Id_y' : 'Id Destino'
    }

contrato.rename(columns = trocar_contrato_final, inplace = True)

contrato.index = contrato.index + 1

contrato['Id'] = contrato.index

colunas_finais_contrato = [
        'Id',
        'Contrato Venda',
        'Item Contrato',
        'Pedido SalesForce',
        'Tipo',
        'Data de criação',
        'Data Início Entrega',
        'Data Fim Entrega',
        'Quantidade',
        'Valor',
        'Moeda',
        'Incoterms',
        'Id Mot. Rec.',
        'Id Centro',
        'Id Local Exp.',
        'Id UF Origem',
        'Id Origem',
        'Id Cliente',
        'Id UF Destino',
        'Id Destino',
        'Id Itinerário',
        'Id Grupo Merc.',
        'Id Produto'
        ]

contrato = contrato.loc[:, colunas_finais_contrato]

contrato.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcontrato.csv', index = False, decimal = ',', encoding = 'latin-1')


# OV

colunas_OV = [
    'OV',
    'Item OV',
    'Contrato Venda',
    'Item Contrato',
    'Tipo Documento',
    'Data de criação',
    'Qtde OV',
    'Valor OV',
    'Requisição de compra',
    'Id Mot. Rec.',
    'Id Centro',
    'Id Local Exp.',
    'Id UF Origem',
    'Origem',
    'Id Cliente',
    'Id UF Destino',
    'Destino',
    'Id Itinerário',
    'Id Grupo Merc.',
    'Id Produto'
    ]

ov = formar_tabela_dim(colunas_uteis = colunas_OV)

trocar_ov = {
    'Tipo Documento' : 'Tipo',
    'Qtde OV' : 'Quantidade',
    'Valor OV' : 'Valor'
    }

ov.rename(columns = trocar_ov, inplace = True)

ov = ov[ov['Quantidade'] > 0]

ov = ov.merge(cidade, left_on = ['Origem', 'Id UF Origem'], right_on = ['Cidade', 'Id UF'], how = 'left')

ov = ov.merge(cidade, left_on = ['Destino', 'Id UF Destino'], right_on = ['Cidade', 'Id UF'], how = 'left')

ov = ov.merge(contrato[['Id', 'Contrato Venda', 'Item Contrato']], on = ['Contrato Venda', 'Item Contrato'], how = 'left')

trocar_ov_final = {
    'Id_x' : 'Id Origem',
    'Id_y' : 'Id Destino',
    'Id' : 'Id Contrato'
    }

ov.rename(columns = trocar_ov_final, inplace = True)

ov.index = ov.index + 1

ov['Id'] = ov.index

ov = ov.loc[:, ['Id', 'OV', 'Item OV', 'Id Contrato', 'Tipo', 'Data de criação', 'Quantidade', 'Valor', 'Requisição de compra', 'Id Mot. Rec.', 'Id Centro', 'Id Local Exp.', 'Id UF Origem', 'Id Origem', 'Id Cliente', 'Id UF Destino', 'Id Destino', 'Id Itinerário', 'Id Grupo Merc.', 'Id Produto']]

ov.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dov.csv', index = False, decimal = ',', encoding = 'latin-1')


# Nota Fiscal

nf = nota_fiscal()

colunas_contrato = [
        'Id',
        'Contrato Venda',
        'Item Contrato',
        'Id Centro',
        'Id Local Exp.',
        'Id UF Origem',
        'Id Origem',
        'Id Cliente',
        'Id UF Destino',
        'Id Destino',
        'Id Itinerário',
        'Id Grupo Merc.',
        'Id Produto'
    ]

nf = nf.merge(contrato[colunas_contrato], on = ['Contrato Venda', 'Item Contrato'], how = 'left')

ov['OV'] = ov['OV'].astype(str)
ov['Item OV'] = ov['Item OV'].astype(str)

nf = nf.merge(ov[['Id', 'OV', 'Item OV']], on = ['OV', 'Item OV'], how = 'left')

trocar_nome_ov = {
    'Id_x' : 'Id Contrato',
    'Id_y' : 'Id OV'
    }

nf.rename(columns = trocar_nome_ov, inplace = True)

nf.index = nf.index + 1

nf['Id'] = nf.index

nf_ordem_colunas = [
            'Id',
            'Id Contrato',
            'Id OV',
            'Data criação',
            'Tipo',
            'Quantidade',
            'Valor',
            'Cofins',
            'ICMS',
            'PIS',
            'Peso KG',
            'Código status NFe',
            'Remessa',
            'Item Rem',
            'Nº NF',
            'Chave de Acesso - NF',
            'Id Centro',
            'Id Local Exp.',
            'Id UF Origem',
            'Id Origem',
            'Id Cliente',
            'Id UF Destino',
            'Id Destino',
            'Id Itinerário',
            'Id Grupo Merc.',
            'Id Produto'
    ]

nf = nf.loc[:, nf_ordem_colunas]

nf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/fNF.csv', index = False, decimal = ',', encoding = 'latin-1')
