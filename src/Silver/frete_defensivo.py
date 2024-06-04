import pandas as pd


def frete_defensivo():


    file = 'C:\\Users\\O1000246\\BUNGE\\Dados Supply Origeo - Documentos\\Projeto_Dados\\Data\\Input\\Frete Defensivo\\Frete Defensivo.xlsx'
    
    crop = pd.read_excel(file)
    
    crop = pd.melt(crop, id_vars=['Origem', 'UF Origem', 'Destino', 'UF Destino'])
    
    crop.rename(columns={'variable': 'Faixa Peso',
                'value': 'Frete R$/t'}, inplace=True)
    
    crop.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Frete Defensivo/Frete Defensivo.csv',
                index=False, decimal=',', encoding='latin-1')

    return crop
