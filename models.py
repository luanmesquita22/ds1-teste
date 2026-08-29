# importar a instancia do banco 'db' criada no arquivo database.py
from database import db

# definir a classe que iria realizar todo o mapeamento da minha tabela
class Registro(db.model):

    #Define o nome da minha tabela 
    __tablename__ = 'registro'

    id = db.column(db.Integer,primary_key=True)
    nome = db.column(db.String(100), nullable=False)
    info = db.column(db.String(200), nullable=False)
    valor = db.column(db.Float, nullable=False)
    status = db.column(db.String(20), default='pendente')
    