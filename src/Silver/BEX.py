import pandas as pd
from src.Bronze.BEX.carteira_vendas import formar_tabela_dim
from src.Bronze.BEX.nota_fiscal import formar_tabela_nota_fiscal
from src.Bronze.BEX.DT import formar_tabela_dt
from src.Bronze.BEX.conta_frete import formar_tabela_conta_frete
from src.Bronze.BEX.estoque import formar_tabela_estoque

# Motivo de Recusas


def motivo_recusa():

    colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']

    motivo_recusa = formar_tabela_dim(colunas_uteis=colunas_mot_rec)

    trocar_mot_rec = {'Id Mot. Rec.': 'Id'}

    motivo_recusa.rename(columns=trocar_mot_rec, inplace=True)

    motivo_recusa.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dmotivo_recusa.csv',
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

    centro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dcentro.csv',
                  index=False, decimal=',', encoding='latin-1')

    return centro

# UF


def uf():

    colunas_uf_origem = ['UF Origem', 'Nome UF Origem']

    uf_origem = formar_tabela_dim(colunas_uteis=colunas_uf_origem)

    trocar_nome_uf_origem = {
        'UF Origem': 'UF',
        'Nome UF Origem': 'Nome UF'
    }

    uf_origem.rename(columns=trocar_nome_uf_origem, inplace=True)

    colunas_uf_destino = ['UF Destino', 'Nome UF Destino']

    uf_destino = formar_tabela_dim(colunas_uteis=colunas_uf_destino)

    trocar_nome_uf_destino = {
        'UF Destino': 'UF',
        'Nome UF Destino': 'Nome UF'
    }

    uf_destino.rename(columns=trocar_nome_uf_destino, inplace=True)

    uf = pd.concat([uf_origem, uf_destino], axis=0)

    uf.drop_duplicates(inplace=True)

    uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dUF.csv',
              index=False, decimal=',', encoding='latin-1')

    return uf


# Cidade

def cidade():

    colunas_origem = ['Origem', 'UF Origem']

    origem = formar_tabela_dim(colunas_uteis=colunas_origem)

    trocar_nome_origem = {
        'Origem': 'Cidade',
        'UF Origem': 'UF'
    }

    origem.rename(columns=trocar_nome_origem, inplace=True)

    colunas_destino = ['Destino', 'UF Destino']

    destino = formar_tabela_dim(colunas_uteis=colunas_destino)

    trocar_nome_destino = {
        'Destino': 'Cidade',
        'UF Destino': 'UF',
    }

    destino.rename(columns=trocar_nome_destino, inplace=True)

    cidade = pd.concat([origem, destino], axis=0)

    cidade.drop_duplicates(inplace=True)

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade


# Local de Expedição

def local_exp():

    colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'BP Local Expedição',
                         'CNPJ Local Exp.', 'UF Origem', 'Origem', 'Zona Transp. Origem']

    local_exp = formar_tabela_dim(colunas_uteis=colunas_local_exp)

    trocar_local_exp = {
        'UF Origem': 'UF',
        'Zona Transp. Origem': 'Zona de Transporte',
        'CNPJ Local Exp.': 'CNPJ',
        'Id Local Exp.': 'Id',
        'BP Local Expedição': 'BP'
    }

    local_exp.rename(columns=trocar_local_exp, inplace=True)

    local_exp['BP'] = local_exp['BP'].str.replace('BP', '')
    local_exp['BP'] = local_exp['BP'].str.replace('-', '')
    local_exp['BP'] = local_exp['BP'].str.strip()

    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('CNPJ', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('CPF', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.replace('-', '')
    local_exp['CNPJ'] = local_exp['CNPJ'].str.strip()

    local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dlocal_expedição.csv',
                     index=False, decimal=',', encoding='latin-1')

    return local_exp


# Cliente

def cliente():

    colunas_clientes = ['Id Cliente', 'Cliente', 'CNPJ Raiz Cliente',
                        'CNPJ Cliente', 'Ins. Est. Cliente', 'UF Destino', 'Destino']

    cliente = formar_tabela_dim(colunas_uteis=colunas_clientes)

    trocar_cliente = {
        'UF Destino': 'UF',
        'CNPJ Raiz Cliente': 'CNPJ Raiz',
        'CNPJ Cliente': 'CNPJ',
        'Ins. Est. Cliente': 'Inscrição Estadual',
        'Id Cliente': 'Id'
    }

    cliente.rename(columns=trocar_cliente, inplace=True)

    cliente.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dcliente.csv',
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

    grupo_mercadoria.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dgrupo_mercadoria.csv',
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

    produto.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dproduto.csv',
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

    itinerario.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/ditinerario.csv',
                      index=False, decimal=',', encoding='latin-1')

    return itinerario

