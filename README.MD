---4.1 Infraestrutura

O projeto SaquaGaming será desenvolvido utilizando contêineres Docker para garantir um ambiente de desenvolvimento padronizado e de fácil execução.

Tecnologias Utilizadas
Python 3.13
FastAPI
SQLAlchemy
PostgreSQL
Alembic
Pydantic v2
Docker
Docker Compose
Pytest
Estrutura de Containers

O ambiente será composto pelos seguintes serviços:

api: responsável pela execução da API REST desenvolvida com FastAPI.
db: banco de dados PostgreSQL utilizado pela aplicação.
pgadmin (opcional): interface gráfica para administração do banco de dados.
Dockerfile

A aplicação possuirá um Dockerfile responsável por configurar o ambiente da API e instalar todas as dependências necessárias para sua execução.

docker-compose.yml

O projeto utilizará um arquivo docker-compose.yml para orquestrar os serviços da aplicação e do banco de dados, permitindo sua inicialização através de um único comando.

docker compose up --build
Variáveis de Ambiente

Será disponibilizado um arquivo .env.example contendo todas as variáveis necessárias para execução do projeto, sem expor informações sensíveis.

Exemplo:

DATABASE_URL=postgresql://usuario:senha@db:5432/saquagaming

SECRET_KEY=sua_chave_secreta

PORT=8000
Inicialização

Após configurar as variáveis de ambiente, toda a aplicação poderá ser iniciada com o comando:

docker compose up --build

Esse comando será responsável por criar os containers necessários e iniciar automaticamente a API e o banco de dados PostgreSQL.