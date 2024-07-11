import pandas as pd
import os
from bs4 import BeautifulSoup
import numpy as np

def formar_tabela_xml_cte():

    path = r'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Input/XML'

    file_list = os.listdir(path)

    df_cte = pd.read_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/XML/fCTE.csv', decimal=',', encoding='latin-1')

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
    
    # CNPJ/CPF Expedidor
    
    cnpj = nested_tag(expedidor, 'CNPJ')
    
    cnpj_tratado = tratar_nested_tag(cnpj, 'CNPJ')
    
    cpf = nested_tag(expedidor, 'CPF')
    
    cpf_tratado = tratar_nested_tag(cpf, 'CPF')
    
    list_cnpj = []
    
    for i in range(len(cnpj_tratado)):
        
        if cnpj_tratado[i] == '':           
            list_cnpj.append(cpf_tratado[i])
        
        else:
            list_cnpj.append(cnpj_tratado[i])
            
    cte['CNPJ/CPF Expedidor'] = list_cnpj

    # Origem Expedidor

    origem_expedidor = nested_tag(expedidor, 'xMun')

    origem_expedidor_tratado = tratar_nested_tag(origem_expedidor, 'xMun')

    cte['Origem Expedidor'] = origem_expedidor_tratado

    cte['Origem Expedidor'] = cte['Origem Expedidor'].str.title()

    # UF Origem Expedidor

    uf_origem_expedidor = nested_tag(expedidor, 'UF')

    uf_origem_expedidor_tratado = tratar_nested_tag(uf_origem_expedidor, 'UF')

    cte['UF Origem Expedidor'] = uf_origem_expedidor_tratado

    cte['UF Origem Expedidor'] = cte['UF Origem Expedidor'].str.upper()
    
    # Remetente

    remetente = appendar_xml_lista('rem')

    nome_remetente = nested_tag(remetente, 'xNome')

    nome_remetente_tratado = tratar_nested_tag(nome_remetente, 'xNome')

    cte['Remetente'] = nome_remetente_tratado

    cte['Remetente'] = cte['Remetente'].str.title()
    
    # CNPJ/CPF Remetente
    
    cnpj = nested_tag(remetente, 'CNPJ')
    
    cnpj_tratado = tratar_nested_tag(cnpj, 'CNPJ')
    
    cpf = nested_tag(remetente, 'CPF')
    
    cpf_tratado = tratar_nested_tag(cpf, 'CPF')
    
    list_cnpj = []
    
    for i in range(len(cnpj_tratado)):
        
        if cnpj_tratado[i] == '':           
            list_cnpj.append(cpf_tratado[i])
        
        else:
            list_cnpj.append(cnpj_tratado[i])
            
    cte['CNPJ/CPF Remetente'] = list_cnpj

    # Origem Remetente

    origem_rementente = nested_tag(remetente, 'xMun')

    origem_remetente_tratado = tratar_nested_tag(origem_rementente, 'xMun')

    cte['Origem Remetente'] = origem_remetente_tratado

    cte['Origem Remetente'] = cte['Origem Remetente'].str.title()

    # UF Origem Remetente

    uf_origem_remetente = nested_tag(remetente, 'UF')

    uf_origem_remetente_tratado = tratar_nested_tag(uf_origem_remetente, 'UF')

    cte['UF Origem Remetente'] = uf_origem_remetente_tratado

    cte['UF Origem Remetente'] = cte['UF Origem Remetente'].str.upper()

    # Recebedor

    recebedor = appendar_xml_lista('receb')

    nome_recebedor = nested_tag(recebedor, 'xNome')

    nome_recebedor_tratado = tratar_nested_tag(nome_recebedor, 'xNome')
        
    cte['Recebedor'] = nome_recebedor_tratado

    cte['Recebedor'] = cte['Recebedor'].str.title()
    
    # CNPJ/CPF Recebedor
    
    cnpj = nested_tag(recebedor, 'CNPJ')
    
    cnpj_tratado = tratar_nested_tag(cnpj, 'CNPJ')
    
    cpf = nested_tag(recebedor, 'CPF')
    
    cpf_tratado = tratar_nested_tag(cpf, 'CPF')
    
    list_cnpj = []
    
    for i in range(len(cnpj_tratado)):
        
        if cnpj_tratado[i] == '':           
            list_cnpj.append(cpf_tratado[i])
        
        else:
            list_cnpj.append(cnpj_tratado[i])
            
    cte['CNPJ/CPF Recebedor'] = list_cnpj

    # Destino Recebedor

    destino_recebedor = nested_tag(recebedor, 'xMun')

    destino_recebedor_tratado = tratar_nested_tag(destino_recebedor, 'xMun')

    cte['Destino Recebedor'] = destino_recebedor_tratado

    cte['Destino Recebedor'] = cte['Destino Recebedor'].str.title()

    # UF Destino Recebedor
    
    uf_destino_recebedor = nested_tag(recebedor, 'UF')

    uf_destino_recebedor_tratado = tratar_nested_tag(uf_destino_recebedor, 'UF')

    cte['UF Destino Recebedor'] = uf_destino_recebedor_tratado

    cte['UF Destino Recebedor'] = cte['UF Destino Recebedor'].str.upper()

    # Destinatário

    destinatario = appendar_xml_lista('dest')

    nome_destinatario = nested_tag(destinatario, 'xNome')

    nome_destinatario_tratado = tratar_nested_tag(nome_destinatario, 'xNome')
        
    cte['Destinatário'] = nome_destinatario_tratado

    cte['Destinatário'] = cte['Destinatário'].str.title()
    
    # CNPJ/CPF Destinatário
    
    cnpj = nested_tag(destinatario, 'CNPJ')
    
    cnpj_tratado = tratar_nested_tag(cnpj, 'CNPJ')
    
    cpf = nested_tag(destinatario, 'CPF')
    
    cpf_tratado = tratar_nested_tag(cpf, 'CPF')
    
    list_cnpj = []
    
    for i in range(len(cnpj_tratado)):
        
        if cnpj_tratado[i] == '':           
            list_cnpj.append(cpf_tratado[i])
        
        else:
            list_cnpj.append(cnpj_tratado[i])
            
    cte['CNPJ/CPF Destinatário'] = list_cnpj

    # Destino Destinatário

    destino_destinatario = nested_tag(destinatario, 'xMun')

    destino_destinatario_tratado = tratar_nested_tag(destino_destinatario, 'xMun')

    cte['Destino Destinatário'] = destino_destinatario_tratado

    cte['Destino Destinatário'] = cte['Destino Destinatário'].str.title()

    # UF Destino Destinatário
    
    uf_destino_destinatario = nested_tag(destinatario, 'UF')

    uf_destino_destinatario_tratado = tratar_nested_tag(uf_destino_destinatario, 'UF')

    cte['UF Destino Destinatário'] = uf_destino_destinatario_tratado

    cte['UF Destino Destinatário'] = cte['UF Destino Destinatário'].str.upper()

    # Transportadora

    emissor = appendar_xml_lista('emit')

    transportadora = nested_tag(emissor, 'xNome')

    transportadora_tratado = tratar_nested_tag(transportadora, 'xNome')

    cte['Transportadora'] = transportadora_tratado

    cte['Transportadora'] = cte['Transportadora'].str.title()
    
    # CNPJ Transportadora

    cnpj_transportadora = nested_tag(emissor, 'CNPJ')

    cnpj_transportadora_tratado = tratar_nested_tag(cnpj_transportadora, 'CNPJ')

    cte['CNPJ Transportadora'] = cnpj_transportadora_tratado

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
    
    # Valor Imposto
    
    imposto = appendar_xml_lista('vTotTrib')
    
    imposto_tratado = tratar_nested_tag(imposto, 'vTotTrib')
    
    icms = appendar_xml_lista('vICMS')
    
    icms_tratado = tratar_nested_tag(icms, 'vICMS')
    
    list_imposto = []
    
    for i in range(len(imposto_tratado)):
        
        if imposto_tratado[i] == '':           
            list_imposto.append(icms_tratado[i])
        
        else:
            list_imposto.append(imposto_tratado[i])
            
    cte['Valor Imposto'] = list_imposto

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
    
    cte_final['Valor Imposto'] = cte_final['Valor Imposto'].replace('', np.nan)
    
    cte_final['Valor Imposto'] = cte_final['Valor Imposto'].astype(float)
    
    cte_final['Valor Frete s/ Imposto'] = cte_final['Valor Frete Total'] - cte_final['Valor Imposto']
    
    cte_final['Peso Volume'] = cte_final['Peso Volume'].replace('', np.nan)
    
    cte_final['Peso Volume'] = cte_final['Peso Volume'].astype(float)
    
    cte_final['Tipo CTE'] = cte_final['Tipo CTE'].replace('', np.nan)
    
    cte_final['Tipo CTE'] = cte_final['Tipo CTE'].astype(float)
    
    cte_final.drop_duplicates(inplace = True)

    cte_final.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/XML/fCTE.csv',
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
        'C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/XML/fCTE.csv', decimal=',', encoding='latin-1')

    origem_exp = df_cte.loc[:, ['Origem Expedidor', 'UF Origem Expedidor']]

    origem_exp.rename(columns={'Origem Expedidor': 'Cidade',
                  'UF Origem Expedidor': 'UF'}, inplace=True)
    
    origem_rem = df_cte.loc[:, ['Origem Remetente', 'UF Origem Remetente']]

    origem_rem.rename(columns={'Origem Remetente': 'Cidade',
                  'UF Origem Remetente': 'UF'}, inplace=True)
    
    destino_rec = df_cte.loc[:, ['Destino Recebedor', 'UF Destino Recebedor']]

    destino_rec.rename(columns={'Destino Recebedor': 'Cidade',
                   'UF Destino Recebedor': 'UF'}, inplace=True)
    
    destino_des = df_cte.loc[:, ['Destino Destinatário', 'UF Destino Destinatário']]

    destino_des.rename(columns={'Destino Destinatário': 'Cidade',
                   'UF Destino Destinatário': 'UF'}, inplace=True)

    cidade = pd.concat([origem_exp, origem_rem, destino_rec, destino_des], axis=0)

    cidade.drop_duplicates(inplace=True)

    cidade.dropna(inplace=True)

    cidade.to_csv('C:/Users/O1000246/BUNGE/Dados Supply Origeo - Documentos/Projeto_Dados/Data/Output/Silver/XML/dcidade.csv',
                  index=False, decimal=',', encoding='latin-1')

    return cidade
