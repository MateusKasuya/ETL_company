from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///banco_origeo.db', echo=True)

print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, DateTime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'cte'
    
    xml = Column(String, primary_key=True)
    expedidor = Column(String)
    origem_expedidor = Column(String)
    cnpj_expedidor = Column(String)
    uf_origem_expedidor = Column(String)
    remetente = Column(String)
    cnpj_remetente = Column(String)
    uf_origem_remetente = Column(String)
    origem_remetente = Column(String)
    recebedor = Column(String)
    cnpj_recebedor = Column(String)
    destino_recebedor = Column(String)
    uf_destino_recebedor = Column(String)
    destinatario = Column(String)
    cnpj_destinatario = Column(String)
    destino_destinatario = Column(String)
    uf_destino_destinatario = Column(String)
    transportadora = Column(String)
    cnpj_transportadora = Column(String)
    data = Column(DateTime)
    chave_nf = Column(String)
    nf = Column(String)
    cte = Column(String)
    peso_volume = Column(Float)
    valor_frete_total = Column(Float)
    produto = Column(String)
    grupo_mercadorias = Column(String)
    tipo_cte = Column(String)


# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

from datetime import datetime

novo_usuario = Usuario(
        xml = '21240722686175000480570020000035041000840171-procCTe.xml',
        expedidor = 'Fertilizantes Tocantins Ltda',
        origem_expedidor = 'São Luís',
        cnpj_expedidor = '05571228000317',
        uf_origem_expedidor = 'MA',
        remetente = 'Fertilizantes Tocantins Ltda',
        cnpj_remetente = '05571228000317',
        uf_origem_remetente = 'MA',
        origem_remetente = 'São Luís',
        recebedor = 'Ione Maria Gabriel Taques',
        cnpj_recebedor = '03745022939',
        destino_recebedor = 'Goiatins',
        uf_destino_recebedor = 'TO',
        destinatario = 'Ione Maria Gabriel Taques',
        cnpj_destinatario = '03745022939',
        destino_destinatario = 'Goiatins',
        uf_destino_destinatario = 'TO',
        transportadora = 'Carvalho Comercio E Transportes Ltda - Sao Luis-Ma',
        cnpj_transportadora = '22686175000480',
        data = datetime.strptime('2024-07-15 00:00:00', '%Y-%m-%d %H:%M:%S'),
        chave_nf = '21240705571228000317550010001596401100280654',
        nf = '159640',
        cte = '3504',
        peso_volume = 50000.0,
        valor_frete_total = 9500.0,
        produto = 'FERTILIZANTE KCL 60%',
        grupo_mercadorias = 'Fertilizantes Outros',
        tipo_cte = 'Normal'
)
    
    #Verificar tipos de dados antes de inserir
print(f"Tipo de xml: {type(novo_usuario.xml)}")
print(f"Tipo de expedidor: {type(novo_usuario.expedidor)}")
print(f"Tipo de origem_expedidor: {type(novo_usuario.origem_expedidor)}")
print(f"Tipo de cnpj_expedidor: {type(novo_usuario.cnpj_expedidor)}")
print(f"Tipo de uf_origem_expedidor: {type(novo_usuario.uf_origem_expedidor)}")
print(f"Tipo de data: {type(novo_usuario.data)}")
print(f"Tipo de peso_volume: {type(novo_usuario.peso_volume)}")
print(f"Tipo de valor_frete_total: {type(novo_usuario.valor_frete_total)}")
          
with Session() as session:
    session.add(novo_usuario)
    session.commit()
    # session.close()