# API de Contatos 📇

API REST desenvolvida com FastAPI para gerenciamento de contatos.

O projeto permite realizar operações completas de CRUD (criar, listar, atualizar e remover contatos), além de aplicar validação de dados e organização em estrutura modular.

---

## 🚀 Tecnologias utilizadas

* Python
* FastAPI
* Pydantic

---

## 📌 Funcionalidades

* Cadastro de contatos
* Listagem de contatos
* Atualização de dados
* Remoção de contatos
* Validação de email

---

## 🔗 Endpoints

| Método | Rota           | Descrição               |
| ------ | -------------- | ----------------------- |
| GET    | /contatos      | Lista todos os contatos |
| POST   | /contatos      | Cria um novo contato    |
| PUT    | /contatos/{id} | Atualiza um contato     |
| DELETE | /contatos/{id} | Remove um contato       |

---

## 📥 Exemplo de requisição

### Criar contato

POST /contatos

```json
{
  "nome": "Murilo",
  "email": "murilo@email.com"
}
```

---

## 📤 Exemplo de resposta

```json
{
  "status": "sucesso",
  "mensagem": "Contato adicionado",
  "contato": {
    "id": 1,
    "nome": "Murilo",
    "email": "murilo@email.com"
  }
}
```

---

## 📷 Demonstração

![API funcionando](assets/api.png)

---

## ▶️ Como executar o projeto

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse a documentação interativa em:
http://127.0.0.1:8000/docs

---

## 📈 Melhorias futuras

* Integração com banco de dados (SQLite)
* Autenticação de usuários
* Deploy da aplicação
