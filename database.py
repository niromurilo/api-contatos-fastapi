import json
import os

ARQUIVO = "contatos.json"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w") as f:
        json.dump([], f)


def ler_contatos():
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=4)