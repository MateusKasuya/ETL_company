import pandas as pd

file = 'Data/Output/BEX/dcontrato.csv'

df = pd.read_csv(file, encoding='latin-1', decimal= ',')