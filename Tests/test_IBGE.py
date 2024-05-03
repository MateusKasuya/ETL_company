from src.DataLake.IBGE import *


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
