from src.Extraction.carteira_vendas import main_df

def contrato():

    df = main_df()
    
    colunas_contrato = ['Contrato Venda', 'Item Contrato', 'Pedido SalesForce', 'Tipo Documento', 'Data de criação', 'Data Início Entrega', 'Data Fim Entrega', 'Qtde Contrato', 'Valor Contrato', 'Moeda', 'Id Mot. Rec.']
    
    contrato = df[colunas_contrato]
    
    contrato = contrato[contrato['Qtde Contrato'] > 0]
    
    contrato.index = contrato['Contrato Venda'].astype(str) + contrato['Item Contrato'].astype(str)
    
    return contrato
