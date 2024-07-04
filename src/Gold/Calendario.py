import pandas as pd
from datetime import date
import locale
import math

def calendario():

    locale.setlocale(locale.LC_ALL, '')

    start = '2023-01-01'
    today = date.today()
    end = today.replace(year = today.year + 1, month = 12, day = 31)
    freq = 'D'
    name = 'Data'
    
    df = pd.DataFrame(
            pd.date_range(
                start = start,
                end = end,
                freq = freq,
                name = name
            )
        )
    
    df['Dia da Semana'] = df['Data'].dt.strftime('%A')
    df['Dia da Semana Abrev'] = df['Data'].dt.strftime('%a')
    df['Dia da Semana Num'] = df['Data'].dt.strftime('%w')
    df['Dia'] = df['Data'].dt.strftime('%d')
    df['Mês'] = df['Data'].dt.strftime('%m')
    df['Mês Nome'] = df['Data'].dt.strftime('%B')
    df['Mês Nome Abrev'] = df['Data'].dt.strftime('%b')
    df['Ano'] = df['Data'].dt.strftime('%Y')
    df['Ano Abrev'] = df['Data'].dt.strftime('%y')
    df['Dia do Ano'] = df['Data'].dt.strftime('%j')
    df['Semana do Ano'] = df['Data'].dt.strftime('%U')
    df['Trimestre'] = [math.ceil(q/3) for q in df['Mês'].astype(int)]
    df['Semestre'] = [math.ceil(q/6) for q in df['Mês'].astype(int)]
    df['Mês/Ano'] = df['Data'].dt.strftime('%b/%y')
    df['Ano/Mês'] = df['Data'].dt.strftime('%Y/%m')
    df['Hoje'] = [True if d[:13] == str(today) else False for d in df['Data'].astype(str)]
    df['Até Hoje'] = [True if d[:13] <= str(today) else False for d in df['Data'].astype(str)]
    
    list_ano_safra = []
           
    for i in df['Data']:
        if str(i) >= '2025-04-01':
            list_ano_safra.append('25/26')
        elif str(i) >= '2024-04-01':
            list_ano_safra.append('24/25')
        elif str(i) >= '2023-04-01':
            list_ano_safra.append('23/24')
        else:
            list_ano_safra.append('22/23')
            
    df['Ano Safra'] = list_ano_safra
    
    df.to_excel('Data/Output/Gold/Calendário.xlsx', index = False)

    return df