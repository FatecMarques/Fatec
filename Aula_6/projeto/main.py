from flask import Flask
from http import HTTPStatus
import requests
import json


app = Flask(__name__)  # controle de erro


# READ
@app.get("/get_info")  # endpoint seguido de função // VER verbos http -- GET POST PUT DELETE --
def get_info():
    """Essa função lê o banco de dados de informações do cliente"""
    with open("db.jason", "r") as arquivo:
        arquivo = json.load(arquivo)
        return arquivo


# UPDATE
@app.post("/<string:cep>")
def save_info(cep):
    """Essa função atualiza o banco de dados"""
    info_coletada = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    with open("db.jason", "w") as arquivo:
        json.dump(info_coletada.json(), arquivo, indent=4)
    return {"msg": "Endereço salvo com sucesso"}        # info_coletada.json()


app.run(port=5050)
