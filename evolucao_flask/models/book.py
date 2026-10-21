#contém os modelos que representam as entidades do banco
#Book representa a entidade book
from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Book(db.Model):
#indicar que book é um modelo gerenciado pelo sqlalchemy
    __tablename__ = "book"
    #define o nome da tabela
    id = db.Column(
        UUID(as_uuid = True), #vou usar o UUID
        primary_key = True, #chave primaria
        default = uuid4 #quando criar um novo livro, um UUID será criado
    )

    #tabela título
    title = db.Column(
        String(255), #recebe a string
        nullable = False #não aceita nulo 
    )

    #tabela autor
    author = db.Column(
        String(255),
        nullable = False
    )
    #title e author são obrigatórios

    description = db.Column(
        Text, #textos maiores
        nullable = False
    )

    #livro favorito
    is_favorite = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    #livro em leitura
    is_reading = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    #livros finalizados
    is_finished = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    def as_dict(self):
        return{
        "id":str(self.id),  #necessário conversão forçada
        "title": self.title,
        "author": self.author,
        "description": self.description,
        "is_favorite": self.is_favorite,
        "is_reading": self.is_reading,
        "is_finished": self.is_finished
    }

#Transformando o modelo em dicionário
"""
POR ISSO SERÁ CRIADO UM MÉTODO RESPONSÁVEL POR TRANSFORMAR 
O OBJETO BOOK EM UM DICIONÁRIO PYTHON

QUANDO OCORRE UMA CONSULTA AO NOSSO SISTEMA ELE RETORNA UM OBJETO BOOK,
ELE NÃO É SIMPLESMENTE  UM DICT PYTHON.
O método AS_DICT() funciona como uma camada de conversão, selecionando
apenas o necessário para ser exposto pela API e transformando em um DICT,
ESTRUTURA PODE SER FACILMENTE SERIALIZADA PARA JSON RESPOSTA HTTP.

"""

