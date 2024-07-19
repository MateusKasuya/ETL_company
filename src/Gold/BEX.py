import pandas as pd


def fazer_de_para_cidade_sap_ibge():

    file_cidade_sap = 'Data/Output/Silver/BEX/dcidade.csv'
    file_ibge = 'Data/Output/Silver/De Para Cidades/de_para_bex.csv'

    cidade_ibge = pd.read_csv(file_ibge, decimal=',', encoding='latin-1')
    cidade_sap = pd.read_csv(file_cidade_sap, decimal=',', encoding='latin-1')

    cidade_sap = cidade_sap.merge(cidade_ibge, left_on=['Cidade', 'UF'], right_on=[
                                  'De-Cidade', 'De-UF'], how='left')

    cidade_sap = cidade_sap.loc[:, ['Cidade', 'UF', 'Para-Cidade']]

    cidade_sap.rename(columns={'Para-Cidade': 'Cidade IBGE'}, inplace=True)

    cidade_sap.to_excel('Data/Output/Gold/Municípios SAP.xlsx',
                        index=False)

    return cidade_sap


def formar_tabela_cliente_gold():

    file_cliente = 'Data/Output/Silver/BEX/dcliente.csv'

    cliente = pd.read_csv(file_cliente, encoding='latin-1', decimal=',')

    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'

    cidade = pd.read_excel(file_cidade)

    cliente = cliente.merge(cidade, left_on=['Destino', 'UF'], right_on=[
                            'Cidade', 'UF'], how='left')

    cliente = cliente.loc[:, ['Id', 'Cliente', 'CNPJ Raiz',
                              'CNPJ', 'Inscrição Estadual', 'UF', 'Cidade IBGE']]

    cliente.rename(columns={'Cidade IBGE': 'Destino'}, inplace=True)

    cliente['Cliente'] = cliente['Cliente'].str.title()

    cliente.replace('None-None', None, inplace=True)

    cliente.to_excel('Data/Output/Gold/Cliente.xlsx', index=False)

    return cliente


def formar_tabela_local_expedicao_gold():

    file_local_exp = 'Data/Output/Silver/BEX/dlocal_expedição.csv'

    local_exp = pd.read_csv(file_local_exp, encoding='latin-1', decimal=',')

    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'

    cidade = pd.read_excel(file_cidade)

    local_exp = local_exp.merge(cidade, left_on=['Origem', 'UF'], right_on=[
                                'Cidade', 'UF'], how='left')

    local_exp = local_exp.loc[:, [
        'Id', 'Local Expedição', 'BP', 'CNPJ', 'UF', 'Cidade IBGE']]

    local_exp.rename(columns={'Cidade IBGE': 'Origem'}, inplace=True)

    local_exp['Local Expedição'] = local_exp['Local Expedição'].str.title()

    local_exp.replace('None-None', None, inplace=True)

    local_exp.to_excel('Data/Output/Gold/Local de Expedição.xlsx', index=False)

    return local_exp


def formar_tabela_contrato_gold():

    file_contrato = 'Data/Output/Silver/BEX/dcontrato.csv'

    contrato = pd.read_csv(file_contrato, encoding='latin-1', decimal=',')

    # file_frete_pedido = 'Data/Output/Silver/BEX/dfrete_pedido.csv'

    # frete_pedido = pd.read_csv(file_frete_pedido, encoding='latin-1', decimal = ',')

    file_frete_pedido = 'Data/Output/Silver/Sales Force/SalesForce.csv'

    frete_pedido = pd.read_csv(
        file_frete_pedido, encoding='latin-1', decimal=',')

    contrato['Contrato Venda'] = contrato['Contrato Venda'].astype(str)
    contrato['Item Contrato'] = contrato['Item Contrato'].astype(str)

    contrato['Contrato-Item'] = contrato['Contrato Venda'] + \
        '-' + contrato['Item Contrato']

    frete_pedido['Contrato Venda'] = frete_pedido['Contrato Venda'].astype(str)

    contrato = contrato.merge(frete_pedido, on=['Contrato Venda'], how='left')

    contrato['Valor Frete Pedido'] = contrato['Valor Frete Pedido'].fillna(0)

    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'

    cidade = pd.read_excel(file_cidade)

    contrato = contrato.merge(cidade, left_on=['Origem', 'UF Origem'], right_on=[
                              'Cidade', 'UF'], how='left')

    contrato.drop(['Origem'], axis=1, inplace=True)

    contrato.rename(columns={'Cidade IBGE': 'Origem'}, inplace=True)

    contrato = contrato.merge(cidade, left_on=['Destino', 'UF Destino'], right_on=[
                              'Cidade', 'UF'], how='left')

    contrato.drop(['Destino'], axis=1, inplace=True)

    contrato.rename(columns={'Cidade IBGE': 'Destino'}, inplace=True)

    contrato = contrato.loc[:, ['Contrato-Item', 'Contrato Venda', 'Item Contrato', 'Pedido SalesForce', 'Tipo',
                                'Data do Contrato', 'Data Início Entrega', 'Data Fim Entrega',
                                'Quantidade', 'Valor', 'Peso Líquido', 'Moeda', 'Incoterms',
                                'Id Mot. Rec.', 'Id Centro', 'Id Local Exp.', 'Origem', 'UF Origem', 'Id Cliente', 'Destino', 'UF Destino',
                                'Id Itinerário', 'Grupo de Mercadorias', 'Id Produto', 'Valor Frete Pedido', 'Obs Ped.Niv.Cab(txt)']]

    contrato.replace('None-None', None, inplace=True)

    contrato.to_excel('Data/Output/Gold/Contrato.xlsx', index=False)

    return contrato


