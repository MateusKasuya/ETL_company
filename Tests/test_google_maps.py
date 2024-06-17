# from src.DataLake.rotas_google_maps import rota_google_maps, cidade_google_maps


# # def test_rota_google_maps():

# #     test_rota_google_maps = rota_google_maps()

# #     unique_id_rota_google_maps = len(test_rota_google_maps.drop_duplicates(
# #         subset=['Origem', 'UF Origem', 'Destino', 'UF Destino'])) - len(test_rota_google_maps.index)

# #     assert unique_id_rota_google_maps == 0


# def test_cidade_google_maps():

#     test_cidade_google_maps = cidade_google_maps()

#     unique_id_cidade = len(test_cidade_google_maps.drop_duplicates(
#         subset=['Cidade', 'UF'])) - len(test_cidade_google_maps.index)

#     assert unique_id_cidade == 0


def test_test():
    assert 1 == 1
