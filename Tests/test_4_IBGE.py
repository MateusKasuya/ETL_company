from src.Silver.IBGE import *
from src.Gold.IBGE import consolidar_cidades_IBGE


def test_municipio():

    test_municipio = municipio()

    unique_id_municipio = len(
        test_municipio['Id'].unique()) - len(test_municipio.index)

    assert unique_id_municipio == 0


def test_micro():

    test_micro = microrregiao()

    unique_id_micro = len(
        test_micro['Id'].unique()) - len(test_micro.index)

    assert unique_id_micro == 0


def test_meso():

    test_meso = mesorregiao()

    unique_id_meso = len(
        test_meso['Id'].unique()) - len(test_meso.index)

    assert unique_id_meso == 0


def test_uf():

    test_uf = uf()

    unique_id_uf = len(
        test_uf['Id'].unique()) - len(test_uf.index)

    assert unique_id_uf == 0


def test_regiao():

    test_regiao = regiao()

    unique_id_regiao = len(
        test_regiao['Id'].unique()) - len(test_regiao.index)

    assert unique_id_regiao == 0

def test_consolidado_IBGE():
    
    test_IBGE = consolidar_cidades_IBGE()
    
    max_value_count = max(test_IBGE['Id Município'].value_counts())
    
    assert max_value_count == 1
    
    