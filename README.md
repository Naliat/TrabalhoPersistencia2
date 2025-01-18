# Aplicação FastAPI para Gerenciamento de Fornecedores

## Descrição

Esta aplicação, desenvolvida com **FastAPI**, utiliza **SQLModel** e **SQLite** para gerenciar informações de fornecedores. A API permite realizar operações CRUD (Create, Read, Update, Delete) e inclui consultas avançadas, como a busca de fornecedores por nome ou CNPJ.

A estrutura segue uma abordagem modular, com separação clara de responsabilidades em arquivos como `models`, `crud`, `routes` e `config`.

---

## Configuração do Projeto

### Requisitos
- Python 3.10+
- FastAPI
- SQLModel
- SQLite
- Gerenciador de dependências `uv`

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Naliat/TrabalhoPersistencia2.git
   cd TrabalhoPersistencia2
   ```
2. Ativar o ambiente virtual
```  
source .venv/bin/activate
```
3. Instale as dependências:
   ```bash
   uv install
   ```
4. Execute a aplicação:
   ```bash
   uv run app.main:app --reload
   ```

5. Acesse a documentação interativa da API no navegador:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Como Testar Usando o Postman

### Passo a Passo

1. **Configure o ambiente no Postman:**
   - Crie uma nova coleção no Postman.
   - Adicione a URL base da API: `http://127.0.0.1:8000`.

2. **Testando os Endpoints:**

#### **1. Adicionar um Fornecedor**
- **Método:** `POST`
- **Endpoint:** `/fornecedores/`
- **Body (JSON):**
  ```json
  {
      "nome": "Fornecedor A",
      "cnpj": "12345678000100",
      "telefone": "11 98765-4321",
      "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
  }
  ```
- **Resposta esperada:**
  ```json
  {
      "id": 1,
      "nome": "Fornecedor A",
      "cnpj": "12345678000100",
      "telefone": "11 98765-4321",
      "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
  }
  ```

#### **2. Listar Todos os Fornecedores**
- **Método:** `GET`
- **Endpoint:** `/fornecedores/`
- **Resposta esperada:**
  ```json
  [
      {
          "id": 1,
          "nome": "Fornecedor A",
          "cnpj": "12345678000100",
          "telefone": "11 98765-4321",
          "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
      }
  ]
  ```

#### **3. Buscar Fornecedores por Nome ou CNPJ**
- **Método:** `GET`
- **Endpoint:** `/fornecedores/busca/nome-cnpj/`
- **Query Parameters:**
  - `nome`: (opcional) Por exemplo, `Fornecedor A`
  - `cnpj`: (opcional) Por exemplo, `12345678000100`
- **Exemplo de URL:**
  ```
  http://127.0.0.1:8000/fornecedores/busca/nome-cnpj/?nome=Fornecedor%20A
  ```
- **Resposta esperada:**
  ```json
  [
      {
          "id": 1,
          "nome": "Fornecedor A",
          "cnpj": "12345678000100",
          "telefone": "11 98765-4321",
          "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
      }
  ]
  ```

#### **4. Atualizar um Fornecedor**
- **Método:** `PUT`
- **Endpoint:** `/fornecedores/{id}`
- **Body (JSON):**
  ```json
  {
      "nome": "Fornecedor A Modificado",
      "cnpj": "12345678000100",
      "telefone": "11 98765-9999",
      "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
  }
  ```
- **Resposta esperada:**
  ```json
  {
      "id": 1,
      "nome": "Fornecedor A Modificado",
      "cnpj": "12345678000100",
      "telefone": "11 98765-9999",
      "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
  }
  ```

#### **5. Deletar um Fornecedor**
- **Método:** `DELETE`
- **Endpoint:** `/fornecedores/{id}`
- **Exemplo:**
  ```
  http://127.0.0.1:8000/fornecedores/1
  ```
- **Resposta esperada:**
  ```json
  {
      "message": "Fornecedor deletado com sucesso."
  }
  ```

---

## Rotas de Estoque

### **Criar Estoque**
- **Método:** `POST`
- **URL:** `/estoque/`
- **Descrição:** Cria um novo registro de estoque.

### **Listar Todos os Estoques**
- **Método:** `GET`
- **URL:** `/estoques/`
- **Descrição:** Retorna uma lista de todos os estoques.

### **Obter Estoque Específico**
- **Método:** `GET`
- **URL:** `/estoque/{estoque_id}`
- **Descrição:** Retorna os detalhes de um estoque específico pelo ID.

### **Atualizar Estoque**
- **Método:** `PUT`
- **URL:** `/estoque/{estoque_id}`
- **Descrição:** Atualiza os dados de um estoque específico.

### **Deletar Estoque**
- **Método:** `DELETE`
- **URL:** `/estoque/{estoque_id}`
- **Descrição:** Remove um estoque específico pelo ID.

---

## Rotas de Fornecedor

### **Criar Fornecedor**
- **Método:** `POST`
- **URL:** `/fornecedor/`
- **Descrição:** Cria um novo fornecedor.

