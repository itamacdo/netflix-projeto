# Gerenciador de Catálogo Netflix - Azure Functions

Este projeto é um microsserviço serverless construído com **Azure Functions** e **Python**, integrado ao **Azure Cosmos DB** para gerenciar um catálogo de filmes.

## Tecnologias Utilizadas

- **Azure Functions** (Processamento Serverless)
- **Azure Cosmos DB** (Banco de Dados NoSQL)
- **Python** (Linguagem de Programação)
- **Visual Studio Code** (IDE)

## Como rodar o projeto localmente

1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv .venv` e ative-o.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Configure sua string de conexão do Cosmos DB no arquivo `local.settings.json`.
5. Execute o comando: `func start`.

## Endpoints da API

- **GET** `/api/movies`: Lista todos os filmes do catálogo.
- **POST** `/api/movies`: Adiciona um novo filme (Requer JSON no corpo).
