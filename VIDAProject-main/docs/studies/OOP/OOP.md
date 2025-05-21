# Programação Orientada a Objetos
É a área da programação que busca simplificar o código para torna-lo mais fácil de fazer alterações futuras. Ao invés de encaixar tudo em um bloco de texto, o código é divido em várias classes, semelhante à programação procedural mas com foco em criações de objetos.

## Definições gerais
![Captura de tela 2025-04-03 222905](https://github.com/user-attachments/assets/532b727e-8257-4e7f-9d08-2d934339ab98)

- Objetos:
São instâncias de uma classe, um acumulo de atributos específicos para cada objeto e métodos comuns a todos.

- Classe:
Molde onde cada objeto é criado

- Atributos:
Dados e variáveis

- Métodos:
funções que o objeto pode executar

- Herança:
Quando se cria uma classe, pode-se faze-la herdar de outra classe, significa que ela possuíra atributos e métodos da "classe-pai"

![Captura de tela 2025-04-03 224726](https://github.com/user-attachments/assets/d7faef86-1612-47a3-8666-7de12c9afd90)

- Polimorfismo:
Quando uma classe herda um método, ela pode reescreve-la e adapta-la às suas necessidades

- Encapsulamento:
Proteger os dados de um objeto, fazendo com que seja apenas possível modifica-los através de métodos set() e coleta-los com métodos get(). Assim o atributo se torna menos suscetível a erros; no geral é só uma boa prática.

![Captura de tela 2025-04-03 225408](https://github.com/user-attachments/assets/de13d976-c52e-4767-bc2a-ef2c06444d2e)
![Captura de tela 2025-04-03 233139](https://github.com/user-attachments/assets/cdae5727-09bd-43c0-a4bd-768364585c1c)



## Acomplamento x Coesão
- Acoplamento:
Interdependência entre duas ou mais classes em um sistema.
  - Se o sistema estiver muito acoplado, quando modificar algo, vai afetar varias outras classes, assim o código fica ruim de modificar/corrigir alguma parte

- Coesão:
Grau em que os elementos dentro de uma classe estão relacionados, membros de uma classe que se relacionam e colaboram em uma única função, promove que cada classe tenha uma responsabilidade clara e bem definida
  - Uma boa prática é limitar cada classe a uma responsabilidade simples e direta
    
De forma resumida, acoplamento e coesão são a mesma coisa feita de jeitos diferentes. A ideia é achar um equilíbrio entre ambas; usar a coesão para que cada classe ter sua função especifica, assim se algo precisar mudar, o programador saberá exatamente onde procurar, mas sem exagerar, para que o código não se torne excessivamente acoplado e não precise modificar varias classes de uma só vez.

## Associação
- Agregação:
um objeto possui outro como atributo simplesmente

- Composição:
um objeto é dono de outro objeto e suas existência se tornam dependentes.
Nesse caso motor só existe por causa do carro e quando o carro for deletado, seu respectivo motor será deletado também

![Captura de tela 2025-04-03 225644](https://github.com/user-attachments/assets/4b154ffd-7d12-418c-b1d3-a0f739571eff)

- Dependência:
Uma classe depende de outra para funcionar corretamente; parecido com a composição, mas os objetos podem existir sozinhos, só que seus métodos vão ser afetados.
