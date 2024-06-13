from src.Gold.BEX import fazer_de_para_cidade_sap_ibge, formar_tabela_cliente_gold, formar_tabela_contrato_gold, formar_tabela_local_expedicao_gold

def test_cidade_sap_gold():

    test_cidade_sap = fazer_de_para_cidade_sap_ibge()

    unique_id_cidade_sap = len(test_cidade_sap.drop_duplicates(
        subset=['Cidade', 'UF'])) - len(test_cidade_sap.index)
    
    assert unique_id_cidade_sap == 0
    
    
def test_cliente_gold():

    cliente = formar_tabela_cliente_gold()
    
    max_value = max(cliente['Id'].value_counts())
    
    assert max_value == 1
    
    
def test_contrato_gold():
    
    contrato = formar_tabela_contrato_gold()

    unique_id_contrato = len(contrato.drop_duplicates(
        subset=['Contrato Venda', 'Item Contrato'])) - len(contrato.index)
    
    assert unique_id_contrato == 0


def test_local_exp_gold():

    local_exp = formar_tabela_local_expedicao_gold()
    
    max_value = max(local_exp['Id'].value_counts())
        
    assert max_value == 1
