import pandas as pd
import numpy as np

def rotas():

    file_contrato = 'Data/Output/Gold/Contrato.xlsx'
    file_local_exp = 'Data/Output/Gold/Local de Expedição.xlsx'
    file_cliente = 'Data/Output/Gold/Cliente.xlsx'
    file_cte = 'Data/Output/Gold/CTE.xlsx'
    file_ov = 'Data/Output/Gold/Ordem de Venda.xlsx'
    
    contrato = pd.read_excel(file_contrato)
    contrato = contrato.loc[:,['Id Local Exp.', 'Id Cliente']]
    
    local_exp = pd.read_excel(file_local_exp)
    local_exp = local_exp.loc[:,['Id', 'Origem', 'UF']]
    
    cliente = pd.read_excel(file_cliente)
    cliente = cliente.loc[:, ['Id', 'Destino', 'UF']]
    
    rota_contrato = contrato.merge(local_exp, left_on = 'Id Local Exp.', right_on = 'Id', how = 'left')
    rota_contrato = rota_contrato.merge(cliente, left_on = 'Id Cliente', right_on = 'Id', how = 'left')
    
    rota_contrato.rename(columns = {'UF_x' : 'UF Origem', 'UF_y' : 'UF Destino'}, inplace = True)
    
    rota_contrato = rota_contrato.loc[:, ['Origem', 'UF Origem', 'Destino', 'UF Destino']]
    
    rota_contrato.dropna(inplace = True)
    
    ov = pd.read_excel(file_ov)
    ov = ov.loc[:, ['Id Local Exp.', 'Id Cliente']]    

    rota_ov = ov.merge(local_exp, left_on = 'Id Local Exp.', right_on = 'Id', how = 'left')
    rota_ov = rota_ov.merge(cliente, left_on = 'Id Cliente', right_on = 'Id', how = 'left')
    
    rota_ov.rename(columns = {'UF_x' : 'UF Origem', 'UF_y' : 'UF Destino'}, inplace = True)
    
    rota_ov = rota_ov.loc[:, ['Origem', 'UF Origem', 'Destino', 'UF Destino']]
    
    rota_ov.dropna(inplace = True)
    
    cte = pd.read_excel(file_cte)
    
    cte = cte.loc[:, ['Origem Expedidor', 'UF Origem Expedidor',
                      'Origem Remetente', 'UF Origem Remetente',
                      'Destino Recebedor', 'UF Destino Recebedor',
                      'Destino Destinatário', 'UF Destino Destinatário'
                      ]]
    
    cte['Origem'] = np.where(pd.isna(cte['Origem Expedidor']), cte['Origem Remetente'], cte['Origem Expedidor'])
    cte['UF Origem'] = np.where(pd.isna(cte['UF Origem Expedidor']), cte['UF Origem Remetente'], cte['UF Origem Expedidor'])
    cte['Destino'] = np.where(pd.isna(cte['Destino Recebedor']), cte['Destino Destinatário'], cte['Destino Recebedor'])
    cte['UF Destino'] = np.where(pd.isna(cte['UF Destino Recebedor']), cte['UF Destino Destinatário'], cte['UF Destino Recebedor'])
    
    cte = cte.loc[:,['Origem', 'UF Origem', 'Destino', 'UF Destino']]
    
    cte.dropna(inplace = True)
    
    rota = pd.concat([rota_contrato, cte, rota_ov], axis = 0)
    
    rota.drop_duplicates(inplace = True)
    
    rota['Rota'] = rota['Origem'] + '-' + rota['UF Origem'] + ' -> ' + rota['Destino'] + '-' + rota['UF Destino']
    
    rota.to_excel('Data/Output/Gold/Rotas.xlsx', index = False)
    
    return rota
