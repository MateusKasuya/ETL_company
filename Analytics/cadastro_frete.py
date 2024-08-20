import pandas as pd
import math

ov = pd.read_excel('Data/Output/Gold/Ordem de Venda.xlsx')

ov = ov[~ov['Id Itinerário'].isna()]

colunas_ov = [
    'Id Centro',
    'Grupo de Mercadorias',
    'Id Itinerário',    
    'Origem',
    'UF Origem',
    'Destino',
    'UF Destino'
    ]

ov = ov.loc[:, colunas_ov]

ov.drop_duplicates(inplace = True)

ov.dropna(inplace = True)

ov['Origem'] = ov['Origem'].str.title()
ov['Destino'] = ov['Destino'].str.title()

map_mercadoria = {
    'Fertilizantes Outros' : 'Z035',
    'Defensor Agri Outros' : 'Z055',
    'Sementes - Outros' : 'Z057'
    }

ov['Grupo de Mercadorias'] = ov['Grupo de Mercadorias'].map(map_mercadoria)

ov_fert = ov[ov['Grupo de Mercadorias'] == 'Z035']
ov_def = ov[ov['Grupo de Mercadorias'] == 'Z055']
ov_seed = ov[ov['Grupo de Mercadorias'] == 'Z057']


file_sim_fert = r'C:\\Users\\O1000246\\BUNGE\\Fornecedores Logistica - Documentos\\Frete Rodoviário\\Transporte Rodoviário - Lista Frete\\Fertilizantes\\Simulacao_Frete.xlsx'

sim_fert = pd.read_excel(file_sim_fert)

sim_fert = sim_fert[sim_fert['Mês'] == 'jul/24']

sim_fert = sim_fert.loc[:, ['Origem', 'UF Origem', 'Destino', 'UF Destino', 'Frete']]

sim_fert['Origem'] = sim_fert['Origem'].str.title()
sim_fert['Destino'] = sim_fert['Destino'].str.title()

ov_fert = ov_fert.merge(sim_fert, on = ['Origem', 'UF Origem', 'Destino', 'UF Destino'], how = 'left')

ov_fert.to_excel('Analytics/ov_fert.xlsx', index = False)


file_frete_def = 'Data/Output/Gold/Frete Defensivo.xlsx'

crop = pd.read_excel(file_frete_def)

ov_def = ov_def.merge(crop, on = ['Origem', 'UF Origem', 'Destino', 'UF Destino'], how = 'left')

ov_def.dropna(inplace = True)

map_faixa_peso = {
    '500' : '0,000001'  ,         
   '500-1000'   : '0,5'    ,
    '1000-2000'   : '1',
    '2000-4000'     : '2',
    '4000-6000'      : '4',
    '6000-9000'      : '6',
    '9000-13000'     : '9',
    '13000-25000'    : '13',
    '> 25000'   : '25'
    }

ov_def['Faixa Peso'] = ov_def['Faixa Peso'].map(map_faixa_peso)

ov_def.to_excel('Analytics/ov_def.xlsx', index = False)


file_frete_seed = 'Data/Input/Frete/Frete Semente/Frete_Sementes.xlsx'

seed = pd.read_excel(file_frete_seed)

file_itinerario = 'Data/Output/Gold/Itinerário.xlsx'

itinerario = pd.read_excel(file_itinerario)

itinerario.drop(['Itinerário'], axis = 1, inplace = True)

itinerario['Distância KM'] = itinerario['Distância KM'].astype(float)

ov_seed = ov_seed.merge(itinerario, left_on = 'Id Itinerário', right_on = 'Id', how = 'left')

ov_seed.drop(['Id'], axis = 1, inplace = True)

seed = seed.loc[:, ['Até (Km)', 'Média']]

seed['Fator'] = seed['Até (Km)'] / 50

ov_seed['Fator'] = ov_seed['Distância KM'].apply(lambda x: math.ceil(x / 50))

ov_seed = ov_seed.merge(seed, on = 'Fator', how = 'left')

ov_seed.drop(columns = ['Distância KM', 'Fator', 'Até (Km)'], axis = 1, inplace = True)

ov_seed.to_excel('Analytics/ov_seed.xlsx', index = False)







