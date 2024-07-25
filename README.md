# AluraFlix API

Bem-vindo ao AluraFlix API, um projeto desenvolvido como parte do Challenge Backend da Alura. Este projeto utiliza o Django Rest Framework para criar uma API RESTful que gerencia vídeos e categorias, permitindo a manipulação e consulta de dados relacionados a um catálogo de mídia.


## Documentação da API

#### Retorna todos os vídeos

GET /videos

#### Retorna um vídeo

GET /videos/${id}

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID do item que você quer.

#### Adiciona um novo vídeo

POST /videos

Parâmetro   | Tipo       | Descrição
------------|------------|------------
titulo       | string     | **Obrigatório**. O título do vídeo.
descricao | string | **Obrigatório**. A descrição do vídeo.
url         | URL    | **Obrigatório**. A URL do vídeo.
categoria   | int[]       | A categoria do vídeo.

#### Atualiza um vídeo existente

PUT /videos/${id}/

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID do vídeo a ser atualizado.
titulo       | string     | Novo título do vídeo.
descricao | string | A descrição do vídeo.
url         | URL     | Nova URL do vídeo.
categoria   | int[]       | A categoria do vídeo.

#### Remove um vídeo

DELETE /videos/${id}/

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID do vídeo a ser removido.

#### Retorna todas as categorias

GET /categorias

#### Retorna uma categoria específica

GET /categorias/${id}

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID da categoria que você deseja recuperar.

#### Adiciona uma nova categoria

POST /categorias

Parâmetro   | Tipo       | Descrição
------------|------------|------------
titulo        | string     | **Obrigatório**. O nome da nova categoria.
cor | string | **Obrigatório**. A cor da nova categoria em hexadecimal.

#### Atualiza uma categoria existente

PUT /categorias/${id}/

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID da categoria a ser atualizada.
titulo        | string     | Novo nome da categoria.
cor | string | Nova cor da categoria em hexadecimal.

#### Remove uma categoria

DELETE /categorias/${id}/

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int     | **Obrigatório**. O ID da categoria a ser removida.

#### Retorna os vídeos de uma categoria

GET /categorias/${id}/videos

Parâmetro   | Tipo       | Descrição
------------|------------|------------
id          | int    | **Obrigatório**. O ID da categoria cujos vídeos você deseja listar.

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