import pandas as pd
from src.DataFrame.carteira_vendas import formar_tabela_dim
from src.DataFrame.nota_fiscal import formar_tabela_nota_fiscal
from src.DataFrame.DT import formar_tabela_dt
from src.DataFrame.conta_frete import formar_tabela_conta_frete
from src.DataFrame.estoque import formar_tabela_estoque

# Motivo de Recusas


def motivo_recusa():

    colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']

    motivo_recusa = formar_tabela_dim(colunas_uteis=colunas_mot_rec)

    trocar_mot_rec = {'Id Mot. Rec.': 'Id'}

    motivo_recusa.rename(columns=trocar_mot_rec, inplace=True)

    motivo_recusa.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dmotivo_recusa.csv',
                         index=False, decimal=',', encoding='latin-1')

    return motivo_recusa


# Centro

def centro():

    colunas_centro = ['Id Centro', 'Centro', 'CNPJ Centro']

    centro = formar_tabela_dim(colunas_uteis=colunas_centro)

    trocar_centro = {
        'Id Centro': 'Id',
        'CNPJ Centro': 'CNPJ'
    }

    centro.rename(columns=trocar_centro, inplace=True)

    centro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcentro.csv',
                  index=False, decimal=',', encoding='latin-1')

    return centro

# UF


def uf():

    colunas_uf_origem = ['Id UF Origem', 'UF Origem']

    uf_origem = formar_tabela_dim(colunas_uteis=colunas_uf_origem)

    trocar_nome_uf_origem = {
        'Id UF Origem': 'Id',
        'UF Origem': 'UF'
    }

    uf_origem.rename(columns=trocar_nome_uf_origem, inplace=True)

    colunas_uf_destino = ['Id UF Destino', 'UF Destino']

    uf_destino = formar_tabela_dim(colunas_uteis=colunas_uf_destino)

    trocar_nome_uf_destino = {
        'Id UF Destino': 'Id',
        'UF Destino': 'UF'
    }

    uf_destino.rename(columns=trocar_nome_uf_destino, inplace=True)

    uf = pd.concat([uf_origem, uf_destino], axis=0)

    uf.drop_duplicates(inplace=True)

    uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dUF.csv',
              index=False, decimal=',', encoding='latin-1')

    return uf


# Cidade

def cidade():

    colunas_origem = ['Origem', 'Id UF Origem']

    origem = formar_tabela_dim(colunas_uteis=colunas_origem)

    trocar_nome_origem = {
        'Origem': 'Cidade',
        'Id UF Origem': 'Id UF'
    }

    origem.rename(columns=trocar_nome_origem, inplace=True)

    colunas_destino = ['Destino', 'Id UF Destino']

    destino = formar_tabela_dim(colunas_uteis=colunas_destino)

    trocar_nome_destino = {
        'Destino': 'Cidade',
        'Id UF Destino': 'Id UF',
    }

    destino.rename(columns=trocar_nome_destino, inplace=True)

    cidade = pd.concat([origem, destino], axis=0)

    cidade.drop_duplicates(inplace=True)

    cidade.reset_index(drop=True, inplace=True)

    cidade.index = cidade.index + 1

    cidade['Id'] = cidade.index

    cidade = cidade.loc[:, ['Id', 'Cidade', 'Id UF']]

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade


# Local de Expedição

