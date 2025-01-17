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

2. Instale as dependências:
   ```bash
   uv install
   ```

3. Execute a aplicação:
   ```bash
   uv run app.main:app --reload
   ```

4. Acesse a documentação interativa da API no navegador:
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

## Observações
- Certifique-se de que o servidor está em execução antes de realizar os testes.
- Utilize o Swagger UI para explorar e testar os endpoints de maneira interativa.
- Para questões ou problemas, abra uma *issue* no repositório GitHub.

---

## Autor
Tailan

---

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.