from src.Gold.Rotas import rotas

def test_rota():
    
    test_rota_gold = rotas()
    
    unique = len(test_rota_gold) - len(test_rota_gold.drop_duplicates())
    
    assert unique == 0
