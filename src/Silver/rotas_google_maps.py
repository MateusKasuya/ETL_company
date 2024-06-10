import googlemaps
import pandas as pd
# from src.Silver.IBGE import municipio, microrregiao, mesorregiao, uf
from dotenv import load_dotenv
import os
import numpy as np


def rota_google_maps():

    load_dotenv('.env')

    KEY_GOOGLE_MAPS = os.getenv('KEY_GOOGLE_MAPS')

    file_fert = 'Data/Input/Google Maps/rotas_fert.parquet'
    file_seed = 'Data/Input/Google Maps/rotas_semente.parquet'

    fert = pd.read_parquet(file_fert)
    seed = pd.read_parquet(file_seed)
    
    fert.rename(columns = {'Dist.' : 'Dist'}, inplace = True)
    seed.rename(columns = {'Dist.' : 'Dist'}, inplace = True)

    # municipio_ibge = municipio()
    # microrregiao_ibge = microrregiao()
    # mesorregiao_ibge = mesorregiao()
    # uf_ibge = uf()

    # ibge = municipio_ibge.merge(
    #     microrregiao_ibge, left_on='Id Microrregião', right_on='Id', how='inner')

    # ibge = ibge.merge(mesorregiao_ibge, left_on='Id Mesorregião',
    #                   right_on='Id', how='inner')

    # ibge = ibge.loc[:, ['Município', 'Id UF']]

    # ibge = ibge.merge(uf_ibge, left_on='Id UF', right_on='Id', how='inner')

    # ibge['Município-UF'] = ibge['Município'] + '-' + ibge['UF']

    list_origem = [
        'RUA NEUSA RIBEIRO, SNº, CHÁCARA SUL REF: CLUBE LAGOA DA ILHA LAGOA DA ILHA, Lagoa da Confusão - TO, 77493-000',
    ]
    
    list_destino = [
       # 'RUA NEUSA RIBEIRO, SNº, CHÁCARA SUL REF: CLUBE LAGOA DA ILHA LAGOA DA ILHA, Lagoa da Confusão - TO, 77493-000' 
'DIVINOPOLIS DO TOCANTINS	TO 77670-000',
'SAO RAIMUNDO DAS MANGABEIRAS	MA 65840-000',
'BARREIRAS	BA',
'BALSAS	MA 65800-000',
'MURICILANDIA	TO 77850-000',
'ALMAS	TO 77310-000',
'PIUM	TO 77570-000',
'TUPIRAMA	TO 77704-000',
'WANDERLANDIA	TO 77860-000',
'ALVORADA	TO 77480-000',
'MATEIROS	TO 77593-000',
'PIRAQUE	TO 77888-000',
'TALISMA	TO 77483-000',
'TASSO FRAGOSO	MA 65820-000',
'PEIXE	TO 77460-000',
'PEDRO AFONSO	TO 77710-000',
'SONORA	MS 79415-000',
'JABORANDI	BA 47655-000',
'ALTO PARNAIBA	MA',
'BARRA DO OURO	TO 77765-000',
'SALVADOR	BA',
'BARREIRAS DO PIAUI PI 64990-000',
'BREJO	 MA 65520-000',
'BURITI	MA 65515-000',
'BURITICUPU	MA 65393-000',
'CAROLINA	MA 65980-000',
'CAXIAS	MA',
'CRISTALANDIA	TO 77490-000',
'FORTUNA	MA 65695-000',
'GOVERNADOR EUGENIO BARROS	MA 65780-000',
'LAGOA DO TOCANTINS	TO 77613-000',
'LORETO	MA 65895-000',
'MAGALHAES DE ALMEIDA	MA',
'MARIANOPOLIS DO TOCANTINS	TO 77675-000',
'MATA ROMA	MA 65510-000',
'MIRADOR	MA 65850-000',
'MIRANORTE	TO 77660-000',
'MONTE ALEGRE DO PIAUI	PI 64940-000',
'MONTE DO CARMO	TO 77585-000',
'NOVA IORQUE	MA 65880-000',
'NOVA ROSALANDIA	TO 77495-000',
'PALMAS	TO',
'PALMEIRA DO PIAUI	PI 64925-000',
'PARAGOMINAS	PA',
'REGENERACAO	PI 64490-000',
'RIACHAO	MA 65990-000',
'SAMBAIBA	MA 65830-000',
'SANTA MARIA DAS BARREIRAS	PA 68565-000',
'SANTA ROSA DO TOCANTINS	TO 77375-000',
'SANTANA DO ARAGUAIA	PA 68560-000',
'SAO DOMINGOS DO AZEITAO	MA 65888-000',
'SAO FELIX DE BALSAS	MA 65890-000',
'SEBASTIAO LEAL	PI 64873-000',
'SILVANOPOLIS	TO 77580-000' ,
'MOJU	PA 68450-000',
'URUCUI	PI 64860-000',
'VILA NOVA DOS MARTIRIOS	MA 65924-000',
'PALMEIRANTE	TO 77798-000',
'PORTO FRANCO	MA 65970-000',
'RIBEIRAO CASCALHEIRA	MT 78675-000',
'RIO SONO	TO 77635-000',
'BRASILIA	DF',
'NOVA MARINGA	MT 78440-000',
'SANTA MARIA DO TOCANTINS	TO 77716-000',
'XAMBIOA	TO 77880-000',
'FATIMA	TO 77555-000'
    ]

    # list_destino = list(ibge['Município-UF'])

    gmaps = googlemaps.Client(key=KEY_GOOGLE_MAPS)

    list_dest = []
    list_orig = []
    list_km = []
    for c_origem in list_origem:
        for c_destino in list_destino:
            try:
                consulta = gmaps.distance_matrix(c_origem, c_destino)
                dest = consulta['destination_addresses'][0]
                orig = consulta['origin_addresses'][0]
                km = consulta['rows'][0]['elements'][0]['distance']['value']
                list_dest.append(dest)
                list_orig.append(orig)
                list_km.append(km)
            except:
                consulta = gmaps.distance_matrix(c_origem, c_destino)
                dest = consulta['destination_addresses'][0]
                orig = consulta['origin_addresses'][0]
                km = ''
                list_dest.append(dest)
                list_orig.append(orig)
                list_km.append(km)

    rota_gm = pd.DataFrame()

    rota_gm['Origem'] = list_orig
    rota_gm['UF Origem'] = list_orig
    rota_gm['Destino'] = list_dest
    rota_gm['UF Destino'] = list_dest
    rota_gm['Dist'] = list_km

    rota_gm.dropna(subset=['Dist'], inplace=True)

    rota_gm = rota_gm[rota_gm['Dist'] != '']

    rota_gm['Dist'] = rota_gm['Dist'].astype(int)

    rota_gm.drop_duplicates(inplace=True)

    rota_gm['Dist'] = rota_gm['Dist'] / 1000
    rota_gm['Dist'] = rota_gm['Dist'].round(0)

    rota_gm['Origem'] = rota_gm['Origem'].str.split(',')
    rota_gm['Origem'] = rota_gm['Origem'].apply(lambda x: x[0])
    rota_gm['Origem'] = rota_gm['Origem'].str.split(' - ')
    rota_gm['Origem'] = rota_gm['Origem'].apply(lambda x: x[0])

    rota_gm['Destino'] = rota_gm['Destino'].str.split(',')
    rota_gm['Destino'] = rota_gm['Destino'].apply(lambda x: x[0])
    rota_gm['Destino'] = rota_gm['Destino'].str.split(' - ')
    rota_gm['Destino'] = rota_gm['Destino'].apply(lambda x: x[0])
    
    list_uf_origem = []

    for i in rota_gm['UF Origem']:
        if 'RS' in i:
            uf = 'RS'
            list_uf_origem.append(uf)
        elif 'SC' in i:
            uf = 'SC'
            list_uf_origem.append(uf)
        elif 'PR' in i:
            uf = 'PR'
            list_uf_origem.append(uf)
        elif 'SP' in i:
            uf = 'SP'
            list_uf_origem.append(uf)
        elif 'MG' in i:
            uf = 'MG'
            list_uf_origem.append(uf)
        elif 'ES' in i:
            uf = 'ES'
            list_uf_origem.append(uf)
        elif 'RJ' in i:
            uf = 'RJ'
            list_uf_origem.append(uf)
        elif 'GO' in i:
            uf = 'GO'
            list_uf_origem.append(uf)
        elif 'DF' in i:
            uf = 'DF'
            list_uf_origem.append(uf)
        elif 'MS' in i:
            uf = 'MS'
            list_uf_origem.append(uf)
        elif 'MT' in i:
            uf = 'MT'
            list_uf_origem.append(uf)
        elif 'AC' in i:
            uf = 'AC'
            list_uf_origem.append(uf)
        elif 'AL' in i:
            uf = 'AL'
            list_uf_origem.append(uf)
        elif 'AM' in i:
            uf = 'AM'
            list_uf_origem.append(uf)
        elif 'AP' in i:
            uf = 'AP'
            list_uf_origem.append(uf)
        elif 'BA' in i:
            uf = 'BA'
            list_uf_origem.append(uf)
        elif 'CE' in i:
            uf = 'CE'
            list_uf_origem.append(uf)
        elif 'MA' in i:
            uf = 'MA'
            list_uf_origem.append(uf)
        elif 'PA' in i:
            uf = 'PA'
            list_uf_origem.append(uf)
        elif 'PB' in i:
            uf = 'PB'
            list_uf_origem.append(uf)
        elif 'PE' in i:
            uf = 'PE'
            list_uf_origem.append(uf)
        elif 'PI' in i:
            uf = 'PI'
            list_uf_origem.append(uf)
        elif 'RN' in i:
            uf = 'RN'
            list_uf_origem.append(uf)
        elif 'RO' in i:
            uf = 'RO'
            list_uf_origem.append(uf)
        elif 'RR' in i:
            uf = 'RR'
            list_uf_origem.append(uf)
        elif 'SE' in i:
            uf = 'SE'
            list_uf_origem.append(uf)
        elif 'TO' in i:
            uf = 'TO'
            list_uf_origem.append(uf)
        elif 'Rio Grande do Sul' in i:
            uf = 'RS'
            list_uf_origem.append(uf)
        elif 'Santa Catarina' in i:
            uf = 'SC'
            list_uf_origem.append(uf)
        elif 'Paraná' in i:
            uf = 'PR'
            list_uf_origem.append(uf)
        elif 'São Paulo' in i:
            uf = 'SP'
            list_uf_origem.append(uf)
        elif 'Minas Gerais' in i:
            uf = 'MG'
            list_uf_origem.append(uf)
        elif 'Espírito Santo' in i:
            uf = 'ES'
            list_uf_origem.append(uf)
        elif 'Rio de Janeiro' in i:
            uf = 'RJ'
            list_uf_origem.append(uf)
        elif 'Goiás' in i:
            uf = 'GO'
            list_uf_origem.append(uf)
        elif 'Federal District' in i:
            uf = 'DF'
            list_uf_origem.append(uf)
        elif 'Mato Grosso do Sul' in i:
            uf = 'MS'
            list_uf_origem.append(uf)
        elif 'Mato Grosso' in i:
            uf = 'MT'
            list_uf_origem.append(uf)
        elif 'Acre' in i:
            uf = 'AC'
            list_uf_origem.append(uf)
        elif 'Alagoas' in i:
            uf = 'AL'
            list_uf_origem.append(uf)
        elif 'Amazonas' in i:
            uf = 'AM'
            list_uf_origem.append(uf)
        elif 'Amapá' in i:
            uf = 'AP'
            list_uf_origem.append(uf)
        elif 'Bahia' in i:
            uf = 'BA'
            list_uf_origem.append(uf)
        elif 'Ceará' in i:
            uf = 'CE'
            list_uf_origem.append(uf)
        elif 'Maranhão' in i:
            uf = 'MA'
            list_uf_origem.append(uf)
        elif 'Pará' in i:
            uf = 'PA'
            list_uf_origem.append(uf)
        elif 'Paraíba' in i:
            uf = 'PB'
            list_uf_origem.append(uf)
        elif 'Pernambuco' in i:
            uf = 'PE'
            list_uf_origem.append(uf)
        elif 'Piauí' in i:
            uf = 'PI'
            list_uf_origem.append(uf)
        elif 'Rio Grande do Norte' in i:
            uf = 'RN'
            list_uf_origem.append(uf)
        elif 'Rondônia' in i:
            uf = 'RO'
            list_uf_origem.append(uf)
        elif 'Roraima' in i:
            uf = 'RR'
            list_uf_origem.append(uf)
        elif 'Sergipe' in i:
            uf = 'SE'
            list_uf_origem.append(uf)
        elif 'Tocantins' in i:
            uf = 'TO'
            list_uf_origem.append(uf)
        else:
            uf = np.nan
            list_uf_origem.append(uf)
    rota_gm['UF Origem'] = list_uf_origem
    list_uf_destino = []
    for i in rota_gm['UF Destino']:
        if 'RS' in i:
            uf = 'RS'
            list_uf_destino.append(uf)
        elif 'SC' in i:
            uf = 'SC'
            list_uf_destino.append(uf)
        elif 'PR' in i:
            uf = 'PR'
            list_uf_destino.append(uf)
        elif 'SP' in i:
            uf = 'SP'
            list_uf_destino.append(uf)
        elif 'MG' in i:
            uf = 'MG'
            list_uf_destino.append(uf)
        elif 'ES' in i:
            uf = 'ES'
            list_uf_destino.append(uf)
        elif 'RJ' in i:
            uf = 'RJ'
            list_uf_destino.append(uf)
        elif 'GO' in i:
            uf = 'GO'
            list_uf_destino.append(uf)
        elif 'DF' in i:
            uf = 'DF'
            list_uf_destino.append(uf)
        elif 'MS' in i:
            uf = 'MS'
            list_uf_destino.append(uf)
        elif 'MT' in i:
            uf = 'MT'
            list_uf_destino.append(uf)
        elif 'AC' in i:
            uf = 'AC'
            list_uf_destino.append(uf)
        elif 'AL' in i:
            uf = 'AL'
            list_uf_destino.append(uf)
        elif 'AM' in i:
            uf = 'AM'
            list_uf_destino.append(uf)
        elif 'AP' in i:
            uf = 'AP'
            list_uf_destino.append(uf)
        elif 'BA' in i:
            uf = 'BA'
            list_uf_destino.append(uf)
        elif 'CE' in i:
            uf = 'CE'
            list_uf_destino.append(uf)
        elif 'MA' in i:
            uf = 'MA'
            list_uf_destino.append(uf)
        elif 'PA' in i:
            uf = 'PA'
            list_uf_destino.append(uf)
        elif 'PB' in i:
            uf = 'PB'
            list_uf_destino.append(uf)
        elif 'PE' in i:
            uf = 'PE'
            list_uf_destino.append(uf)
        elif 'PI' in i:
            uf = 'PI'
            list_uf_destino.append(uf)
        elif 'RN' in i:
            uf = 'RN'
            list_uf_destino.append(uf)
        elif 'RO' in i:
            uf = 'RO'
            list_uf_destino.append(uf)
        elif 'RR' in i:
            uf = 'RR'
            list_uf_destino.append(uf)
        elif 'SE' in i:
            uf = 'SE'
            list_uf_destino.append(uf)
        elif 'TO' in i:
            uf = 'TO'
            list_uf_destino.append(uf)
        elif 'Rio Grande do Sul' in i:
            uf = 'RS'
            list_uf_destino.append(uf)
        elif 'Santa Catarina' in i:
            uf = 'SC'
            list_uf_destino.append(uf)
        elif 'Paraná' in i:
            uf = 'PR'
            list_uf_destino.append(uf)
        elif 'São Paulo' in i:
            uf = 'SP'
            list_uf_destino.append(uf)
        elif 'Minas Gerais' in i:
            uf = 'MG'
            list_uf_destino.append(uf)
        elif 'Espírito Santo' in i:
            uf = 'ES'
            list_uf_destino.append(uf)
        elif 'Rio de Janeiro' in i:
            uf = 'RJ'
            list_uf_destino.append(uf)
        elif 'Goiás' in i:
            uf = 'GO'
            list_uf_destino.append(uf)
        elif 'Federal District' in i:
            uf = 'DF'
            list_uf_destino.append(uf)
        elif 'Mato Grosso do Sul' in i:
            uf = 'MS'
            list_uf_destino.append(uf)
        elif 'Mato Grosso' in i:
            uf = 'MT'
            list_uf_destino.append(uf)
        elif 'Acre' in i:
            uf = 'AC'
            list_uf_destino.append(uf)
        elif 'Alagoas' in i:
            uf = 'AL'
            list_uf_destino.append(uf)
        elif 'Amazonas' in i:
            uf = 'AM'
            list_uf_destino.append(uf)
        elif 'Amapá' in i:
            uf = 'AP'
            list_uf_destino.append(uf)
        elif 'Bahia' in i:
            uf = 'BA'
            list_uf_destino.append(uf)
        elif 'Ceará' in i:
            uf = 'CE'
            list_uf_destino.append(uf)
        elif 'Maranhão' in i:
            uf = 'MA'
            list_uf_destino.append(uf)
        elif 'Pará' in i:
            uf = 'PA'
            list_uf_destino.append(uf)
        elif 'Paraíba' in i:
            uf = 'PB'
            list_uf_destino.append(uf)
        elif 'Pernambuco' in i:
            uf = 'PE'
            list_uf_destino.append(uf)
        elif 'Piauí' in i:
            uf = 'PI'
            list_uf_destino.append(uf)
        elif 'Rio Grande do Norte' in i:
            uf = 'RN'
            list_uf_destino.append(uf)
        elif 'Rondônia' in i:
            uf = 'RO'
            list_uf_destino.append(uf)
        elif 'Roraima' in i:
            uf = 'RR'
            list_uf_destino.append(uf)
        elif 'Sergipe' in i:
            uf = 'SE'
            list_uf_destino.append(uf)
        elif 'Tocantins' in i:
            uf = 'TO'
            list_uf_destino.append(uf)
        else:
            uf = np.nan
            list_uf_destino.append(uf)
    rota_gm['UF Destino'] = list_uf_destino

    # rota_gm['UF Origem'] = rota_gm['UF Origem'].str.split(',')
    # rota_gm['UF Origem'] = rota_gm['UF Origem'].apply(lambda x: x[1])
    # rota_gm['UF Origem'] = rota_gm['UF Origem'].str.strip()


    # rota_gm['UF Destino'] = rota_gm['UF Destino'].str.split(',')
    # rota_gm['UF Destino'] = rota_gm['UF Destino'].apply(lambda x: x[1])
    # rota_gm['UF Destino'] = rota_gm['UF Destino'].str.strip()
    # rota_gm['UF Destino'] = rota_gm['UF Destino'].map(ufs_brasil)
    
    # file_drota = r'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Google Maps/drota.csv'
    # drota = pd.read_csv(file_drota, decimal=',', encoding='latin-1',)
    
    rota_geral = rota_gm[:]

    # rota_geral = pd.concat([rota_gm, fert, seed], axis=0)
    rota_geral.drop_duplicates(inplace=True)

    rota_geral.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Google Maps/drota.csv',
                      index=False, decimal=',', encoding='latin-1')

    return rota_geral


def cidade_google_maps():

    rota_geral = rota_google_maps()

    origem = rota_geral.loc[:, ['Origem', 'UF Origem']]
    origem.rename(columns={'Origem': 'Cidade',
                  'UF Origem': 'UF'}, inplace=True)

    destino = rota_geral.loc[:, ['Destino', 'UF Destino']]
    destino.rename(columns={'Destino': 'Cidade',
                   'UF Destino': 'UF'}, inplace=True)

    cidade = pd.concat([origem, destino], axis=0)
    cidade.drop_duplicates(inplace=True)

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Google Maps/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade
