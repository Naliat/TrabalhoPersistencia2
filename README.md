# Aplicação FastAPI para Gerenciamento de Remédios

## Descrição

Esta aplicação, desenvolvida com **FastAPI**, utiliza **SQLModel** e **SQLite** para gerenciar informações de fornecedores. A API permite realizar operações CRUD (Create, Read, Update, Delete) e inclui consultas avançadas, como a busca de fornecedores por nome ou CNPJ.

A estrutura segue uma abordagem modular, com separação clara de responsabilidades em arquivos como `models` e `routes` 

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


### Populando a entidade Remédio
```

```



## Resultado esperado População da entidade Remédio
```
[
    {
        "id": 1,
        "validade": "2025-12-31",
        "created_at": "2025-01-17T19:26:42.865320",
        "fornecedor_id": 1,
        "nome": "Dipirona",
        "descricao": "Analgésico e antipirético",
        "preco": 10.5,
        "updated_at": "2025-01-17T19:51:47.075628"
    },
    {
        "id": 2,
        "validade": "2026-06-30",
        "created_at": "2025-01-17T19:26:42.865488",
        "fornecedor_id": 2,
        "nome": "Ibuprofeno",
        "descricao": "Anti-inflamatório",
        "preco": 15.75,
        "updated_at": "2025-01-17T19:26:42.865497"
    },
    {
        "id": 3,
        "validade": "2025-07-15",
        "created_at": "2025-01-17T19:26:42.865575",
        "fornecedor_id": 1,
        "nome": "Dipirona",
        "descricao": "Analgésico e antitérmico",
        "preco": 8.0,
        "updated_at": "2025-01-17T19:26:42.865584"
    },
    {
        "id": 4,
        "validade": "2026-03-10",
        "created_at": "2025-01-17T19:26:42.865656",
        "fornecedor_id": 3,
        "nome": "Amoxicilina",
        "descricao": "Antibiótico",
        "preco": 25.0,
        "updated_at": "2025-01-17T19:26:42.865665"
    },
    {
        "id": 5,
        "validade": "2025-11-01",
        "created_at": "2025-01-17T19:26:42.865736",
        "fornecedor_id": 4,
        "nome": "Losartana",
        "descricao": "Antihipertensivo",
        "preco": 45.0,
        "updated_at": "2025-01-17T19:26:42.865745"
    },
    {
        "id": 6,
        "validade": "2025-08-20",
        "created_at": "2025-01-17T19:26:42.865818",
        "fornecedor_id": 5,
        "nome": "Loratadina",
        "descricao": "Antialérgico",
        "preco": 12.0,
        "updated_at": "2025-01-17T19:26:42.865827"
    },
    {
        "id": 7,
        "validade": "2026-01-12",
        "created_at": "2025-01-17T19:26:42.865907",
        "fornecedor_id": 3,
        "nome": "Omeprazol",
        "descricao": "Inibidor de bomba de prótons",
        "preco": 20.0,
        "updated_at": "2025-01-17T19:26:42.865916"
    },
    {
        "id": 8,
        "validade": "2025-04-22",
        "created_at": "2025-01-17T19:26:42.865984",
        "fornecedor_id": 6,
        "nome": "Sertralina",
        "descricao": "Antidepressivo",
        "preco": 35.0,
        "updated_at": "2025-01-17T19:26:42.865993"
    },
    {
        "id": 9,
        "validade": "2025-02-18",
        "created_at": "2025-01-17T19:26:42.866059",
        "fornecedor_id": 4,
        "nome": "Atorvastatina",
        "descricao": "Redutor de colesterol",
        "preco": 50.0,
        "updated_at": "2025-01-17T19:26:42.866068"
    },
    {
        "id": 10,
        "validade": "2026-09-05",
        "created_at": "2025-01-17T19:26:42.866142",
        "fornecedor_id": 2,
        "nome": "Cloridrato de Ranitidina",
        "descricao": "Antiácido",
        "preco": 18.0,
        "updated_at": "2025-01-17T19:26:42.866151"
    },
    {
        "id": 11,
        "validade": "2025-12-31",
        "created_at": "2025-01-17T23:08:26.824151",
        "fornecedor_id": 1,
        "nome": "Dipirona",
        "descricao": "Analgésico e antipirético",
        "preco": 10.5,
        "updated_at": "2025-01-17T23:08:26.824165"
    },
    {
        "id": 12,
        "validade": "2025-12-31",
        "created_at": "2025-01-17T23:08:38.651943",
        "fornecedor_id": 1,
        "nome": "Dipirona",
        "descricao": "Analgésico e antipirético",
        "preco": 10.5,
        "updated_at": "2025-01-17T23:08:38.651956"
    }
]
```

Populando tabela fornecedor

```
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
  },
  {
    "id": 3,
    "nome": "Fornecedor C",
    "cnpj": "45678912000158",
    "telefone": "21 99887-6543",
    "endereco": "Avenida C, 789, Bairro C, Rio de Janeiro, RJ"
  },
  {
    "id": 4,
    "nome": "Fornecedor D",
    "cnpj": "34567891000123",
    "telefone": "21 97765-4321",
    "endereco": "Rua D, 101, Bairro D, Rio de Janeiro, RJ"
  },
  {
    "id": 5,
    "nome": "Fornecedor E",
    "cnpj": "56789012345678",
    "telefone": "31 98876-5432",
    "endereco": "Praça E, 123, Bairro E, Belo Horizonte, MG"
  },
  {
    "id": 6,
    "nome": "Fornecedor F",
    "cnpj": "12349012347898",
    "telefone": "41 98765-9876",
    "endereco": "Rua F, 321, Bairro F, Curitiba, PR"
  },
  {
    "id": 7,
    "nome": "Fornecedor G",
    "cnpj": "65431208765432",
    "telefone": "61 97765-4321",
    "endereco": "Rua G, 432, Bairro G, Brasília, DF"
  },
  {
    "id": 8,
    "nome": "Fornecedor H",
    "cnpj": "23456789001234",
    "telefone": "51 99665-4321",
    "endereco": "Avenida H, 654, Bairro H, Porto Alegre, RS"
  },
  {
    "id": 9,
    "nome": "Fornecedor I",
    "cnpj": "76543210987654",
    "telefone": "48 99664-3322",
    "endereco": "Rua I, 789, Bairro I, Florianópolis, SC"
  },
  {
    "id": 10,
    "nome": "Fornecedor J",
    "cnpj": "87654321000012",
    "telefone": "85 98876-5432",
    "endereco": "Rua J, 567, Bairro J, Fortaleza, CE"
  }
]

```

Resultado esperado aṕos popular aa entidade Fornecedor

```
[
    {
        "cnpj": "12345678000100",
        "telefone": "11 99999-9999",
        "endereco": "Rua L, 987, Bairro L, Campinas, SP",
        "nome": "Fornecedor A",
        "id": 1
    },
    {
        "cnpj": "98765432000199",
        "telefone": "11 99876-5432",
        "endereco": "Rua B, 456, Bairro B, São Paulo, SP",
        "nome": "Fornecedor B",
        "id": 2
    },
    {
        "cnpj": "45678912000158",
        "telefone": "21 99887-6543",
        "endereco": "Avenida C, 789, Bairro C, Rio de Janeiro, RJ",
        "nome": "Fornecedor C",
        "id": 3
    },
    {
        "cnpj": "34567891000123",
        "telefone": "21 97765-4321",
        "endereco": "Rua D, 101, Bairro D, Rio de Janeiro, RJ",
        "nome": "Fornecedor D",
        "id": 4
    },
    {
        "cnpj": "56789012345678",
        "telefone": "31 98876-5432",
        "endereco": "Praça E, 123, Bairro E, Belo Horizonte, MG",
        "nome": "Fornecedor E",
        "id": 5
    },
    {
        "cnpj": "12349012347898",
        "telefone": "41 98765-9876",
        "endereco": "Rua F, 321, Bairro F, Curitiba, PR",
        "nome": "Fornecedor F",
        "id": 6
    },
    {
        "cnpj": "65431208765432",
        "telefone": "61 97765-4321",
        "endereco": "Rua G, 432, Bairro G, Brasília, DF",
        "nome": "Fornecedor G",
        "id": 7
    },
    {
        "cnpj": "23456789001234",
        "telefone": "51 99665-4321",
        "endereco": "Avenida H, 654, Bairro H, Porto Alegre, RS",
        "nome": "Fornecedor H",
        "id": 8
    },
    {
        "cnpj": "76543210987654",
        "telefone": "48 99664-3322",
        "endereco": "Rua I, 789, Bairro I, Florianópolis, SC",
        "nome": "Fornecedor I",
        "id": 9
    },
    {
        "cnpj": "87654321000012",
        "telefone": "85 98876-5432",
        "endereco": "Rua J, 567, Bairro J, Fortaleza, CE",
        "nome": "Fornecedor J",
        "id": 10
    }
]
```

### Populando a entidade Estoque

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
### Resultado esperado aṕos popular a entidade estoque

```
[
    {
        "validade": "2025-12-31T23:59:59",
        "id": 1,
        "data_entrada_estoque": "2025-01-01T12:00:00",
        "quantidade": 100,
        "remedio_id": 1
    },
    {
        "validade": "2026-01-01T23:59:59",
        "id": 2,
        "data_entrada_estoque": "2025-01-02T10:00:00",
        "quantidade": 200,
        "remedio_id": 2
    },
    {
        "validade": "2025-09-01T23:59:59",
        "id": 3,
        "data_entrada_estoque": "2025-01-03T09:00:00",
        "quantidade": 50,
        "remedio_id": 3
    },
    {
        "validade": "2025-08-01T23:59:59",
        "id": 4,
        "data_entrada_estoque": "2025-01-04T08:00:00",
        "quantidade": 75,
        "remedio_id": 4
    },
    {
        "validade": "2025-07-01T23:59:59",
        "id": 5,
        "data_entrada_estoque": "2025-01-05T07:30:00",
        "quantidade": 120,
        "remedio_id": 5
    },
    {
        "validade": "2026-02-01T23:59:59",
        "id": 6,
        "data_entrada_estoque": "2025-01-06T14:00:00",
        "quantidade": 90,
        "remedio_id": 6
    },
    {
        "validade": "2025-06-01T23:59:59",
        "id": 7,
        "data_entrada_estoque": "2025-01-07T13:00:00",
        "quantidade": 60,
        "remedio_id": 7
    },
    {
        "validade": "2026-03-01T23:59:59",
        "id": 8,
        "data_entrada_estoque": "2025-01-08T11:00:00",
        "quantidade": 150,
        "remedio_id": 8
    },
    {
        "validade": "2025-05-01T23:59:59",
        "id": 9,
        "data_entrada_estoque": "2025-01-09T15:00:00",
        "quantidade": 40,
        "remedio_id": 9
    },
    {
        "validade": "2026-04-01T23:59:59",
        "id": 10,
        "data_entrada_estoque": "2025-01-10T16:00:00",
        "quantidade": 300,
        "remedio_id": 10
    }
]
```

