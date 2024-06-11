from src.Silver.de_para_cidades import fazer_de_para_bex, fazer_de_para_cte

def test_cidade_sap_ibge():

    test_cidade_sap = fazer_de_para_bex()

    unique_id_cidade = len(test_cidade_sap.drop_duplicates(
        subset=['De-Cidade', 'De-UF'])) - len(test_cidade_sap.index)

    assert unique_id_cidade == 0
    
def test_cidade_xml():
    
    test_cidade_xml = fazer_de_para_cte()
    
    max_value_count = max(test_cidade_xml['De'].value_counts())

    assert max_value_count == 1
