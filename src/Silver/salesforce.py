import pandas as pd

def salesforce():

    file_sf = 'C:\\Users\\O1000246\\BUNGE\\Dados Supply Origeo - Documentos\\ETL\\Bases\\SalesForce\\SalesForce.xlsx'
    
    df_sf = pd.read_excel(file_sf)
    
    df_sf.drop(df_sf.index[:3], inplace=True)
    df_sf = df_sf.set_axis(df_sf.iloc[0], axis=1)
    df_sf.drop(df_sf.index[:1], inplace=True)
    df_sf.drop(df_sf.index[-2:], inplace=True)
    df_sf.drop(df_sf.columns[[0, 2]], axis=1, inplace=True)
    
    df_sf.dropna(subset=['Contrato SAP'], inplace=True)
    
    df_sf = df_sf.loc[:, ['Contrato SAP',
                          'Data de criação', 'Valor Frete Unitário', 'Moeda']]
    
    df_sf.rename(
        columns={'Valor Frete Unitário': 'Valor Frete Pedido',
                 'Contrato SAP' : 'Contrato Venda'}, inplace=True)
       
    df_sf['Contrato Venda'] = df_sf['Contrato Venda'].apply(
        lambda string: string[:string.find('-')])
    df_sf['Contrato Venda'] = df_sf['Contrato Venda'].str.lstrip("0")
       
    df_sf['Data de criação'] = pd.to_datetime(
        df_sf['Data de criação'], format='%d/%m/%Y')
    
    df_sf['Valor Frete Pedido'] = df_sf['Valor Frete Pedido'].astype(float)
    
    data_comparacao = pd.to_datetime('2024-06-01')
    
    for index, row in df_sf.iterrows():
        if row['Moeda'] == 'USD' and row['Data de criação'] < data_comparacao:
            df_sf.at[index, 'Valor Frete Pedido'] = row['Valor Frete Pedido'] * 4.841304
        elif row['Moeda'] == 'USD' and row['Data de criação'] >= data_comparacao:
            df_sf.at[index, 'Valor Frete Pedido'] = row['Valor Frete Pedido'] * 5.24160
        else:
            df_sf.at[index, 'Valor Frete Pedido'] = row['Valor Frete Pedido']
    
    df_sf = df_sf.loc[:, ['Contrato Venda', 'Valor Frete Pedido']]
    
    df_sf = df_sf[df_sf['Valor Frete Pedido'] > 0]
    
    df_sf = df_sf.groupby(by=[
        'Contrato Venda'], as_index=False, dropna=False).agg({'Valor Frete Pedido': 'mean'})
    
    df_sf.to_csv('Data/Output/Silver/Sales Force/SalesForce.csv',
                 index=False, decimal=',', encoding='latin-1')

    return df_sf