def formar_tabela_ov_gold():

    file_ov = 'Data/Output/Silver/BEX/dOV.csv'

    ov = pd.read_csv(file_ov, encoding='latin-1', decimal=',')

    ov['OV'] = ov['OV'].astype(str)
    ov['Item OV'] = ov['Item OV'].astype(str)

    ov['OV-Item'] = ov['OV'] + '-' + ov['Item OV']

    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'

    cidade = pd.read_excel(file_cidade)

    ov = ov.merge(cidade, left_on=['Origem', 'UF Origem'], right_on=[
                  'Cidade', 'UF'], how='left')

    ov.drop(['Origem'], axis=1, inplace=True)

    ov.rename(columns={'Cidade IBGE': 'Origem'}, inplace=True)

    ov = ov.merge(cidade, left_on=['Destino', 'UF Destino'], right_on=[
                  'Cidade', 'UF'], how='left')

    ov.drop(['Destino'], axis=1, inplace=True)

    ov.rename(columns={'Cidade IBGE': 'Destino'}, inplace=True)

    file_contrato = 'Data/Output/Gold/Contrato.xlsx'

    contrato = pd.read_excel(file_contrato)

    contrato = contrato.loc[:, ['Contrato-Item', 'Valor Frete Pedido']]

    ov = ov.merge(contrato, on='Contrato-Item', how='left')

    ov = ov.loc[:, ['OV-Item', 'OV', 'Item OV', 'Contrato-Item', 'Tipo', 'Data da OV', 'Quantidade',
                    'Valor', 'Peso Líquido', 'Valor Frete Pedido', 'Requisição Compra', 'Id Mot. Rec.',
                    'Id Centro', 'Id Local Exp.', 'Origem', 'UF Origem', 'Id Cliente', 'Destino', 'UF Destino',
                    'Id Itinerário', 'Grupo de Mercadorias',
                    'Id Produto', 'Obs N. Fiscal (text)', 'Rot Entrega (texto)']]

    ov.replace('None-None', None, inplace=True)

    ov.to_excel('Data/Output/Gold/Ordem de Venda.xlsx', index=False)

    return ov


def formar_tabela_nf_gold():

    file_nf = 'Data/Output/Silver/BEX/fNF.csv'

    nf = pd.read_csv(file_nf, encoding='latin-1',
                     decimal=',', low_memory=False)

    file_ov = 'Data/Output/Gold/Ordem de Venda.xlsx'

    ov = pd.read_excel(file_ov)

    ov = ov.loc[:, ['OV-Item',
                    'Id Local Exp.', 'Origem', 'UF Origem',
                    'Id Cliente', 'Destino', 'UF Destino', 'Valor Frete Pedido']]

    nf = nf.merge(ov, on='OV-Item', how='left')

    file_lexp = 'Data/Output/Gold/Local de Expedição.xlsx'

    local_exp = pd.read_excel(file_lexp)

    local_exp = local_exp.loc[:, ['Id', 'Local Expedição']]

    nf = nf.merge(local_exp, left_on='Id Local Exp.',
                  right_on='Id', how='left')

    file_cliente = 'Data/Output/Gold/Cliente.xlsx'

    cliente = pd.read_excel(file_cliente)

    cliente = cliente.loc[:, ['Id', 'Cliente']]

    nf = nf.merge(cliente, left_on='Id Cliente', right_on='Id', how='left')

    nf = nf.loc[:, ['Contrato-Item', 'OV-Item', 'Pedido SalesForce', 'Data criação',
                    'Hora da criação', 'Tipo', 'Código status NFe', 'NF-e: Status Doc',
                    'Id Centro', 'Centro', 'Remessa', 'Item Rem', 'Grupo de mercadorias',
                    'Id Produto', 'Produto', 'Lote', 'Incoterms', 'Nº NF',
                    'Chave de Acesso - NF', 'Id Local Exp.', 'Local Expedição', 'Origem', 'UF Origem', 'Id Cliente', 'Cliente',
                    'Destino', 'UF Destino', 'Quantidade', 'Valor', 'Cofins', 'ICMS', 'PIS',
                    'Peso KG', 'Valor Frete Pedido']]

    nf.replace('None-None', None, inplace=True)

    nf.to_excel('Data/Output/Gold/Nota Fiscal.xlsx', index=False)

    return nf


