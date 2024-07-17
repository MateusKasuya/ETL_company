import pandas as pd
from src.Bronze.BEX.documentos_sd import formar_tabela_dim
from src.Bronze.BEX.nota_fiscal import formar_tabela_nota_fiscal
from src.Bronze.BEX.DT import formar_tabela_dt
from src.Bronze.BEX.conta_frete import formar_tabela_conta_frete
from src.Bronze.BEX.estoque import formar_tabela_estoque
from src.Bronze.BEX.transferencia import formar_tabela_transf

# Motivo de Recusas


def motivo_recusa():

    colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']

    motivo_recusa = formar_tabela_dim(colunas_uteis=colunas_mot_rec)

    trocar_mot_rec = {'Id Mot. Rec.': 'Id'}

    motivo_recusa.rename(columns=trocar_mot_rec, inplace=True)

    motivo_recusa.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dmotivo_recusa.csv',
                         index=False, decimal=',', encoding='latin-1')
    motivo_recusa.to_excel('Data/Output/Gold/Motivos Recusas.xlsx',
                           index=False)

    return motivo_recusa


# Centro

def centro():

    colunas_centro = ['Id Centro', 'Centro', 'CNPJ Centro', 'Endereço Centro']

    centro = formar_tabela_dim(colunas_uteis=colunas_centro)

    trocar_centro = {
        'Id Centro': 'Id',
        'CNPJ Centro': 'CNPJ',
        'Endereço Centro': 'Endereço'
    }

    centro.rename(columns=trocar_centro, inplace=True)

    centro['Id'] = centro['Id'].astype(str)
    centro['CNPJ'] = centro['CNPJ'].astype(str)

    centro.drop_duplicates(inplace=True)

    centro.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dcentro.csv',
                  index=False, decimal=',', encoding='latin-1')
    centro.to_excel('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Gold/Centro.xlsx',
                    index=False)

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

    uf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dUF.csv',
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

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade


# Local de Expedição

def local_exp():

    colunas_local_exp = ['Id Local Exp.', 'Local Expedição', 'BP Local Expedição',
                         'CNPJ Local Exp.', 'UF Origem', 'Origem']

    local_exp = formar_tabela_dim(colunas_uteis=colunas_local_exp)

    trocar_local_exp = {
        'UF Origem': 'UF',
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
    
    # mask = (local_exp['Id'] == '2165') & (
    #     local_exp['UF'] == 'MA')
    # local_exp = local_exp[~mask]

    local_exp.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dlocal_expedição.csv',
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

    mask = (cliente['Id'] == 1000892) & (
        cliente['Destino'] == 'MONTE ALEGRE DO PIAU')
    cliente = cliente[~mask]

    mask = (cliente['Id'] == 2346077) & (
        cliente['Cliente'] == 'DORAIR ANDRE DOGNANI')
    cliente = cliente[~mask]

    mask = (cliente['Id'] == 1618750) & (
        cliente['Destino'] == 'FORMOSA DO RIO PRETO')
    cliente = cliente[~mask]
    
    mask = (cliente['Id'] == 2297057) & (
        cliente['Cliente'] == 'SAMUEL ANDRE DOGNANI')
    cliente = cliente[~mask]
    
    mask = (cliente['Id'] == 1000057) & (
        cliente['Cliente'] == 'AGREX DO BRASIL LTDA')
    cliente = cliente[~mask]
    
    mask = (cliente['Id'] == 2014500) & (
        cliente['Cliente'] == 'DORAIR ANDRE DOGNANI')
    cliente = cliente[~mask]
    
    mask = (cliente['Id'] == 2313906) & (
        cliente['Destino'] == 'PIUM')
    cliente = cliente[~mask]
    
    mask = (cliente['Id'] == 1999126) & (
        cliente['Destino'] == 'BAIXA GRANDE DO RIBEIRO')
    cliente = cliente[~mask]
    
    cliente.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dcliente.csv',
                   index=False, decimal=',', encoding='latin-1')

    return cliente

# Produto


