# Spring Ava

O **Spring Ava** é uma ferramenta de automação para a geração de código CRUD no Spring. Durante o desenvolvimento de um projeto, muitas vezes seguimos uma estrutura padrão para manipulação de entidades. Por exemplo, ao criar um CRUD em Java para uma entidade, como **Produto**, normalmente seguimos as seguintes etapas:

## Estrutura Padrão de CRUD

1. **Entidade (ProdutoEntity)**  
   Criamos uma classe que representa a entidade que será mapeada para o banco de dados (ex: `Produto`, `ProdutoModel`, `ProdutoEntity`). Esta classe geralmente inclui atributos como ID, nome, data de criação e data de atualização.

2. **DTO (ProdutoDTO)**  
   Criamos um **DTO** (Data Transfer Object), que serve para mapear os dados necessários para criar ou atualizar a entidade. O **ProdutoDTO** é usado para transferir dados entre camadas da aplicação sem incluir a lógica de persistência.

3. **Repositório (ProdutoRepository)**  
   Criamos uma interface que estende **JPARepository** para facilitar as operações de banco de dados relacionadas à entidade. Por exemplo, o repositório `ProdutoRepository` oferece funcionalidades como salvar, buscar, atualizar e deletar registros.

4. **Serviço (ProdutoService)**  
   A camada de serviço é responsável pela lógica de negócios da aplicação. Normalmente, inclui os seguintes métodos:
   - `findById(Long id)`
   - `findAll(Pageable page)`
   - `save(ProdutoDTO dto)`
   - `update(Long id, ProdutoDTO dto)`
   - `delete(Long id)`

5. **Controlador (ProdutoController)**  
   A camada de controle gerencia as requisições HTTP. Cada método do serviço é mapeado para um endpoint específico, como:
   - `findById(Long id)` -> `/produtos/{id}`
   - `findAll(Pageable page)` -> `/produtos`
   - `save(ProdutoDTO dto)` -> `/produtos`
   - `update(Long id, ProdutoDTO dto)` -> `/produtos/{id}`
   - `delete(Long id)` -> `/produtos/{id}`

## Automação do Processo

Essas etapas, embora essenciais, costumam ser repetitivas e demoradas. Inspirado no **Laravel**, o **Spring Ava** foi desenvolvido para automatizar esse processo. Com um simples comando de linha, o projeto gera toda a camada de código repetitiva necessária para criar um CRUD completo no Spring.

## Como Usar
em desenvolvimento...
