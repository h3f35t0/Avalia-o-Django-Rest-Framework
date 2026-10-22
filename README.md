# 🎬 API de Filmes — Django REST Framework

Projeto desenvolvido em Python utilizando **Django REST Framework** para a criação de uma API REST de gerenciamento de filmes e gêneros cinematográficos.

A aplicação permite consultar, cadastrar, editar e excluir registros de filmes e gêneros, utilizando uma estrutura de banco de dados relacional e serialização de dados no formato JSON.

## 🚀 Tecnologias utilizadas

- Python
- Django
- Django REST Framework (DRF)
- Django Filter
- SQLite (banco de dados padrão do Django)
- API REST e JSON
- Autenticação por Token

## ⚙️ Funcionalidades

- Cadastro e gerenciamento de filmes.
- Cadastro e gerenciamento de gêneros cinematográficos.
- Relacionamento entre filmes e gêneros.
- Consulta e filtragem de registros.
- Autenticação por token.
- Controle de permissões de acesso.
- Administração de dados pelo Django Admin.
- Testes dos endpoints via navegador e terminal utilizando cURL.

## 📋 Estrutura dos dados

**Filmes**
- Título
- Descrição
- Ano de lançamento
- Gênero
- Duração

**Gêneros**
- Nome

## 🎯 Objetivo

Consolidar conhecimentos em desenvolvimento web com Python, construção de APIs REST, operações CRUD, modelagem de dados, serialização JSON, autenticação e controle de acesso utilizando Django REST Framework.

## ▶️ Como executar o projeto

1. Crie e ative um ambiente virtual.
2. Instale as dependências:

   ```bash
   pip install django django-filter djangorestframework
   ```

3. Execute as migrações do banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

A API ficará disponível localmente em `http://127.0.0.1:8000/`.

**Projeto acadêmico desenvolvido para praticar a criação e o gerenciamento de APIs REST com Django.**
