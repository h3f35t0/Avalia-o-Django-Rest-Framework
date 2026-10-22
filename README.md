# 🎬 API de Filmes com Django REST Framework

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/REST%20API-009688?style=for-the-badge" alt="REST API">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de uma API REST para gerenciamento de filmes, utilizando Python, Django e Django REST Framework.

A aplicação foi desenvolvida com o objetivo de colocar em prática conceitos de desenvolvimento backend, criação de endpoints, serialização de dados, operações CRUD e integração com banco de dados.

O projeto também possui uma página HTML de boas-vindas e um script para importação de dados a partir de um arquivo CSV.

## 🎯 Objetivos

- Desenvolver uma API REST utilizando Django.
- Implementar operações de gerenciamento de filmes.
- Trabalhar com modelos, views e serializers.
- Utilizar banco de dados SQLite.
- Praticar requisições HTTP e manipulação de dados JSON.
- Importar dados de filmes utilizando arquivos CSV.

## ✨ Funcionalidades

- 🎥 Gerenciamento de filmes.
- 📋 Consulta de informações cadastradas.
- ➕ Cadastro de filmes.
- ✏️ Atualização de registros.
- 🗑️ Exclusão de registros.
- 📄 Página HTML de boas-vindas.
- 📥 Importação de dados por meio de arquivo CSV.

*As operações disponíveis dependem das rotas e dos métodos implementados no código.*

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Django** — framework para desenvolvimento web.
- **Django REST Framework** — desenvolvimento de APIs REST.
- **SQLite** — banco de dados relacional.
- **HTML5** — estruturação da página inicial.
- **CSV** — armazenamento e importação de dados.
- **Git e GitHub** — controle de versão e hospedagem do código.

## 📂 Estrutura do projeto

```text
projeto4/
│
├── filmes/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── inicio.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── projeto4/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── base_filmes.csv
├── importarDados.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## ⚙️ Pré-requisitos

Para executar o projeto, você precisará ter instalado:

- Python 3.
- pip.
- Git, caso deseje clonar o repositório.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Entre na pasta do projeto

```bash
cd SEU-REPOSITORIO
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

http://127.0.0.1:8000/

## 🔌 Endpoints da API

A API utiliza os métodos HTTP para realizar operações sobre os filmes.

| Método | Descrição |
|---|---|
| GET | Consultar filmes |
| POST | Cadastrar filmes |
| PUT | Atualizar um filme |
| PATCH | Atualizar parcialmente um filme |
| DELETE | Excluir um filme |

Os caminhos exatos dos endpoints devem ser consultados no arquivo `filmes/urls.py` ou nas rotas definidas em `projeto4/urls.py`.

### 🔐 Autenticação

Caso a API exija autenticação, as requisições deverão incluir as credenciais ou o token configurado no Django REST Framework.

O método de autenticação e as permissões disponíveis dependem das configurações da aplicação.

## 📥 Importação de dados

O projeto possui o arquivo `base_filmes.csv`, que pode ser utilizado como fonte de dados para os filmes.

O script `importarDados.py` é destinado à importação desses registros para a aplicação.

Para executá-lo, utilize:

```bash
python importarDados.py
```

**Observação:** execute o comando após verificar se o script está configurado corretamente e se as migrações do banco de dados foram aplicadas.

## 🧠 Principais conceitos praticados

- Desenvolvimento de APIs REST.
- Operações CRUD.
- Modelagem de dados com Django.
- Serialização de dados.
- Requisições HTTP.
- Integração com banco de dados.
- Importação de arquivos CSV.
- Organização de aplicações Django.

## 👨‍💻 Desenvolvedor

**Muller Araújo do Vale**

Desenvolvedor com experiência em Python, C#, Java, Angular, OutSystems e bancos de dados relacionais, com interesse em desenvolvimento backend, APIs REST e arquitetura de sistemas.

- 💼 [LinkedIn](https://www.linkedin.com/in/muller-araujo-65714b15/)

---

<p align="center">
  Desenvolvido com Python e Django 🚀
</p>