def produto():

    colunas_produto_carteira = ['Id Produto', 'Produto',
                                'Unid. Produto', 'NCM Produto', 'Grupo de Mercadorias']

    produto_carteira = formar_tabela_dim(
        colunas_uteis=colunas_produto_carteira)

    produto_carteira.dropna(subset='NCM Produto', inplace=True)

    colunas_produto_estoque = ['Id Produto',
                               'Produto', 'Grupo de Mercadorias']

    produto_estoque = formar_tabela_estoque(colunas_produto_estoque)

    produto = pd.concat([produto_carteira, produto_estoque], axis=0)

    produto.drop_duplicates(subset='Id Produto', inplace=True)

    trocar_produto = {
        'Id Produto': 'Id',
        'Unid. Produto': 'Unidade',
        'NCM Produto': 'NCM'
    }

    produto.rename(columns=trocar_produto, inplace=True)

    produto.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dproduto.csv',
                   index=False, decimal=',', encoding='latin-1')
    produto.to_excel('Data/Output/Gold/Produto.xlsx',
                     index=False)

    return produto


# Itinerário

def itinerario():

    colunas_itinerario = ['Id Itinerário', 'Itinerário', 'Distância KM']

    itinerario = formar_tabela_dim(colunas_uteis=colunas_itinerario)

    itinerario.rename(columns={'Id Itinerário': 'Id'}, inplace=True)

    itinerario['Distância KM'] = itinerario['Distância KM'].str.replace(
        'KM', '')
    itinerario['Distância KM'] = itinerario['Distância KM'].str.strip()

    itinerario.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/ditinerario.csv',
                      index=False, decimal=',', encoding='latin-1')
    itinerario.to_excel('Data/Output/Gold/Itinerário.xlsx',
                        index=False)

    return itinerario

# Contrato


def contrato():

    colunas_contrato = [
        'Contrato Venda',
        'Item Contrato',
        'Pedido SalesForce',
        'Tipo Documento',
        'Categoria Documento',
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
        'Origem',
        'UF Origem',
        'Id Cliente',
        'Destino',
        'UF Destino',
        'Id Itinerário',
        'Grupo de Mercadorias',
        'Id Produto',
        'Obs Ped.Niv.Cab(txt)'
    ]

    contrato = formar_tabela_dim(colunas_uteis=colunas_contrato)

    trocar_contrato = {
        'Tipo Documento': 'Tipo',
        'Qtde Contrato': 'Quantidade',
        'Valor Contrato': 'Valor',
        'Peso Liq. Contrato': 'Peso Líquido'
    }

    contrato.rename(columns=trocar_contrato, inplace=True)

    contrato = contrato[contrato['Categoria Documento'] == 'Contrato']

    contrato = contrato[contrato['Quantidade'] != 0]

    contrato.drop(['Categoria Documento'], axis=1, inplace=True)

    contrato['Data do Contrato'] = pd.to_datetime(
        contrato['Data do Contrato'], dayfirst=True)
    contrato['Data Início Entrega'] = pd.to_datetime(
        contrato['Data Início Entrega'], dayfirst=True)
    contrato['Data Fim Entrega'] = pd.to_datetime(
        contrato['Data Fim Entrega'], dayfirst=True)

    contrato['Quantidade'] = contrato['Quantidade'].astype(float)
    contrato['Valor'] = contrato['Valor'].astype(float)
    contrato['Peso Líquido'] = contrato['Peso Líquido'].astype(float)

    contrato['Contrato Venda'] = contrato['Contrato Venda'].astype(str)
    contrato['Item Contrato'] = contrato['Item Contrato'].astype(str)

    contrato.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dcontrato.csv',
                    index=False, decimal=',', encoding='latin-1')

    return contrato


# OV

def ov():

    colunas_OV = [
        'OV',
        'Item OV',
        'Contrato Venda',
        'Item Contrato',
        'Categoria Documento',
        'Tipo Documento',
        'Data da OV',
        'Qtde OV',
        'Valor OV',
        'Peso Liq. OV',
        'Requisição Compra',
        'Id Mot. Rec.',
        'Id Centro',
        'Id Local Exp.',
        'Origem',
        'UF Origem',
        'Id Cliente',
        'Destino',
        'UF Destino',
        'Id Itinerário',
        'Grupo de Mercadorias',
        'Id Produto',
        'Obs N. Fiscal (text)',
        'Rot Entrega (texto)'
    ]

    ov = formar_tabela_dim(colunas_uteis=colunas_OV)

    trocar_ov = {
        'Tipo Documento': 'Tipo',
        'Qtde OV': 'Quantidade',
        'Valor OV': 'Valor',
        'Peso Liq. OV': 'Peso Líquido',
    }

    ov.rename(columns=trocar_ov, inplace=True)

    cat_ov = ['Ordem', 'Devol.']

    ov = ov[ov['Categoria Documento'].isin(cat_ov)]

    ov = ov[ov['Quantidade'] != 0]

    ov.drop(['Categoria Documento'], axis=1, inplace=True)

    ov['Data da OV'] = pd.to_datetime(
        ov['Data da OV'], dayfirst=True)

    ov['Quantidade'] = ov['Quantidade'].astype(float)
    ov['Valor'] = ov['Valor'].astype(float)
    ov['Peso Líquido'] = ov['Peso Líquido'].astype(float)

    ov['Contrato Venda'] = ov['Contrato Venda'].astype(str)
    ov['Item Contrato'] = ov['Item Contrato'].astype(str)

    ov['Contrato-Item'] = ov['Contrato Venda'] + '-' + ov['Item Contrato']

    ov = ov.loc[:, [
        'OV', 'Item OV', 'Contrato-Item', 'Tipo',
        'Data da OV', 'Quantidade', 'Valor', 'Peso Líquido',
        'Requisição Compra', 'Id Mot. Rec.', 'Id Centro', 'Id Local Exp.', 'Origem', 'UF Origem',
        'Id Cliente', 'Destino', 'UF Destino',
        'Id Itinerário', 'Grupo de Mercadorias', 'Id Produto',
        'Obs N. Fiscal (text)', 'Rot Entrega (texto)'
    ]]

    ov.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dOV.csv',
              index=False, decimal=',', encoding='latin-1')

    return ov


