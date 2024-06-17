from src.Gold.Calendario import calendario

def test_calendario():
    
    test_data = calendario()
    
    max_value = max(test_data['Data'].value_counts())
    
    assert max_value == 1