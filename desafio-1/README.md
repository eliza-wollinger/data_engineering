# Ingestão de dados da NBA e de startups de tecnologia em um banco de dados PostgreSQL utilizando Python

Este é um projeto desenvolvido em python que lê arquivos CSV e JSON e insere os dados em um banco de dados PostgreSQL. O objetivo deste projeto é demonstrar como carregar dados em um banco de dados relacional usando Python.

## Tecnologias utilizadas

Este projeto utiliza as seguintes tecnologias:

- Python 3.9.7 - Linguagem de programação
- PostgreSQL 14.0 - Banco de dados relacional
- Psycopg2-binary 2.9.1 - Biblioteca Python para conectar o banco de dados PostgreSQL

## Como utilizar

Siga as instruções abaixo para executar o script e carregar os dados no banco de dados PostgreSQL.

### Pré-requisitos

- Python 3.x instalado
- PostgreSQL 14.x instalado
- Arquivos de dados CSV da NBA (pode ser encontrado no seguinte link: [DADOS NBA](https://www.kaggle.com/datasets/loganlauton/nba-players-and-team-data))
- Arquivo de dados JSON de startups de tecnologia (pode ser encontrado no seguinte link: [DADOS STARTUP](https://www.kaggle.com/datasets/chickooo/top-tech-startups-hiring-2023?select=json_data.json))

### Instalação

Clone este repositório:

~~~~
git clone https://github.com/eliza-wollinger/engenharia-de-dados.git
~~~~

Entre na pasta `desafio-1` e instale as dependências usando o pip:

~~~~
pip install -r requirements.txt
~~~~

Crie um banco de dados no PostgreSQL utilizando os scripts disponibilizados.

### Utilização

Execute o script main.py da pasta `desafio-1` para carregar os dados da NBA e das startups no banco de dados PostgreSQL:

~~~~
python main.py
~~~~

### Estrutura do projeto

O projeto tem a seguinte estrutura de diretórios e arquivos:

~~~~
    get_nba_data.py
    get_startup_data.py
    db_connection.py
    main.py
    requirements.txt
    README.md
    .gitignore
~~~~

- get_nba_data.py: Script Python que lê os dados dos arquivos CSV da NBA e insere no banco de dados PostgreSQL.
- get_startup_data.py: Script Python que lê os dados do arquivo JSON de startups de tecnologia e insere no banco de dados PostgreSQL.
- db_connection: Script Python que faz a conexão com o banco de dados PostgreSQL.
- main.py: Script principal.
- requirements.txt: Arquivo que lista as dependências do projeto.
- README.md: Arquivo que contém informações sobre o projeto.
- .gitignore: Arquivo que lista os arquivos que não devem ser incluídos no repositório Git.
