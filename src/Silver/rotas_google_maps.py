import googlemaps
import pandas as pd
from src.DataLake.IBGE import municipio, microrregiao, mesorregiao, uf
from dotenv import load_dotenv
import os


def rota_google_maps():

    load_dotenv('.env')

    KEY_GOOGLE_MAPS = os.getenv('KEY_GOOGLE_MAPS')

    file_fert = 'Data/Input/Google Maps/rotas_fert.parquet'
    file_seed = 'Data/Input/Google Maps/rotas_semente.parquet'

    fert = pd.read_parquet(file_fert)
    seed = pd.read_parquet(file_seed)
    
    fert.rename(columns = {'Dist.' : 'Dist'}, inplace = True)
    seed.rename(columns = {'Dist.' : 'Dist'}, inplace = True)

    municipio_ibge = municipio()
    microrregiao_ibge = microrregiao()
    mesorregiao_ibge = mesorregiao()
    uf_ibge = uf()

    ibge = municipio_ibge.merge(
        microrregiao_ibge, left_on='Id Microrregião', right_on='Id', how='inner')

    ibge = ibge.merge(mesorregiao_ibge, left_on='Id Mesorregião',
                      right_on='Id', how='inner')

    ibge = ibge.loc[:, ['Município', 'Id UF']]

    ibge = ibge.merge(uf_ibge, left_on='Id UF', right_on='Id', how='inner')

    ibge['Município-UF'] = ibge['Município'] + '-' + ibge['UF']

    list_origem = [
        'DIAMANTINO-MT',
    ]

    list_destino = list(ibge['Município-UF'])

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

    ufs_brasil = {
        'State of Acre': 'AC',
        'State of Alagoas': 'AL',
        'State of Amapá': 'AP',
        'State of Amazonas': 'AM',
        'State of Bahia': 'BA',
        'State of Ceará': 'CE',
        'State of Distrito Federal': 'DF',
        'State of Espírito Santo': 'ES',
        'State of Goiás': 'GO',
        'State of Maranhão': 'MA',
        'State of Mato Grosso': 'MT',
        'State of Mato Grosso do Sul': 'MS',
        'State of Minas Gerais': 'MG',
        'State of Pará': 'PA',
        'State of Paraíba': 'PB',
        'State of Paraná': 'PR',
        'State of Pernambuco': 'PE',
        'State of Piauí': 'PI',
        'State of Rio de Janeiro': 'RJ',
        'State of Rio Grande do Norte': 'RN',
        'State of Rio Grande do Sul': 'RS',
        'State of Rondônia': 'RO',
        'State of Roraima': 'RR',
        'State of Santa Catarina': 'SC',
        'State of São Paulo': 'SP',
        'State of Sergipe': 'SE',
        'State of Tocantins': 'TO'
    }

    rota_gm['UF Origem'] = rota_gm['UF Origem'].str.split(',')
    rota_gm['UF Origem'] = rota_gm['UF Origem'].apply(lambda x: x[1])
    rota_gm['UF Origem'] = rota_gm['UF Origem'].str.strip()
    rota_gm['UF Origem'] = rota_gm['UF Origem'].map(ufs_brasil)

    rota_gm['UF Destino'] = rota_gm['UF Destino'].str.split(',')
    rota_gm['UF Destino'] = rota_gm['UF Destino'].apply(lambda x: x[1])
    rota_gm['UF Destino'] = rota_gm['UF Destino'].str.strip()
    rota_gm['UF Destino'] = rota_gm['UF Destino'].map(ufs_brasil)

    rota_geral = pd.concat([rota_gm, fert, seed], axis=0)
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
