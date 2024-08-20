import pandas as pd

file_cidade_crop = 'Data/Output/Silver/Frete Defensivo/Cidades Frete Defensivo.csv'
file_ibge = 'Data/Output/Silver/De Para Cidades/de_para_frete_defensivo.csv'

cidade_ibge = pd.read_csv(file_ibge, decimal=',', encoding='latin-1')
cidade_crop = pd.read_csv(file_cidade_crop, decimal=',', encoding='latin-1')

cidade_crop = cidade_crop.merge(cidade_ibge, left_on=['Cidade', 'UF'], right_on=[
                              'De-Cidade', 'De-UF'], how='left')

cidade_crop = cidade_crop.loc[:, ['Cidade', 'UF', 'Para-Cidade']]

cidade_crop.rename(columns={'Para-Cidade': 'Cidade IBGE'}, inplace=True)

file_crop = 'Data/Output/Silver/Frete Defensivo/Frete Defensivo.csv'

crop = pd.read_csv(file_crop, encoding='latin-1', decimal=',')

crop = crop.merge(cidade_crop, left_on=['Origem', 'UF Origem'], right_on=[
                'Cidade', 'UF'], how='left')

crop.drop(['Origem', 'UF', 'Cidade'], axis=1, inplace=True)
crop.rename(columns={'Cidade IBGE': 'Origem'}, inplace=True)

crop = crop.merge(cidade_crop, left_on=['Destino', 'UF Destino'], right_on=[
                'Cidade', 'UF'], how='left')

crop.drop(['Destino', 'UF', 'Cidade'], axis=1, inplace=True)
crop.rename(columns={'Cidade IBGE': 'Destino'}, inplace=True)

crop = crop.loc[:, ['Origem', 'UF Origem', 'Destino', 'UF Destino', 'Faixa Peso', 'Frete R$/t']]

crop.to_excel('Data/Output/Gold/Frete Defensivo.xlsx', index = False)
