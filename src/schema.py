from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional
from datetime import datetime

class df_schema(BaseModel):
    Contrato_Venda : Optional[PositiveInt]
    Item_Contrato : Optional[PositiveInt]
    OV : PositiveInt
    Item_OV : PositiveInt
    Pedido_SalesForce : Optional[str]
    Tipo_Documento : str
    Data_de_criação : Optional[datetime]
    Data_Início_Entrega : Optional[datetime]
    Data_Fim_Entrega : Optional[datetime]
    Qtde_Contrato : Optional[PositiveFloat]
    Valor_Contrato : Optional[PositiveFloat]
    Qtde_OV : Optional[PositiveFloat]
    Valor_OV : Optional[PositiveFloat]
    Moeda : str
    Id_Mot_Rec : Optional[str]
    Motivo_de_Recusa : Optional[str]
    Requisição_de_compra : Optional[PositiveInt]
    Id_Centro : Optional[PositiveInt]
    Centro : Optional[PositiveInt]
    CNPJ_Centro : Optional[PositiveInt]
    Id_Local_Exp : Optional[str]
    Local_Expedição : Optional[str]
    CNPJ_Local_Exp : Optional[str]
    Id_UF_Origem : Optional[str]
    UF_Origem : Optional[str]
    Origem : Optional[str]
    Zona_Transp_Origem : Optional[str]
    Id_Cliente : PositiveInt
    Cliente : str
    CNPJ_Raiz_Cliente : PositiveInt
    CNPJ_Cliente : Optional[PositiveInt]
    CPF_Cliente : Optional[PositiveInt]
    Ins_Est_Cliente : Optional[PositiveInt]
    Ins_Mun_Cliente : Optional[PositiveInt]
    Id_UF_Destino : str
    UF_Destino : str
    Destino : str
    Zona_Transp_Destino : str
    Id_Itinerário : Optional[str]
    Itinerário : Optional[str]
    Distância : Optional[str]
    Incoterms : Optional[str]
    Id_Grupo_Merc : str
    Grupo_de_Mercadorias : str
    Id_Produto : PositiveInt
    Produto : str
    Unid_Produto : str
    NCM_Produto : Optional[str]