def formar_tabela_dt_gold():

    file_dt = 'Data/Output/Silver/BEX/fDT.csv'

    dt = pd.read_csv(file_dt, encoding='latin-1', decimal=',')

    file_nf = 'Data/Output/Gold/Nota Fiscal.xlsx'

    nf = pd.read_excel(file_nf)

    nf = nf.loc[:, ['OV-Item', 'Remessa', 'Item Rem']]

    nf.drop_duplicates(inplace=True)

    dt = dt.merge(nf, on=['Remessa', 'Item Rem'], how='left')

    dt = dt.loc[:, ['DT', 'Remessa', 'Item Rem', 'OV-Item', 'Data de criação', 'Quantidade',
                    'Valor Frete Total', 'Peso KG', 'Item Superior', 'Id Categoria',
                    'Categoria', 'DT Agrupadora Pai', 'Id Transportador', 'Transportador',
                    'Grupo de Mercadorias']]

    dt.replace('None-None', None, inplace=True)

    dt.to_excel('Data/Output/Gold/Documento de Transporte.xlsx', index=False)

    return dt


def formar_tabela_transf_gold():

    file_transf = 'Data/Output/Silver/BEX/ftransferencia.csv'

    transf = pd.read_csv(file_transf, encoding='latin-1', decimal=',')

    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'

    cidade = pd.read_excel(file_cidade)

    transf = transf.merge(cidade, left_on=['Origem', 'UF Origem'], right_on=[
                          'Cidade', 'UF'], how='left')

    transf.drop(['Origem'], axis=1, inplace=True)

    transf.rename(columns={'Cidade IBGE': 'Origem'}, inplace=True)

    transf = transf.merge(cidade, left_on=['Destino', 'UF Destino'], right_on=[
                          'Cidade', 'UF'], how='left')

    transf.drop(['Destino'], axis=1, inplace=True)

    transf.rename(columns={'Cidade IBGE': 'Destino'}, inplace=True)

    transf = transf.loc[:, ['Pedido Transf.', 'Data', 'Centro fornecedor', 'Origem', 'UF Origem', 'Recebedor',
                            'Destino', 'UF Destino', 'Grupo de mercadorias']]

    transf['Data'] = pd.to_datetime(transf['Data'])

    transf.replace('None-None', None, inplace=True)

    transf.to_excel('Data/Output/Gold/Transferência.xlsx', index=False)

    return transf


def formar_tabela_gerencial_frete_gold():

    file_gf = 'Data/Output/Silver/BEX/fgerencial_frete.csv'

    gf = pd.read_csv(file_gf, encoding='latin-1',
                     decimal=',', low_memory=False)

    file_ov = 'Data/Output/Gold/Ordem de Venda.xlsx'

    ov = pd.read_excel(file_ov)

    ov = ov.loc[:, ['OV-Item',
                    'Origem', 'UF Origem',
                    'Destino', 'UF Destino']]

    gf = gf.merge(ov, on='OV-Item', how='left')

    ordem_colunas_gf = [
        'Contrato Venda', 'Item Contrato', 'OV-Item', 'Origem',
        'UF Origem', 'Destino', 'UF Destino', 'Grupo de Mercadorias',
        'Incoterms', 'Frete', 'Volume Receita', 'Gross Sales', 'Net Sales',
        'Classe Contas', 'Documento Contábil', 'Item Doc Contábil',
        'Data de lançamento', 'Data Compensação', 'Data Vencimento'
    ]

    gf = gf.loc[:, ordem_colunas_gf]

    gf.replace('None-None', None, inplace=True)

    gf.to_excel('Data/Output/Gold/Gerencial Frete.xlsx', index=False)

    return gf
