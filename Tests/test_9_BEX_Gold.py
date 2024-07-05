from src.Gold.BEX import fazer_de_para_cidade_sap_ibge, formar_tabela_cliente_gold, formar_tabela_contrato_gold, formar_tabela_local_expedicao_gold, formar_tabela_dt_gold, formar_tabela_ov_gold, formar_tabela_transf_gold, formar_tabela_nf_gold
import pandas as pd


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


def test_ov_gold():

    ov = formar_tabela_ov_gold()

    max_value = max(ov['OV-Item'].value_counts())

    assert max_value == 1
    
def test_nf_gold():
    
    nf = formar_tabela_nf_gold()
    
    sum_nf = sum(nf['Valor'])

    assert sum_nf > 0


def test_dt_gold():

    test_dt = formar_tabela_dt_gold()

    unique_id_dt = len(test_dt.drop_duplicates(
        subset=['DT', 'Remessa', 'Item Rem'])) - len(test_dt.index)

    assert unique_id_dt == 0


def test_transf_gold():

    test_transf = formar_tabela_transf_gold()

    assert pd.api.types.is_datetime64_any_dtype(test_transf['Data']) == True