def local_exp():

    colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'BP Local Expedição',
                         'CNPJ Local Exp.', 'Id UF Origem', 'Origem', 'Zona Transp. Origem',]

    local_exp = formar_tabela_dim(colunas_uteis=colunas_local_exp)

    cidade_function = cidade()

    local_exp = local_exp.merge(cidade_function, left_on=[
                                'Origem', 'Id UF Origem'], right_on=['Cidade', 'Id UF'], how='left')

    local_exp = local_exp.loc[:, ['Id Local Exp.', 'Local Expedição', 'BP Local Expedição',
                                  'CNPJ Local Exp.', 'Id UF Origem', 'Id', 'Zona Transp. Origem']]

    trocar_local_exp = {
        'Id UF Origem': 'Id UF',
        'Zona Transp. Origem': 'Zona de Transporte',
        'CNPJ Local Exp.': 'CNPJ',
        'Id': 'Id Cidade',
        'Id Local Exp.': 'Id',
        'BP Local Expedição': 'BP'
    }

    local_exp.rename(columns=trocar_local_exp, inplace=True)

    local_exp.index = local_exp['Id']

    local_exp['BP'] = local_exp['BP'].str.replace('BP', '')
    local_exp['BP'] = local_exp['BP'].str.replace('-', '')
    local_exp['BP'] = local_exp['BP'].str.strip()

    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('CNPJ', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('CPF', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('-', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.strip()

    local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dlocal_expedição.csv',
                     index=False, decimal=',', encoding='latin-1')

    return local_exp


# Cliente

def cliente():

    colunas_clientes = ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente',
                        'CNPJ Cliente', 'Ins. Est. Cliente', 'Id UF Destino', 'Destino']

    cliente = formar_tabela_dim(colunas_uteis=colunas_clientes)

    cidade_funtion = cidade()

    cliente = cliente.merge(cidade_funtion, left_on=[
                            'Destino', 'Id UF Destino'], right_on=['Cidade', 'Id UF'], how='left')

    trocar_cliente = {
        'Id UF Destino': 'Id UF',
        'CNPJ Raiz Cliente': 'CNPJ Raiz',
        'CNPJ Cliente': 'CNPJ',
        'Ins. Est. Cliente': 'Inscrição Estadual',
        'Id': 'Id Cidade',
        'Id Cliente': 'Id'
    }

    cliente.rename(columns=trocar_cliente, inplace=True)

    cliente.index = cliente['Id']

    cliente = cliente.loc[:, ['Id', 'Cliente', 'CNPJ Raiz',
                              'CNPJ', 'Inscrição Estadual', 'Id UF', 'Id Cidade']]

    cliente.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcliente.csv',
                   index=False, decimal=',', encoding='latin-1')

    return cliente


# Grupo de Mercadorias

def grupo_mercadoria():

    colunas_mercadoria_carteira = ['Id Grupo Merc.', 'Grupo de Mercadorias']

    grupo_mercadoria_carteira = formar_tabela_dim(
        colunas_uteis=colunas_mercadoria_carteira)

    colunas_mercadoria_estoque = ['Id Grupo Merc.', 'Grupo de Mercadorias']

    grupo_mercadoria_estoque = formar_tabela_estoque(
        colunas_mercadoria_estoque)

    grupo_mercadoria = pd.concat(
        [grupo_mercadoria_carteira, grupo_mercadoria_estoque], axis=0)

    grupo_mercadoria.drop_duplicates(inplace=True)

    trocar_mercadoria = {'Id Grupo Merc.': 'Id'}

    grupo_mercadoria.rename(columns=trocar_mercadoria, inplace=True)

    grupo_mercadoria.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dgrupo_mercadoria.csv',
                            index=False, decimal=',', encoding='latin-1')

    return grupo_mercadoria
# Produto


def produto():

    colunas_produto_carteira = ['Id Produto', 'Produto',
                                'Unid. Produto', 'NCM Produto', 'Id Grupo Merc.']

    produto_carteira = formar_tabela_dim(
        colunas_uteis=colunas_produto_carteira)

    produto_carteira.dropna(subset='NCM Produto', inplace=True)

    colunas_produto_estoque = ['Id Produto',  'Produto', 'Id Grupo Merc.']

    produto_estoque = formar_tabela_estoque(colunas_produto_estoque)

    produto = pd.concat([produto_carteira, produto_estoque], axis=0)

    produto.drop_duplicates(subset='Id Produto', inplace=True)

    trocar_produto = {
        'Id Produto': 'Id',
        'Unid. Produto': 'Unidade',
        'NCM Produto': 'NCM'
    }

    produto.rename(columns=trocar_produto, inplace=True)

    produto.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dproduto.csv',
                   index=False, decimal=',', encoding='latin-1')

    return produto


# Itinerário

def itinerario():

    colunas_itinerario = ['Id Itinerário', 'Itinerário', 'Distância KM']

    itinerario = formar_tabela_dim(colunas_uteis=colunas_itinerario)

    itinerario.rename(columns={'Id Itinerário': 'Id'}, inplace=True)

    itinerario['Distância KM'] = itinerario['Distância KM'].str.replace(
        'KM', '')
    itinerario['Distância KM'] = itinerario['Distância KM'].str.strip()

    itinerario.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/ditinerario.csv',
                      index=False, decimal=',', encoding='latin-1')

    return itinerario

# Contrato