# Contrato


def contrato():

    colunas_contrato = [
        'Contrato Venda',
        'Item Contrato',
        'Pedido SalesForce',
        'Tipo Documento',
        'Data do Contrato',
        'Data Início Entrega',
        'Data Fim Entrega',
        'Qtde Contrato',
        'Valor Contrato',
        'Peso Liq. Contrato',
        'Moeda',
        'Incoterms',
        'Id Mot. Rec.',
        'Id Centro',
        'Id Local Exp.',
        'Id Cliente',
        'Id Itinerário',
        'Incoterms',
        'Id Grupo Merc.',
        'Id Produto',
        'Obs Ped.Niv.Cab(txt)'
    ]

    contrato = formar_tabela_dim(colunas_uteis=colunas_contrato)

    trocar_contrato = {
        'Tipo Documento': 'Tipo',
        'Qtde Contrato': 'Quantidade',
        'Valor Contrato': 'Valor'
    }

    contrato.rename(columns=trocar_contrato, inplace=True)

    contrato = contrato[contrato['Quantidade'] > 0]

    contrato['Data do Contrato'] = pd.to_datetime(
        contrato['Data do Contrato'], dayfirst=True)
    contrato['Data Início Entrega'] = pd.to_datetime(
        contrato['Data Início Entrega'], dayfirst=True)
    contrato['Data Fim Entrega'] = pd.to_datetime(
        contrato['Data Fim Entrega'], dayfirst=True)

    contrato.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dcontrato.csv',
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
        'UF Origem',
        'Origem',
        'Id Cliente',
        'UF Destino',
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

    ov['Data de criação'] = pd.to_datetime(
        ov['Data de criação'], dayfirst=True)

    ov.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dOV.csv',
              index=False, decimal=',', encoding='latin-1')

    return ov


# Nota Fiscal

def nf():

    nf = formar_tabela_nota_fiscal()

    nf['Data criação'] = pd.to_datetime(nf['Data criação'], dayfirst=True)

    nf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/fNF.csv',
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

    categoria.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dcategoria_dt.csv',
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

    transportador.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dtransportador.csv',
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
        'Peso KG',
        'Item Superior',
        'Id Categoria',
        'Id Transportador',
    ]

    dt = formar_tabela_dt(colunas_dt)

    dt['Data de criação'] = pd.to_datetime(
        dt['Data de criação'], dayfirst=True)

    dt.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/fDT.csv',
              index=False, decimal=',', encoding='latin-1')

    return dt


# Conta Frete

def conta_frete():

    conta_frete = formar_tabela_conta_frete()

    conta_frete.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/dfrete_pedido.csv',
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

    estoque['Data Vencimento'] = pd.to_datetime(
        estoque['Data Vencimento'], dayfirst=True)
    estoque['Data Última EM'] = pd.to_datetime(
        estoque['Data Última EM'], dayfirst=True)

    estoque.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/BEX/destoque.csv',
                   index=False, decimal=',', encoding='latin-1')

    return estoque
