import pandas as pd

file = 'C:\\Users\\O1000246\\BUNGE\\Dados Supply Origeo - Documentos\\Projeto_Dados\\Data\\Input\\Frete Defensivo\\Frete Defensivo.xlsx'
    
crop = pd.read_excel(file)
    
crop = pd.melt(crop, id_vars=['Origem', 'UF Origem', 'Destino', 'UF Destino'])
    
crop.rename(columns={'variable': 'Faixa Peso',
                'value': 'Frete R$/t'}, inplace=True)
    
crop.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/Frete Defensivo/Frete Defensivo.csv',
                index=False, decimal=',', encoding='latin-1')

crop_origem = crop[['Origem', 'UF Origem']]
crop_origem.drop_duplicates(inplace = True)
crop_origem.rename(columns = {'Origem' : 'Cidade', 'UF Origem': 'UF'}, inplace = True)

crop_destino = crop[['Destino', 'UF Destino']]
crop_destino.drop_duplicates(inplace = True)
crop_destino.rename(columns = {'Destino' : 'Cidade', 'UF Destino': 'UF'}, inplace = True)

crop_cidade = pd.concat([crop_origem, crop_destino], axis = 0)
crop_cidade.drop_duplicates(inplace = True)

crop_cidade.to_csv('Data/Output/Silver/Frete Defensivo/Cidades Frete Defensivo.csv', index = False, decimal = ',', encoding = 'latin-1')
