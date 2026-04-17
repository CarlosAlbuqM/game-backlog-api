# 🎮 Game Backlog API

API REST desenvolvida com **FastAPI**, **PostgreSQL** e **SQLModel** para gerenciar um backlog de jogos.

## 📌 Sobre o projeto

Este projeto foi criado para praticar desenvolvimento backend com Python, criação de APIs RESTe integração com banco de dados PostgreSQL

A proposta da API é permitir o cadastro e gerenciamento de jogos com informações como título, gênero, plataforma, status e nota.

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- SQLModel
- python-dotenv

## 🎯 Funcionalidades

- Criar um jogo
- Listar jogos
- Buscar jogo por ID
- Atualizar jogo
- Deletar jogo
- Filtrar jogos por status
- Filtrar jogos por plataforma
- Filtrar por gênero
- Paginação com limit e offset
- Resumo por status
- Resumo por gênero

## 🕹️ Status disponíveis

- `backlog`
- `playing`
- `completed`
- `dropped`

## 📁 Estrutura do projeto

```bash
game-backlog-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── enums.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Como executar o projeto

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DATABASE_URL=postgresql+psycopg://SEU_USUARIO:SUA_SENHA@localhost:5432/game_backlog_db
```

### 3. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

## 📚 Documentação da API

Após iniciar o projeto, acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`

## 🔗 Endpoints principais

- `GET /`
- `POST /games`
- `GET /games`
- `GET /games/{id}`
- `PUT /games/{id}`
- `DELETE /games/{id}`
- `GET /games/summary`
- `GET /games/summary/genres`

## 🧪 Exemplo de requisição

### Criar um jogo

```json
{
  "title": "Resident Evil 2 Remake",
  "genre": "Survival Horror",
  "platform": "PC",
  "status": "completed",
  "score": 9,
  "release_year": 2019
}
```

## ✅ Aprendizados

Neste projeto pratiquei:

- Criação de API REST com FastAPI
- Integração com PostgreSQL
- Modelagem de dados
- Validação com Pydantic/SQLModel
- Testes de endpoints com Swagger
- Organização de projeto backend para portfólio

## 👨‍💻 Autor

Projeto desenvolvido por **Carlos Albuquerque**.