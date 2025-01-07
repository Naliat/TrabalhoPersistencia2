# Projeto: Implementação de API Web com FastAPI e SQLModel

Este projeto tem como objetivo a criação de uma API Web utilizando FastAPI e SQLModel para o gerenciamento de informações de remédios, fornecedores e estoque.

## Estrutura do Projeto

```bash
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py             # Arquivo principal da aplicação
│   ├── models/             # Modelos do banco de dados
│   │   ├── __init__.py
│   │   ├── remedio.py      # Modelo para a entidade Remédio
│   │   ├── fornecedor.py   # Modelo para a entidade Fornecedor
│   │   └── estoque.py      # Modelo para a entidade Estoque
│   ├── crud/               # Funções CRUD (Create, Read, Update, Delete)
│   │   ├── __init__.py
│   │   ├── remedio.py      # CRUD para a entidade Remédio
│   │   ├── fornecedor.py   # CRUD para a entidade Fornecedor
│   │   └── estoque.py      # CRUD para a entidade Estoque
│   ├── schemas/            # Esquemas de dados para a API (Pydantic)
│   │   ├── __init__.py
│   │   ├── remedio.py      # Esquema para a entidade Remédio
│   │   ├── fornecedor.py   # Esquema para a entidade Fornecedor
│   │   └── estoque.py      # Esquema para a entidade Estoque
│   ├── routes/             # Rotas da API
│   │   ├── __init__.py
│   │   ├── remedio.py      # Rotas para a entidade Remédio
│   │   ├── fornecedor.py   # Rotas para a entidade Fornecedor
│   │   └── estoque.py      # Rotas para a entidade Estoque
│   └── config.py           # Configurações do projeto (conexão com o banco, etc.)
```
Como Executar o Projeto
1. Ativando o Ambiente Virtual (Linux/Mac):
Para ativar o ambiente virtual, execute o seguinte comando:

bash
source .venv/bin/activate
2. Executando a Aplicação
Após ativar o ambiente, execute o servidor de desenvolvimento utilizando o uvicorn:

bash
uvicorn app.main:app --reload
A aplicação estará disponível no endereço http://127.0.0.1:8000.

Descrição das Entidades
Remédio
id: Identificador único do remédio.

nome: Nome do remédio.

tarja: Tipo de tarja do remédio (ex.: vermelha, preta, etc.).

preço: Preço do remédio.

validade: Data de validade do remédio.

Fornecedor
ID_Fornecedor: Identificador único do fornecedor.

nome_fornecedor: Nome do fornecedor.

contato: Informações de contato do fornecedor.

endereço: Localização do fornecedor.

tipo_produto: Tipo de produto fornecido (ex.: remédios, equipamentos médicos, etc.).

Estoque
id_do_remedio: Identificador do remédio relacionado ao estoque.

quantidade: Quantidade de itens no estoque.

data_validade: Data de validade do produto.

data_entrada_estoque: Data de entrada do produto no estoque.

unidade_medida: Unidade de medida do produto (ex.: caixa, frasco, etc.)


│
├── .env                    # Variáveis de ambiente
├── .python-version         # Versão do Python utilizada
├── uv.lock                 # Lock file do UVicorn
└── pyproject.toml          # Dependências e configurações do projeto
