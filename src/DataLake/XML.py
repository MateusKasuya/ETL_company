import pandas as pd
import os
from bs4 import BeautifulSoup
import numpy as np

def formar_tabela_xml_cte():

    path = r'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/XML'

    file_list = os.listdir(path)

    df_cte = pd.read_csv(
        'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/XML/fCTE.csv', decimal=',', encoding='latin-1')

    # Funções

    def appendar_xml_lista(tag=str):

        lista_xml = []

        for file in file_list:

            file_path = os.path.join(path, file)

            with open(file_path, encoding='utf-8') as f:

                data = f.read()

                soup = BeautifulSoup(data, 'xml')

                var = soup.find_all(tag)

                lista_xml.append(var)

        return lista_xml

    def nested_tag(lista_xml, nest_tag=str):

        lista_xml_conteudo = []

        for xml in lista_xml:

            if xml:

                for conteudo in xml:

                    sub_conteudo = conteudo.find_all(nest_tag)

                    lista_xml_conteudo.append(sub_conteudo)

            else:

                lista_xml_conteudo.append([])

        return lista_xml_conteudo

    def tratar_nested_tag(lista_xml_conteudo, nest_tag=str):

        lista_xml_conteudo = str(lista_xml_conteudo)

        lista_xml_conteudo = lista_xml_conteudo.split('], [')

        lista_xml_conteudo = [i.replace(nest_tag, '')
                              for i in lista_xml_conteudo]

        lista_xml_conteudo = [i.replace('<', '') for i in lista_xml_conteudo]

        lista_xml_conteudo = [i.replace('>', '') for i in lista_xml_conteudo]

        lista_xml_conteudo = [i.replace('/', '') for i in lista_xml_conteudo]

        lista_xml_conteudo = [i.replace('[', '') for i in lista_xml_conteudo]

        lista_xml_conteudo = [i.replace(']', '') for i in lista_xml_conteudo]

        return lista_xml_conteudo

    # Separando CTE de NFE

    separar_cte = appendar_xml_lista('CTe')

    separar_cte = str(separar_cte)

    separar_cte = separar_cte.split('], [')

    lista_zip = list(zip(file_list, separar_cte))

    lista_zip = [(fl, sc) for fl, sc in lista_zip if len(sc) > 0]

    file_list, separar_cte = zip(*lista_zip)

    # Criando DataFrame

    cte = pd.DataFrame()

    # XML

    cte['XML'] = file_list

    # Expedidor

    expedidor = appendar_xml_lista('exped')

    nome_expedidor = nested_tag(expedidor, 'xNome')

    nome_expedidor_tratado = tratar_nested_tag(nome_expedidor, 'xNome')

    cte['Expedidor'] = nome_expedidor_tratado

    cte['Expedidor'] = cte['Expedidor'].str.title()

    # Origem

    origem = nested_tag(expedidor, 'xMun')

    origem_tratado = tratar_nested_tag(origem, 'xMun')

    cte['Origem'] = origem_tratado

    cte['Origem'] = cte['Origem'].str.title()

    # UF Origem

    uf_origem = nested_tag(expedidor, 'UF')

    uf_origem_tratado = tratar_nested_tag(uf_origem, 'UF')

    cte['UF Origem'] = uf_origem_tratado

    cte['UF Origem'] = cte['UF Origem'].str.upper()

    # Recebedor

    recebedor = appendar_xml_lista('receb')

    nome_recebedor = nested_tag(recebedor, 'xNome')

    nome_recebedor_tratado = tratar_nested_tag(nome_recebedor, 'xNome')

    cte['Recebedor'] = nome_recebedor_tratado

    cte['Recebedor'] = cte['Recebedor'].str.title()

    # Destino

    destino = nested_tag(recebedor, 'xMun')

    destino_tratado = tratar_nested_tag(destino, 'xMun')

    cte['Destino'] = destino_tratado

    cte['Destino'] = cte['Destino'].str.title()

    # UF Destino

    uf_destino = nested_tag(recebedor, 'UF')

    uf_destino_tratado = tratar_nested_tag(uf_destino, 'UF')

    cte['UF Destino'] = uf_destino_tratado

    cte['UF Destino'] = cte['UF Destino'].str.upper()

    # Transportadora

    emissor = appendar_xml_lista('emit')

    transportadora = nested_tag(emissor, 'xNome')

    transportadora_tratado = tratar_nested_tag(transportadora, 'xNome')

    cte['Transportadora'] = transportadora_tratado

    cte['Transportadora'] = cte['Transportadora'].str.title()

    # Data Emissão

    data_emissao = appendar_xml_lista('dhEmi')

    data_emissao_tratado = tratar_nested_tag(data_emissao, 'dhEmi')

    cte['Data'] = data_emissao_tratado

    cte['Data'] = [i.split('T') for i in cte['Data']]

    cte['Data'] = [i[0] for i in cte['Data']]

    cte['Data'] = pd.to_datetime(cte['Data'])

    # Chave NF

    chave_nf = appendar_xml_lista('chave')

    chave_nf_tratado = tratar_nested_tag(chave_nf, 'chave')

    cte['Chave NF'] = chave_nf_tratado

    # NF

    list_nf = []

    for i in cte['Chave NF']:

        if i == '':

            list_nf.append(i)

        elif i[28:34][0] == '0':

            list_nf.append(i[29:34])

        else:

            list_nf.append(i[28:34])

    cte['NF'] = list_nf

    cte['NF'] = cte['NF'].str.lstrip('0')

    # CTE

    numero_cte = appendar_xml_lista('nCT')

    numero_cte_tratado = tratar_nested_tag(numero_cte, 'nCT')

    cte['CTE'] = numero_cte_tratado

    # Peso Volume

    peso_volume = appendar_xml_lista('qCarga')

    peso_volume_tratado = tratar_nested_tag(peso_volume, 'qCarga')

    peso_volume_tratado = [i.split(', ') for i in peso_volume_tratado]

    peso_volume_tratado = [[float(j) if j != '' else j for j in i]
                           for i in peso_volume_tratado]

    peso_volume_tratado = [sorted(i) for i in peso_volume_tratado]

    peso_volume_tratado = [i[-1] if len(i) > 1 else i[0]
                           for i in peso_volume_tratado]

    cte['Peso Volume'] = peso_volume_tratado

    # Valor Frete

    frete = appendar_xml_lista('vRec')

    frete_tratado = tratar_nested_tag(frete, 'vRec')

    cte['Valor Frete Total'] = frete_tratado

    # Produto

    produto = appendar_xml_lista('proPred')

    produto_tratado = tratar_nested_tag(produto, 'proPred')

    cte['Produto'] = produto_tratado
    
    # Tipo CTE
    
    tipo_cte = appendar_xml_lista('tpCTe')
    
    tipo_cte_tratado = tratar_nested_tag(tipo_cte, 'tpCTe')
    
    cte['Tipo CTE'] = tipo_cte_tratado

    # Juntando DF
    
    #  Para quando precisar fazer gambiarra
    # df_cte = pd.DataFrame(columns = cte.columns)

    cte_final = pd.concat([cte, df_cte])

    cte_final['Data'] = pd.to_datetime(cte_final['Data'])
    
    cte_final['Valor Frete Total'] = cte_final['Valor Frete Total'].replace('', np.nan)
    
    cte_final['Valor Frete Total'] = cte_final['Valor Frete Total'].astype(float)
    
    cte_final['Peso Volume'] = cte_final['Peso Volume'].replace('', np.nan)
    
    cte_final['Peso Volume'] = cte_final['Peso Volume'].astype(float)
    
    cte_final['Tipo CTE'] = cte_final['Tipo CTE'].replace('', np.nan)
    
    cte_final['Tipo CTE'] = cte_final['Tipo CTE'].astype(float)
    
    cte_final.drop_duplicates(inplace = True)

    cte_final.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/XML/fCTE.csv',
                     index=False, decimal=',', encoding='latin-1')

    # Excluindo Arquivos

    arquivos = os.listdir(path)

    for arquivo in arquivos:

        caminho_completo = os.path.join(path, arquivo)

        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

    return cte_final

# Tabelas Cidade


def cidade_xml():
    
    # df_cte = formar_tabela_xml_cte()

    df_cte = pd.read_csv(
        'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/XML/fCTE.csv', decimal=',', encoding='latin-1')

    origem = df_cte.loc[:, ['Origem', 'UF Origem']]

    origem.rename(columns={'Origem': 'Cidade',
                  'UF Origem': 'UF'}, inplace=True)
    

    destino = df_cte.loc[:, ['Destino', 'UF Destino']]

    destino.rename(columns={'Destino': 'Cidade',
                   'UF Destino': 'UF'}, inplace=True)

    cidade = pd.concat([origem, destino], axis=0)

    cidade.drop_duplicates(inplace=True)

    cidade.dropna(inplace=True)

    # cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/XML/dcidade.csv',
    #               index=False, decimal=',', encoding='latin-1')

    return cidade
