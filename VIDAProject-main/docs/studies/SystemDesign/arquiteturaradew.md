# Arquitetura de Software
É importante fazer a arquitetura no dia 0 do projeto, a arquitetura é o planejamento de como os componentes de um sistema interagem entre si
É um mapa simples que dá uma ideia geral de quais componentes interagem entre si, o que cada tipo de usuário (cliente e adm) vai ter acesso, etc
## 3 fases
- Analise do problema
- Brainstorm de varias possíveis soluções
- Avaliação das decisões tomadas
# Aruqitetura Simples
Não tem muito o que falar é só padrão mesmo
![arq simples](https://github.com/user-attachments/assets/ab424ac7-52fc-4a53-bdae-53060e1074d9)
# Arquitetura em Camadas
Não tem limite de camadas, mas não pode exagerar; as camadas devem ser claras em suas funções
- Controler
- 	Responsável por gerenciar as requisições e respostas do sistema
- Service
-	Responsável por todas as regras de negocio
- Repository
- 	Responsável por operações com bancos de dados
- Entity
-	representação da tabela do banco de dados
Pode ser resumido em Arquitetura hexagonal e clean
# Arquitetura Hexagonal
O fato de ser um hexagono é meramente ilustrativo
![hexagonal](https://github.com/user-attachments/assets/312b72c7-4fd3-49f1-a5c9-fb9b72435296)
O sistema é feito em camadas que se comunicam em portas e adaptadores
É como se cada parte do software fosse uma peça que so se conecta em seu respectivo lugar
Mantem o domínio protegido enquanto a interação com o cliente é limitada à portas e adaptadores
- Portas e Adaptadores
- Primary Adapters
Recebem e enviam os dados para a aplicação
- Secondary Adapters
Levam os dados para fora da aplicação
Arquitetura Clean é basicamente um passo a mais da Hexagonal, onde as estruturas são mais bem divididas
