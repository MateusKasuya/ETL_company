from src.Extraction.carteira_vendas import main_df
from src.schema import df_schema
from src.Transform.dmotivo_recusa import motivo_recusa
from src.Transform.dcontrato import contrato

def test_main_df():

    # Comparando a quantidade de colunas da nossa main_df como o schema definido
    
    df = main_df()
    
    extra_cols = len(df.columns) - len(df_schema.__fields__.keys())

    assert extra_cols == 0
    
def test_motivo_recusa():

    # Verificar se Motivo Recusa tem valores únicos
    
    df_motivo_recusa = motivo_recusa()
    
    unique_id_mot_rec = len(df_motivo_recusa['Id Mot. Rec.']) - len(df_motivo_recusa['Id Mot. Rec.'].unique())
    
    assert unique_id_mot_rec == 0
    
def test_contrato():
    
    # Verificar se Contrato tem PK's únicas
    
    df_contrato = contrato()
    
    unique_contrato = len(df_contrato[['Contrato Venda', 'Item Contrato']]) - len(set(df_contrato['Contrato Venda'].astype(str) + df_contrato['Item Contrato'].astype(str)))
    
    assert unique_contrato == 0