Rotas de Estoque
Criar estoque

Método: POST
URL: /estoque/
Descrição: Cria um novo registro de estoque.
Listar todos os estoques

Método: GET
URL: /estoques/
Descrição: Retorna uma lista de todos os estoques.
Obter estoque específico

Método: GET
URL: /estoque/{estoque_id}
Descrição: Retorna os detalhes de um estoque específico pelo ID.
Atualizar estoque

Método: PUT
URL: /estoque/{estoque_id}
Descrição: Atualiza os dados de um estoque específico.
Deletar estoque

Método: DELETE
URL: /estoque/{estoque_id}
Descrição: Remove um estoque específico pelo ID.
Rotas de Fornecedor
Criar fornecedor

Método: POST
URL: /fornecedor/
Descrição: Cria um novo fornecedor.
Listar todos os fornecedores

Método: GET
URL: /fornecedores/
Descrição: Retorna uma lista de todos os fornecedores.
Obter fornecedor específico

Método: GET
URL: /fornecedor/{fornecedor_id}
Descrição: Retorna os detalhes de um fornecedor específico pelo ID.
Buscar fornecedores por nome

Método: GET
URL: /fornecedores/busca/
Parâmetro: nome (str)
Descrição: Busca fornecedores pelo nome.
Atualizar fornecedor

Método: PUT
URL: /fornecedor/{fornecedor_id}
Descrição: Atualiza os dados de um fornecedor específico.
Deletar fornecedor

Método: DELETE
URL: /fornecedor/{fornecedor_id}
Descrição: Remove um fornecedor específico pelo ID.
Rotas de Remédio
Adicionar remédio(s)

Método: POST
URL: /remedios/
Descrição: Adiciona um ou mais remédios.
Listar todos os remédios

Método: GET
URL: /remedios/
Descrição: Retorna uma lista de todos os remédios.
Obter remédio específico

Método: GET
URL: /remedio/{remedio_id}
Descrição: Retorna os detalhes de um remédio específico pelo ID.
Buscar remédios por nome

Método: GET
URL: /remedios/busca/
Parâmetro: nome (str)
Descrição: Busca remédios pelo nome.
Listar remédios por validade

Método: GET
URL: /remedios/validade/
Parâmetro: ano (int)
Descrição: Lista remédios cuja validade pertence ao ano fornecido.
Listar remédios por fornecedor

Método: GET
URL: /fornecedor/{fornecedor_id}/remedios/
Descrição: Lista os remédios fornecidos por um fornecedor específico.
Atualizar remédio

Método: PUT
URL: /remedio/{remedio_id}
Descrição: Atualiza os dados de um remédio específico.
