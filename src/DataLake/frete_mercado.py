import pandas as pd


def frete_mercado():

    # Argus

    file_argus = 'C:\\Users\\O1000246\\BUNGE\\Fornecedores Logistica - Documentos\\Report Argus\\Report Argus Frete.xlsx'

    argus = pd.read_excel(file_argus, sheet_name='Base Argus')

    argus['Fonte'] = 'Argus'

    # Sifreca

    file_sifreca = 'C:\\Users\\O1000246\\BUNGE\\Fornecedores Logistica - Documentos\\Frete Rodoviário\\Reporte Semanal ESALQ - SIFRECA\Sifreca base.xlsx'

    sifreca = pd.read_excel(file_sifreca, sheet_name='Sifreca')

    sifreca.rename(columns={'Frete\xa0(R$/t)': 'Frete R$/ton'}, inplace=True)

    sifreca['Fonte'] = 'Sifreca'

    # Agrinvest

    file_agrinvest = 'C:\\Users\\O1000246\\BUNGE\\Operações Logística - Documentos\\Fertilizantes\\2. Contratação de Transporte - FERT - NOVO.xlsx'

    agrinvest = pd.read_excel(file_agrinvest, sheet_name='Agrinvest')

    colunas_agrinvest = {
        'Data Report': 'Data',
        'Cidade Origem': 'Origem',
        'Cidade Destino': 'Destino',
        'Frete BRL/ton': 'Frete R$/ton'
    }

    agrinvest.rename(columns=colunas_agrinvest, inplace=True)

    agrinvest.drop(['Análise Semana Anterior'], axis=1, inplace=True)

    agrinvest['Fonte'] = 'Agrinvest'

    # Mercado

    mercado = pd.concat([argus, sifreca, agrinvest], axis=0)

    mercado.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Frete Mercado/ffrete_mercado.csv',
                   index=False, decimal=',', encoding='latin-1')

    return mercado


def cidade_mercado():

    mercado = frete_mercado()

    origem = mercado.loc[:, ['Origem', 'UF Origem']]

    origem.rename(columns={'Origem': 'Cidade',
                  'UF Origem': 'UF'}, inplace=True)

    destino = mercado.loc[:, ['Destino', 'UF Destino']]

    destino.rename(columns={'Destino': 'Cidade',
                   'UF Destino': 'UF'}, inplace=True)

    cidade = pd.concat([origem, destino], axis=0)

    cidade.drop_duplicates(inplace=True)

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Frete Mercado/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade
