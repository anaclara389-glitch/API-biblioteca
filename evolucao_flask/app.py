#responsável pela aplicação flask
#e pelos endpoints
#app de gerenciamento de livros - 
#consultar livros
#editar 
#atualizar
#deletar
#favoritar
#Livros em leitura
#livros finalizados
import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from db import db
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL"
)

db.init_app(app)
migrate = Migrate(app, db)

print(os.getenv("DATABASE_URL"))
