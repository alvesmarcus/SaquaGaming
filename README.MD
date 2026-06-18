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


# 5.1 Decisões de Design Justificadas

## Por que os relacionamentos foram modelados dessa forma?

No sistema existem usuários, jogos e empréstimos. Foi criada uma tabela de empréstimos para ligar usuários e jogos, pois um usuário pode pegar vários jogos emprestados e um jogo pode ser emprestado várias vezes ao longo do tempo.

Essa forma foi escolhida porque permite guardar o histórico dos empréstimos realizados no sistema.

## Por que algumas regras estão no Pydantic e outras na camada de serviço?

As validações mais simples, como verificar o tamanho do título do jogo ou se o ano de lançamento é válido, foram colocadas no Pydantic.

Já as regras de negócio foram colocadas na camada de serviço. Por exemplo, verificar se um jogo está disponível para empréstimo ou se um empréstimo já foi devolvido.

Essa divisão deixa o código mais organizado e fácil de manter.

## Por que a Migration 2 foi necessária?

No início do projeto a tabela de usuários não possuía senha.

Depois foi necessário implementar o login utilizando JWT, então foi criada uma migration para adicionar a coluna senha na tabela users.

Essa alteração foi necessária porque o sistema evoluiu e passou a precisar de autenticação.

## O que acontece se dois usuários tentarem pegar o mesmo jogo ao mesmo tempo?

O correto é que apenas o primeiro usuário consiga realizar o empréstimo.

Quando o empréstimo é criado, o jogo passa para o estado indisponível. Se outro usuário tentar emprestar o mesmo jogo, o sistema retorna uma mensagem informando que ele não está disponível.

## Quais estados são terminais?

Um empréstimo pode estar ativo ou devolvido.

Quando o campo devolvido fica como true, significa que o empréstimo foi finalizado. Esse é considerado um estado terminal, pois não faz sentido devolver novamente um jogo que já foi devolvido.


# 5.2 Consistência em Cenários de Borda

## Cenário 1 – Jogo indisponível

Se um usuário tentar emprestar um jogo que já está emprestado, o sistema não permite a operação e retorna uma mensagem informando que o jogo está indisponível.

## Cenário 2 – Devolução de um empréstimo já finalizado

Se um usuário tentar devolver um empréstimo que já foi devolvido anteriormente, o sistema bloqueia a operação e retorna uma mensagem de erro.

## Cenário 3 – Usuário inexistente

Se for realizada uma busca por um usuário que não existe no banco de dados, o sistema retorna erro informando que o usuário não foi encontrado.

## Cenário 4 – E-mail já cadastrado

O sistema não permite o cadastro de dois usuários com o mesmo e-mail. Caso isso aconteça, o banco de dados bloqueia a operação para evitar registros duplicados.



# 5.3 Mensagens de Erro Informativas

Durante o desenvolvimento foi utilizado um padrão de retorno de erros contendo código HTTP, mensagem e detalhes.

Exemplo:

{
"codigo": 400,
"mensagem": "Erro na requisição",
"detalhes": "Jogo indisponível"
}

Uma melhoria futura seria utilizar códigos específicos para cada regra de negócio.

Exemplos:

GAME_UNAVAILABLE – quando o jogo não estiver disponível para empréstimo.

EMAIL_ALREADY_EXISTS – quando já existir um usuário cadastrado com o mesmo e-mail.

LOAN_ALREADY_FINISHED – quando for realizada uma tentativa de devolver um empréstimo já finalizado.

Esses códigos ajudam a identificar os erros de forma mais rápida e organizada.
