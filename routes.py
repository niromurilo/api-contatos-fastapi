from fastapi import APIRouter
from models import Contato
from database import ler_contatos, salvar_contatos

router = APIRouter()

@router.get("/contatos")
def listar_contatos():
    return ler_contatos()


@router.post("/contatos")
def adicionar_contato(contato: Contato):
    contatos = ler_contatos()

    if contatos:
        novo_id = max(c["id"] for c in contatos) + 1
    else:
        novo_id = 1

    novo = {
        "id": novo_id,
        "nome": contato.nome,
        "email": contato.email
    }

    contatos.append(novo)
    salvar_contatos(contatos)

    return {"mensagem": "Contato adicionado", "contato": novo}

@router.delete("/contatos/{id}")
def deletar_contato(id: int):
    contatos = ler_contatos()

    novos = [c for c in contatos if c["id"] != id]

    salvar_contatos(novos)

    if len(contatos) == len(novos):
        return {"erro": "Contato não encontrado"}
    return {"status": "sucesso", "mensagem": "Contato removido"}

@router.put("/contatos/{id}")
def editar_contato(id: int, contato: Contato):
    contatos = ler_contatos()

    for c in contatos:
        if c["id"] == id:
            c["nome"] = contato.nome
            c["email"] = contato.email

    salvar_contatos(contatos)

    return {"mensagem": "Contato atualizado"}