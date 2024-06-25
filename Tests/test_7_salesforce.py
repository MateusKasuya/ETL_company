from src.Silver.salesforce import salesforce

def test_sf():
    
    test_salesforce = salesforce()
    
    max_value = max(test_salesforce['Contrato Venda'].value_counts())
    
    assert max_value == 1