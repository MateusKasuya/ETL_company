from src.DataLake.XML import formar_tabela_xml_cte, cidade_xml

# def test_xml():

#     test_xml = formar_tabela_xml_cte()

#     unique_id_xml = len(
#         test_xml['XML'].unique()) - len(test_xml.index)

#     assert unique_id_xml == 0

def test_cidade_xml():
    
    test_cidade = cidade_xml()

    unique_id_cidade = len(test_cidade.drop_duplicates(
        subset=['Cidade', 'UF'])) - len(test_cidade.index)

    assert unique_id_cidade == 0
