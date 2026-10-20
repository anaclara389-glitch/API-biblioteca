#desenvolver um back end com api - 
#postman - teste http -> verificar respostas da API
#1. OBJETIVO 
#2. URL BASE
#3. ENDPOINTS
#4. RECURSOS DISPONIBILIZADOS

#VAMOS CRIAR UMA API:

"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
#APP -> representa a aplicação flask
#__name__ identifica o módulo da aplicação

livros = [
   {
"id": 1,
"titulo": "Harry Potter",
"autor": "J. K. Rowling"
},

{
"id": 2,
"titulo": "Dragões de éter",
"autor": "Rafael Draccon"
},

{
"id": 3,
"titulo": "Coraline",
"autor": "Neil Gaiman"
},

{
"id": 4,
"titulo": "O Senhor dos Anéis",
"autor": "J. R. R. Tolkien"
},

{
"id": 5,
"titulo": "O Hobbit",
"autor": "J. R. R. Tolkien"
},

{
"id": 6,
"titulo": "Percy Jackson e os Olimpianos",
"autor": "Rick Riordan"
},

{
"id": 7,
"titulo": "As Crônicas de Nárnia",
"autor": "C. S. Lewis"
},

{
"id": 8,
"titulo": "O Nome do Vento",
"autor": "Patrick Rothfuss"
},

{
"id": 9,
"titulo": "A Bússola de Ouro",
"autor": "Philip Pullman"
},

{
"id": 10,
"titulo": "O Ladrão de Raios",
"autor": "Rick Riordan"
},

{
"id": 11,
"titulo": "O Feiticeiro de Terramar",
"autor": "Ursula K. Le Guin"
},

{
"id": 12,
"titulo": "O Silmarillion",
"autor": "J. R. R. Tolkien"
}

]

#consultar livros - criar uma função 
#def obter_livros():
    #return jsonify(livros)

#criar as rotas  /livros -> endpoint
#a rota foi especificada, somente o método GET será aceito
@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)


#criar as rotas  /livros id
@app.route("/livros/<int:id>", methods = ["GET"])
#<int:> -> indica inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"message": "livro não encontrado!"}), 404

#PUT -> primeiro os dados enviados pelo cliente serão obtidos
@app.route("/livros/<int:id>", methods = ["PUT"])
def editar_livro_por_id(id):
    #permite acessar od dados json enviados no corpo da requisição
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return (f"Livro alterado: Índice: {indice} | ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
        

#CRIAÇÃO DE UM NOVO LIVRO
@app.route("/livros", methods = ["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


#delete - excluir um livroJ
@app.route("/livros/<int:id>", methods = ["DELETE"])
def excluir_livro(id):
#como é necesário remover um elemento da lista
#pelo seu indice, será utilizado novamente o enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)

#inicialização do servidor local
app.run(
    host = "localhost",
    port = 5000,
    debug = True
)