def contrato():

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
        'CPF Cliente',
        'Ins. Mun. Cliente',
        'Zona Transp. Destino',
        'Id UF Destino',
        'Destino',
        'Id Itinerário',
        'Id Grupo Merc.',
        'Id Produto',
    ]

    contrato = formar_tabela_dim(colunas_uteis=colunas_contrato)

    trocar_contrato = {
        'Tipo Documento': 'Tipo',
        'Qtde Contrato': 'Quantidade',
        'Valor Contrato': 'Valor'
    }

    contrato.rename(columns=trocar_contrato, inplace=True)

    contrato = contrato[contrato['Quantidade'] > 0]

    cidade_function = cidade()

    contrato = contrato.merge(cidade_function, left_on=[
                              'Origem', 'Id UF Origem'], right_on=['Cidade', 'Id UF'], how='left')

    contrato = contrato.merge(cidade_function, left_on=[
                              'Destino', 'Id UF Destino'], right_on=['Cidade', 'Id UF'], how='left')

    trocar_contrato_final = {
        'Id_x': 'Id Origem',
        'Id_y': 'Id Destino'
    }

    contrato.rename(columns=trocar_contrato_final, inplace=True)

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
        'CPF Cliente',
        'Ins. Mun. Cliente',
        'Id UF Destino',
        'Id Destino',
        'Zona Transp. Destino',
        'Id Itinerário',
        'Id Grupo Merc.',
        'Id Produto'
    ]

    contrato = contrato.loc[:, colunas_finais_contrato]

    contrato['Data de criação'] = pd.to_datetime(
        contrato['Data de criação'], dayfirst=True)
    contrato['Data Início Entrega'] = pd.to_datetime(
        contrato['Data Início Entrega'], dayfirst=True)
    contrato['Data Fim Entrega'] = pd.to_datetime(
        contrato['Data Fim Entrega'], dayfirst=True)

    contrato.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcontrato.csv',
                    index=False, decimal=',', encoding='latin-1')

    return contrato


# OV

def ov():

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

    ov = formar_tabela_dim(colunas_uteis=colunas_OV)

    trocar_ov = {
        'Tipo Documento': 'Tipo',
        'Qtde OV': 'Quantidade',
        'Valor OV': 'Valor'
    }

    ov.rename(columns=trocar_ov, inplace=True)

    ov = ov[ov['Quantidade'] > 0]

    cidade_function = cidade()

    contrato_function = contrato()

    ov = ov.merge(cidade_function, left_on=['Origem', 'Id UF Origem'], right_on=[
                  'Cidade', 'Id UF'], how='left')

    ov = ov.merge(cidade_function, left_on=['Destino', 'Id UF Destino'], right_on=[
                  'Cidade', 'Id UF'], how='left')

    ov = ov.merge(contrato_function[['Id', 'Contrato Venda', 'Item Contrato']], on=[
                  'Contrato Venda', 'Item Contrato'], how='left')

    trocar_ov_final = {
        'Id_x': 'Id Origem',
        'Id_y': 'Id Destino',
        'Id': 'Id Contrato'
    }

    ov.rename(columns=trocar_ov_final, inplace=True)

    ov.index = ov.index + 1

    ov['Id'] = ov.index

    ov = ov.loc[:, ['Id', 'OV', 'Item OV', 'Id Contrato', 'Tipo', 'Data de criação', 'Quantidade', 'Valor', 'Requisição de compra', 'Id Mot. Rec.',
                    'Id Centro', 'Id Local Exp.', 'Id UF Origem', 'Id Origem', 'Id Cliente', 'Id UF Destino', 'Id Destino', 'Id Itinerário', 'Id Grupo Merc.', 'Id Produto']]

    ov['Data de criação'] = pd.to_datetime(
        ov['Data de criação'], dayfirst=True)

    ov.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dov.csv',
              index=False, decimal=',', encoding='latin-1')

    return ov


# Nota Fiscal

def nf():

    nf = formar_tabela_nota_fiscal()

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

    contrato_function = contrato()

    nf = nf.merge(contrato_function[colunas_contrato], on=[
                  'Contrato Venda', 'Item Contrato'], how='left')

    ov_function = ov()

    ov_function['OV'] = ov_function['OV'].astype(str)
    ov_function['Item OV'] = ov_function['Item OV'].astype(str)

    nf = nf.merge(ov_function[['Id', 'OV', 'Item OV']],
                  on=['OV', 'Item OV'], how='left')

    trocar_nome_ov = {
        'Id_x': 'Id Contrato',
        'Id_y': 'Id OV'
    }

    nf.rename(columns=trocar_nome_ov, inplace=True)

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

    nf['Data criação'] = pd.to_datetime(nf['Data criação'], dayfirst=True)

    nf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/fNF.csv',
              index=False, decimal=',', encoding='latin-1')

    return nf


