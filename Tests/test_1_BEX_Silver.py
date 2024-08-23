from src.Silver.BEX import *


def test_centro():

    test_centro = centro()

    unique_id_centro = len(test_centro['Id'].unique()) - len(test_centro.index)

    assert unique_id_centro == 0


def test_cidade():

    test_cidade = cidade()

    unique_id_cidade = len(test_cidade.drop_duplicates(
        subset=['Cidade', 'UF'])) - len(test_cidade.index)

    assert unique_id_cidade == 0


def test_cliente():

    test_cliente = cliente()

    unique_id_cliente = len(
        test_cliente['Id'].unique()) - len(test_cliente.index)

    assert unique_id_cliente == 0


def test_contrato():

    test_contrato = contrato()

    unique_id_contrato = len(test_contrato.drop_duplicates(
        subset=['Contrato Venda', 'Item Contrato'])) - len(test_contrato.index)

    assert unique_id_contrato == 0


# def test_frete_pedido():

#     test_frete_pedido = conta_frete()

#     unique_id_frete_pedido = len(test_frete_pedido.drop_duplicates(
#         subset=['Contrato Venda', 'Item Contrato'])) - len(test_frete_pedido.index)

#     assert unique_id_frete_pedido == 0


def test_itinerario():

    test_itinerario = itinerario()

    unique_id_itinerario = len(
        test_itinerario['Id'].unique()) - len(test_itinerario.index)

    assert unique_id_itinerario == 0


def test_local_exp():

    test_local_exp = local_exp()

    unique_id_local_exp = len(
        test_local_exp['Id'].unique()) - len(test_local_exp.index)

    assert unique_id_local_exp == 0


def test_mot_rec():

    test_mot_rec = motivo_recusa()

    unique_id_mot_rec = len(
        test_mot_rec['Id'].unique()) - len(test_mot_rec.index)

    assert unique_id_mot_rec == 0


def test_ov():

    test_ov = ov()

    unique_id_ov = len(test_ov.drop_duplicates(
        subset=['OV', 'Item OV'])) - len(test_ov.index)

    assert unique_id_ov == 0


def test_produto():

    test_produto = produto()

    unique_id_produto = len(
        test_produto['Id'].unique()) - len(test_produto.index)

    assert unique_id_produto == 0


def test_UF():

    test_UF = uf()

    unique_id_UF = len(test_UF['UF'].unique()) - len(test_UF.index)

    assert unique_id_UF == 0


def test_nf():

    test_nf = nf()

    sum_nf = sum(test_nf['Valor'])

    assert sum_nf > 0


def test_dt():

    test_dt = dt()

    sum_dt = sum(test_dt['Quantidade'])

    assert sum_dt > 0


def test_transf():

    test_transf = transferencia()

    assert pd.api.types.is_datetime64_any_dtype(test_transf['Data']) == True


def test_gerencial_frete():

    test_gerencial_frete = gerencial_frete()

    unique_id_gerencial_frete = len(test_gerencial_frete.drop_duplicates(
        subset=['Documento Contábil',
                'Item Doc Contábil'])) - len(test_gerencial_frete.index)

    assert unique_id_gerencial_frete == 0
    
def test_estoque():
    
    test_estoque = estoque()
    
    sum_estoque = sum(test_estoque['Estoque Livre'])

    assert sum_estoque > 1
