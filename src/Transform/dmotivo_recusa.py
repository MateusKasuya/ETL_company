from src.Extraction.carteira_vendas import main_df

def motivo_recusa():

    df = main_df()
    
    colunas_mot_rec = ['Id Mot. Rec.', 'Motivo de Recusa']
    
    motivo_recusa = df[colunas_mot_rec].drop_duplicates()
    
    motivo_recusa.dropna(inplace = True)
    
    motivo_recusa.index = motivo_recusa['Id Mot. Rec.']
    
    motivo_recusa['Id Mot. Rec.'] = motivo_recusa['Id Mot. Rec.'].astype(str)
    motivo_recusa['Motivo de Recusa'] = motivo_recusa['Motivo de Recusa'].astype(str)
    
    return motivo_recusa
