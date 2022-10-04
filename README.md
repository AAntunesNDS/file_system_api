<h1 align="center">File System API</h1>

<p align="center">API simples para criação de diretórios e arquivos</p>

## Descrição do Desafio

Desenvolver a camada de modelos de um sistema de arquivos persistido em um banco de dados SQL onde seja possível criar diretórios e arquivos.
Os diretórios poderão conter sub-diretórios e arquivos.
O conteúdo dos arquivos podem ser persistidos como blob, S3 ou mesmo em disco.
A solução deverá ser escrita majoritariamente em Python com um dos frameworks Django, Flask ou Pyramid.


### Pré-requisitos

Para rodar o projeto é preciso ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python 3.8](https://www.python.org/downloads/release/python-380/) e o gerenciador de dependencias [Poetry](https://python-poetry.org/). 

### Setup Inicial

```bash
# Clone este repositório
$ git clone https://github.com/AAntunesNDS/file_system_api.git

# Entre na pasta do projeto:
$ cd file-system-api

# Instale as dependências:
$ poetry install

# Entre no diretório da aplicação e crie um arquivo .env com as credenciais da AWS para utilizar o S3 (pode ser feito pela interface):
$ cd file_system_api
$ cat > .env
AWS_ACCOUNT_ID=<value>
AWS_REGION=<value>
AWS_SECRET_KEY=<value>
BUCKET_NAME=<value>

```

### Rodando o servidor 

```bash
# Dentro do diretório da aplicação (file-system-api/file_system_api) execute o comando:
$ python3.8 app.py 

# O servidor inciará na porta:5000 (http://127.0.0.1:5000)
# Para validar que está de pé o servidor você pode acessar o endpoint http://127.0.0.1:5000/apidocs/
# 

```


### Testes Unitários

```bash
# Parte dos testes unitários utiliza diretamente o client da aplicação, portanto, se certifique que o servidor está rodando nesse ponto. 
# Dentro do diretório da aplicação (file-system-api/file_system_api) execute o comando:
$ python3.8 -m unittest discover -v

```

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- Python
- Flask (Framework para expor a API)
- Flasgger (Para expor o Swagger)
- SQLite (Banco de dados SQL simples)
- Peewee (ORM para o banco de dados SQL)
- Boto3 (AWS SDK)