### **Listar Todos os Fornecedores**
- **Método:** `GET`
- **URL:** `/fornecedores/`
- **Descrição:** Retorna uma lista de todos os fornecedores.

### **Obter Fornecedor Específico**
- **Método:** `GET`
- **URL:** `/fornecedor/{fornecedor_id}`
- **Descrição:** Retorna os detalhes de um fornecedor específico pelo ID.

### **Buscar Fornecedores por Nome**
- **Método:** `GET`
- **URL:** `/fornecedores/busca/`
- **Parâmetro:** nome (str)
- **Descrição:** Busca fornecedores pelo nome.

### **Atualizar Fornecedor**
- **Método:** `PUT`
- **URL:** `/fornecedor/{fornecedor_id}`
- **Descrição:** Atualiza os dados de um fornecedor específico.

### **Deletar Fornecedor**
- **Método:** `DELETE`
- **URL:** `/fornecedor/{fornecedor_id}`
- **Descrição:** Remove um fornecedor específico pelo ID.

---

## Rotas de Remédio

### **Adicionar Remédio(s)**
- **Método:** `POST`
- **URL:** `/remedios/`
- **Descrição:** Adiciona um ou mais remédios.

### **Listar Todos os Remédios**
- **Método:** `GET`
- **URL:** `/remedios/`
- **Descrição:** Retorna uma lista de todos os remédios.

### **Obter Remédio Específico**
- **Método:** `GET`
- **URL:** `/remedio/{remedio_id}`
- **Descrição:** Retorna os detalhes de um remédio específico pelo ID.

### **Buscar Remédios por Nome**
- **Método:** `GET`
- **URL:** `/remedios/busca/`
- **Parâmetro:** nome (str)
- **Descrição:** Busca remédios pelo nome.

### **Listar Remédios por Validade**
- **Método:** `GET`
- **URL:** `/remedios/validade/`
- **Parâmetro:** ano (int)
- **Descrição:** Lista remédios cuja validade pertence ao ano fornecido.

### **Listar Remédios por Fornecedor**
- **Método:** `GET`
- **URL:** `/fornecedor/{fornecedor_id}/remedios/`
- **Descrição:** Lista os remédios fornecidos por um fornecedor específico.

### **Atualizar Remédio**
- **Método:** `PUT`
- **URL:** `/remedio/{remedio_id}`
- **Descrição:** Atualiza os dados de um remédio específico.

---

## Estrutura de Dados de Teste

### Fornecedores Preexistentes
A base de dados inicial contém os seguintes fornecedores para teste:

```json
[
    {
        "id": 1,
        "nome": "Fornecedor A",
        "cnpj": "12345678000100",
        "telefone": "11 98765-4321",
        "endereco": "Rua A, 123, Bairro A, São Paulo, SP"
    },
    {
        "id": 2,
        "nome": "Fornecedor B",
        "cnpj": "98765432000199",
        "telefone": "11 99876-5432",
        "endereco": "Rua B, 456, Bairro B, São Paulo, SP"
    }
]
```

---

## População estoque
```
[
  {
    "remedio_id": 1,
    "quantidade": 100,
    "data_entrada_estoque": "2025-01-01T12:00:00Z",
    "validade": "2025-12-31T23:59:59Z"
  },
  {
    "remedio_id": 2,
    "quantidade": 200,
    "data_entrada_estoque": "2025-01-02T10:00:00Z",
    "validade": "2026-01-01T23:59:59Z"
  },
  {
    "remedio_id": 3,
    "quantidade": 50,
    "data_entrada_estoque": "2025-01-03T09:00:00Z",
    "validade": "2025-09-01T23:59:59Z"
  },
  {
    "remedio_id": 4,
    "quantidade": 75,
    "data_entrada_estoque": "2025-01-04T08:00:00Z",
    "validade": "2025-08-01T23:59:59Z"
  },
  {
    "remedio_id": 5,
    "quantidade": 120,
    "data_entrada_estoque": "2025-01-05T07:30:00Z",
    "validade": "2025-07-01T23:59:59Z"
  },
  {
    "remedio_id": 6,
    "quantidade": 90,
    "data_entrada_estoque": "2025-01-06T14:00:00Z",
    "validade": "2026-02-01T23:59:59Z"
  },
  {
    "remedio_id": 7,
    "quantidade": 60,
    "data_entrada_estoque": "2025-01-07T13:00:00Z",
    "validade": "2025-06-01T23:59:59Z"
  },
  {
    "remedio_id": 8,
    "quantidade": 150,
    "data_entrada_estoque": "2025-01-08T11:00:00Z",
    "validade": "2026-03-01T23:59:59Z"
  },
  {
    "remedio_id": 9,
    "quantidade": 40,
    "data_entrada_estoque": "2025-01-09T15:00:00Z",
    "validade": "2025-05-01T23:59:59Z"
  },
  {
    "remedio_id": 10,
    "quantidade": 300,
    "data_entrada_estoque": "2025-01-10T16:00:00Z",
    "validade": "2026-04-01T23:59:59Z"
  }
]
```

População da entidade Remédio

```

```

População da tabela fornecedor

```

```
