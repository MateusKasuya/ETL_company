import pandas as pd
# from src.DataLake.IBGE import *

path = 'C:\\Users\\O1000246\\BUNGE\\Dados Supply Origeo - Documentos\\Projeto_Dados\\Data\\Output\\IBGE'

mun = pd.read_csv(path+'\\dmunicipio.csv', decimal=',', encoding='latin-1')
micro = pd.read_csv(path+'\\dmicrorregiao.csv', decimal=',', encoding='latin-1')
meso = pd.read_csv(path+'\\dmesorregiao.csv', decimal=',', encoding='latin-1')
uf = pd.read_csv(path+'\\dUF.csv', decimal=',', encoding='latin-1')



# mun = municipio()
# micro = microrregiao()
# meso = mesorregiao()
# UF = uf()

ibge = mun.merge(micro, left_on = 'Id Microrregião', right_on = 'Id', how = 'inner')

ibge = ibge.merge(meso, left_on = 'Id Mesorregião', right_on = 'Id', how = 'inner')

ibge.rename(columns = {'Id_x' : 'Id Município'}, inplace = True)

ibge = ibge.loc[:, ['Id Município', 'Município', 'Microrregião', 'Mesorregião', 'Id UF']]

ibge = ibge.merge(uf, left_on = 'Id UF', right_on = 'Id', how = 'inner')

ibge = ibge.loc[:, ['Id Município', 'Município', 'Microrregião', 'Mesorregião', 'UF']]