# Nota Fiscal

def nf():

    nf = formar_tabela_nota_fiscal()

    nf['Data criação'] = pd.to_datetime(nf['Data criação'], dayfirst=True)

    nf['Quantidade'] = nf['Quantidade'].astype(float)
    nf['Valor'] = nf['Valor'].astype(float)
    nf['Cofins'] = nf['Cofins'].astype(float)
    nf['ICMS'] = nf['ICMS'].astype(float)
    nf['PIS'] = nf['PIS'].astype(float)
    nf['Peso KG'] = nf['Peso KG'].astype(float)

    nf['Contrato Venda'] = nf['Contrato Venda'].astype(str)
    nf['Item Contrato'] = nf['Item Contrato'].astype(str)

    nf['Contrato-Item'] = nf['Contrato Venda'] + '-' + nf['Item Contrato']

    nf['OV'] = nf['OV'].astype(str)
    nf['Item OV'] = nf['Item OV'].astype(str)

    nf['OV-Item'] = nf['OV'] + '-' + nf['Item OV']

    nf = nf.loc[:,
                ['Contrato-Item', 'OV-Item', 'Pedido SalesForce',
                       'Data criação', 'Hora da criação', 'Tipo', 'Código status NFe', 'NF-e: Status Doc',
                       'Id Centro', 'Centro', 'Remessa', 'Item Rem', 'Grupo de mercadorias',
                       'Id Produto', 'Produto', 'Lote', 'Incoterms', 'Nº NF',
                       'Chave de Acesso - NF', 'Quantidade', 'Valor', 'Cofins', 'ICMS', 'PIS',
                       'Peso KG' ]
                ]

    nf.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/fNF.csv',
              index=False, decimal=',', encoding='latin-1')

    return nf

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
        'Categoria',
        'DT Agrupadora Pai',
        'Id Transportador',
        'Transportador',
        'Grupo de Mercadorias'
    ]

    dt = formar_tabela_dt(colunas_dt)

    dt['Data de criação'] = pd.to_datetime(
        dt['Data de criação'], dayfirst=True)

    dt['Quantidade'] = dt['Quantidade'].astype(float)
    dt['Valor Frete Total'] = dt['Valor Frete Total'].astype(float)
    dt['Peso KG'] = dt['Peso KG'].astype(float)

    dt.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/fDT.csv',
              index=False, decimal=',', encoding='latin-1')

    return dt


# Conta Frete

def conta_frete():

    conta_frete = formar_tabela_conta_frete()

    for i in conta_frete['Contrato Venda']:
        if isinstance(i, int):
            int(i)

    for i in conta_frete['Item Contrato']:
        if isinstance(i, int):
            int(i)

    conta_frete['Valor Frete Pedido'] = conta_frete['Valor Frete Pedido'].astype(
        float)

    conta_frete.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/dfrete_pedido.csv',
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

    estoque.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/BEX/destoque.csv',
                   index=False, decimal=',', encoding='latin-1')

    return estoque


# Transferência

def transferencia():

    transf = formar_tabela_transf()

    transf['Data'] = pd.to_datetime(transf['Data'], dayfirst=True)

    transf.to_csv('Data/Output/Silver/BEX/ftransferencia.csv',
                  index=False, decimal=',', encoding='latin-1')

    return transf
