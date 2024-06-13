from src.Gold.XML import formar_tabela_cidade_cte_gold, formar_tabela_cte_gold

def test_cte_gold():

    test_cte = formar_tabela_cte_gold()

    unique_id_xml = len(
        test_cte['XML'].unique()) - len(test_cte.index)

    assert unique_id_xml == 0

def test_cidade_gold():
    
    test_cidade = formar_tabela_cidade_cte_gold()

    unique_id_cidade = len(test_cidade.drop_duplicates(
        subset=['Cidade', 'UF'])) - len(test_cidade.index)

    assert unique_id_cidade == 0