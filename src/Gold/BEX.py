import pandas as pd

def fazer_de_para_cidade_sap_ibge():

    file_cidade_sap = 'Data/Output/Silver/BEX/dcidade.csv'
    file_ibge = 'Data/Output/Silver/De Para Cidades/de_para_bex.csv'
    
    cidade_ibge = pd.read_csv(file_ibge, decimal=',', encoding='latin-1')
    cidade_sap = pd.read_csv(file_cidade_sap, decimal=',', encoding='latin-1')
    
    cidade_sap = cidade_sap.merge(cidade_ibge, left_on = ['Cidade', 'UF'], right_on = ['De-Cidade', 'De-UF'], how = 'left')
     
    cidade_sap = cidade_sap.loc[:, ['Cidade', 'UF', 'Para-Cidade']]
    
    cidade_sap.rename(columns = {'Para-Cidade' : 'Cidade IBGE'}, inplace = True)
    
    cidade_sap.to_excel('Data/Output/Gold/Municípios SAP.xlsx',
                      index=False)
    
    return cidade_sap

def formar_tabela_cliente_gold():

    file_cliente = 'Data/Output/Silver/BEX/dcliente.csv'
    
    cliente = pd.read_csv(file_cliente, encoding='latin-1', decimal = ',')
    
    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'
    
    cidade = pd.read_excel(file_cidade)
    
    cliente = cliente.merge(cidade, left_on = ['Destino', 'UF'], right_on = ['Cidade', 'UF'], how = 'left')
    
    cliente = cliente.loc[:,['Id', 'Cliente', 'CNPJ Raiz', 'CNPJ', 'Inscrição Estadual', 'UF', 'Cidade IBGE']]
    
    cliente.rename(columns = {'Cidade IBGE' : 'Destino'}, inplace = True)
    
    cliente['Cliente'] = cliente['Cliente'].str.title()
    
    cliente.to_excel('Data/Output/Gold/Cliente.xlsx', index = False)
    
    return cliente


def formar_tabela_contrato_gold():

    file_contrato = 'Data/Output/Silver/BEX/dcontrato.csv'
    
    contrato = pd.read_csv(file_contrato, encoding='latin-1', decimal = ',')
    
    file_frete_pedido = 'Data/Output/Silver/BEX/dfrete_pedido.csv'
    
    frete_pedido = pd.read_csv(file_frete_pedido, encoding='latin-1', decimal = ',')
    
    contrato = contrato.merge(frete_pedido, on = ['Contrato Venda', 'Item Contrato'], how = 'left')
    
    contrato['Valor Frete Pedido'] = contrato['Valor Frete Pedido'].fillna(0)
    
    contrato['Contrato Venda'] = contrato['Contrato Venda'].astype(str)
    contrato['Item Contrato'] = contrato['Item Contrato'].astype(str)
    
    contrato['Contrato-Item'] = contrato['Contrato Venda'] + '-' + contrato['Item Contrato']
    
    contrato = contrato.loc[:, ['Contrato-Item', 'Contrato Venda', 'Item Contrato', 'Pedido SalesForce', 'Tipo',
           'Data do Contrato', 'Data Início Entrega', 'Data Fim Entrega',
           'Quantidade', 'Valor', 'Peso Líquido', 'Moeda', 'Incoterms',
           'Id Mot. Rec.', 'Id Centro', 'Id Local Exp.', 'Id Cliente',
           'Id Itinerário', 'Grupo de Mercadorias', 'Id Produto', 'Valor Frete Pedido', 'Obs Ped.Niv.Cab(txt)']]
    
    contrato.to_excel('Data/Output/Gold/Contrato.xlsx', index = False)
    
    return contrato


def formar_tabela_local_expedicao_gold():

    file_local_exp = 'Data/Output/Silver/BEX/dlocal_expedição.csv'
    
    local_exp = pd.read_csv(file_local_exp, encoding='latin-1', decimal = ',')
    
    file_cidade = 'Data/Output/Gold/Municípios SAP.xlsx'
    
    cidade = pd.read_excel(file_cidade)
    
    local_exp = local_exp.merge(cidade, left_on = ['Origem', 'UF'], right_on = ['Cidade', 'UF'], how = 'left')
    
    local_exp = local_exp.loc[:,['Id', 'Local Expedição', 'BP', 'CNPJ', 'UF', 'Cidade IBGE', 'Zona de Transporte']]
    
    local_exp.rename(columns = {'Cidade IBGE' : 'Origem'}, inplace = True)
    
    local_exp['Local Expedição'] = local_exp['Local Expedição'].str.title()
    
    local_exp.to_excel('Data/Output/Gold/Local de Expedição.xlsx', index = False)
    
    return local_exp