# Categoria DT

def categoria():

    colunas_categoria = [
        'Id Categoria',
        'Categoria'
    ]

    categoria = formar_tabela_dt(colunas_categoria)

    categoria.rename(columns={'Id Categoria': 'Id'}, inplace=True)

    categoria.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dcategoria_dt.csv',
                     index=False, decimal=',', encoding='latin-1')

    return categoria


# Transportador

def transportador():

    colunas_transportador = [
        'Id Transportador',
        'Transportador'
    ]

    transportador = formar_tabela_dt(colunas_transportador)

    transportador.rename(columns={'Id Transportador': 'Id'}, inplace=True)

    transportador.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dtransportador.csv',
                         index=False, decimal=',', encoding='latin-1')

    return transportador


# DT

def dt():

    colunas_dt = [
        'DT',
        'Remessa',
        'Item Rem',
        'Data de criação',
        'Quantidade',
        'Valor Frete Total',
        'Valor Frete Lote',
        'Peso KG',
        'Item Superior',
        'Id Categoria',
        'Id Transportador',
    ]

    dt = formar_tabela_dt(colunas_dt)

    dt['Remessa'] = dt['Remessa'].astype(str)
    dt['Item Rem'] = dt['Item Rem'].astype(str)

    nf_function = nf()

    dt = dt.merge(nf_function[['Remessa', 'Item Rem', 'Id']], on=[
                  'Remessa', 'Item Rem'], how='left')

    dt.rename(columns={'Id': 'Id NF'}, inplace=True)

    dt.index = dt.index + 1

    dt['Id'] = dt.index

    nova_ordem_dt = [
        'Id',
        'DT',
        'Remessa',
        'Item Rem',
        'Data de criação',
        'Quantidade',
        'Valor Frete Total',
        'Valor Frete Lote',
        'Peso KG',
        'Item Superior',
        'Id Categoria',
        'Id Transportador',
        'Id NF'
    ]

    dt = dt.loc[:, nova_ordem_dt]

    dt['Data de criação'] = pd.to_datetime(
        dt['Data de criação'], dayfirst=True)

    dt.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/fDT.csv',
              index=False, decimal=',', encoding='latin-1')

    return dt


# Conta Frete

def conta_frete():

    conta_frete = formar_tabela_conta_frete()

    contrato_function = contrato()

    conta_frete = conta_frete.merge(contrato_function[['Contrato Venda', 'Item Contrato', 'Id']], on=[
                                    'Contrato Venda', 'Item Contrato'], how='left')

    conta_frete.rename(columns={'Id': 'Id Contrato'}, inplace=True)

    conta_frete.index = conta_frete.index + 1

    conta_frete['Id'] = conta_frete.index

    conta_frete = conta_frete.loc[:, [
        'Id', 'Valor Frete Pedido', 'Id Contrato']]

    conta_frete.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/dfrete_pedido.csv',
                       index=False, decimal=',', encoding='latin-1')

    return conta_frete


# Estoque

def estoque():

    colunas_estoque = [
        'Id Centro',
        'Id Grupo Merc.',
        'Id Produto',
        'Lote',
        'Data Vencimento',
        'Data Última EM',
        'Texto Cabeç Doc',
        'Id Cliente',
        'Estoque Livre',
        'Estoque Bloqueado',
        'Estoque Consignado'
    ]

    estoque = formar_tabela_estoque(colunas_estoque)

    estoque.reset_index(drop=True, inplace=True)

    estoque.index = estoque.index + 1

    estoque['Id'] = estoque.index

    ordem_colunas_estoque = [
        'Id',
        'Id Centro',
        'Id Grupo Merc.',
        'Id Produto',
        'Lote',
        'Data Vencimento',
        'Data Última EM',
        'Texto Cabeç Doc',
        'Id Cliente',
        'Estoque Livre',
        'Estoque Bloqueado',
        'Estoque Consignado'
    ]

    estoque = estoque.loc[:, ordem_colunas_estoque]

    estoque['Data Vencimento'] = pd.to_datetime(
        estoque['Data Vencimento'], dayfirst=True)
    estoque['Data Última EM'] = pd.to_datetime(
        estoque['Data Última EM'], dayfirst=True)

    estoque.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/destoque.csv',
                   index=False, decimal=',', encoding='latin-1')

    return estoque
