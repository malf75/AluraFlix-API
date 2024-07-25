# AluraFlix API

Bem-vindo ao AluraFlix API, um projeto desenvolvido como parte do Challenge Backend da Alura. Este projeto utiliza o Django Rest Framework para criar uma API RESTful que gerencia vídeos e categorias, permitindo a manipulação e consulta de dados relacionados a um catálogo de mídia.


## Documentação da API

### Informações Gerais

Esta API possui autenticação JWT. Os endpoints relacionados à autenticação são:

- `POST /token/`: Gera um novo token de acesso e um token de refresh.
- `POST /refresh/`: Gera um novo token de acesso usando um token de refresh.
- `GET /secure/`: Verifica se o token de acesso é válido e se o usuário está autenticado.
  
  A API também aplica rate limiting para proteger contra abusos:

- **Anônimos:** 50 requisições por dia.
- **Usuários Autenticados:** 500 requisições por dia.

### Endpoints

#### Retorna todos os vídeos

GET /videos

Parâmetro   | Tipo       | Descrição
------------|------------|------------
api_key     | string     | **Obrigatório**. A chave da sua API.

#### Retorna um vídeo

GET /videos/${id}

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | string     | **Obrigatório**. O ID do item que você quer.
api_key     | string     | **Obrigatório**. A chave da sua API.

#### Adiciona um novo vídeo

POST /videos

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
api_key       | string     | **Obrigatório**. A chave da sua API.
title         | string     | **Obrigatório**. O título do vídeo.
url           | string     | **Obrigatório**. A URL do vídeo.
categories    | int[]      | **Obrigatório**. Lista de IDs das categorias associadas.

#### Atualiza um vídeo existente

PUT /videos/${id}

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID do vídeo a ser atualizado.
api_key       | string     | **Obrigatório**. A chave da sua API.
title         | string     | Novo título do vídeo.
url           | string     | Nova URL do vídeo.
categories    | int[]      | Lista de IDs das categorias associadas.

#### Remove um vídeo

DELETE /videos/${id}

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID do vídeo a ser removido.
api_key       | string     | **Obrigatório**. A chave da sua API.

#### Retorna todas as categorias

GET /categorias

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
api_key       | string     | **Obrigatório**. A chave da sua API.

#### Retorna uma categoria específica

GET /categorias/${id}

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID da categoria que você deseja recuperar.
api_key     | string     | **Obrigatório**. A chave da sua API.

#### Adiciona uma nova categoria

POST /categorias

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
api_key       | string     | **Obrigatório**. A chave da sua API.
name          | string     | **Obrigatório**. O nome da nova categoria.

#### Atualiza uma categoria existente

PUT /categorias/${id}

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID da categoria a ser atualizada.
api_key       | string     | **Obrigatório**. A chave da sua API.
name          | string     | Novo nome da categoria.

#### Remove uma categoria

DELETE /categorias/${id}

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID da categoria a ser removida.
api_key       | string     | **Obrigatório**. A chave da sua API.

#### Retorna os vídeos de uma categoria

GET /categorias/${id}/videos

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
id            | string     | **Obrigatório**. O ID da categoria cujos vídeos você deseja listar.
api_key       | string     | **Obrigatório**. A chave da sua API.

GET /free/

Parâmetro   | Tipo       | Descrição
------------|------------|------------
Nenhum      | -          | Retorna os 10 primeiros vídeos. Não é necessária autenticação.

### Autenticação JWT

#### Gera um novo token

POST /token/

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
username      | string     | **Obrigatório**. O nome de usuário.
password      | string     | **Obrigatório**. A senha do usuário.

#### Gera um novo token de acesso usando um token de refresh

POST /refresh/

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
refresh       | string     | **Obrigatório**. O token de refresh.

#### Verifica se o token de acesso é válido

GET /secure/

Parâmetro     | Tipo       | Descrição
--------------|------------|------------
api_key       | string     | **Obrigatório**. A chave da sua API.


## Rodando localmente

Clone o Repositório

```bash
git clone https://github.com/usuario/aluraflix-api.git
```

Instale as Dependências
```bash
pip install -r requirements.txt
```
Configure o Ambiente

Crie um arquivo .env e adicione as variáveis de ambiente necessárias.

Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```
Inicie o Servidor

```bash
python manage.py runserver
```

Acesse a API

Acesse a documentação interativa da API em http://localhost:8000/swagger/ ou http://localhost:8000/redoc/
