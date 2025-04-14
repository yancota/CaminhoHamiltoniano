# Caminho Hamiltoniano

Implementação de um algoritmo para encontrar um Caminho Hamiltoniano em grafos orientados ou não orientados, utilizando a linguagem Python.

## Como rodar o projeto

Instalar a última versão do python disponível em: https://www.python.org/downloads/

Necessário rodar o seguinte comando no terminal:
```bash
https://github.com/yancota/CaminhoHamiltoniano.git
```

Rodar o seguinte comando no terminal:
```bash
python main.py
```

## Versão do Python
Este projeto foi desenvolvido na versão 3.13.2 do Python.

## Explicação das funções

### Arquivo: main.py

- **Descrição das funções:**

#### verificar_caminho_hamiltoniano(grafo, trilha, visitados)
- **Objetivo:**
  - Realizar uma busca recursiva com backtracking para verificar se há um Caminho Hamiltoniano a partir do vértice atual.
- **Parâmetros:**
  - grafo: dicionário que representa o grafo (lista de adjacência);
  - trilha: lista com a sequência de vértices visitados no caminho atual;
  - visitados: dicionário booleano que indica se um vértice já foi visitado.
- **Lógica:**
  - Caso base: Se o comprimento da trilha for igual ao número de vértices do grafo, então encontramos um Caminho Hamiltoniano e retornamos True.
  - Iteramos sobre os vizinhos do vértice atual (trilha[-1]).
  - Para cada vizinho não visitado:
     - Marcamos como visitado;
     - Adicionamos à trilha;
     - Chamamos recursivamente a função;
     - Se a chamada retornar True, encerramos.
     - Caso contrário, desfazemos a escolha (backtracking).
  - Se nenhum vizinho resultar em sucesso, retornamos False.

- **Retorno:**
  - True se existir um Caminho Hamiltoniano a partir do ponto atual;
  - False caso contrário.

#### buscar_caminho_hamiltoniano(grafo)
- **Objetivo:**
  - Tentar iniciar um Caminho Hamiltoniano a partir de cada vértice do grafo, retornando o caminho se encontrado.
- **Parâmetros:**
  - grafo: dicionário representando a lista de adjacência do grafo.
- **Lógica:**
  - Percorremos cada vértice do grafo como ponto de partida.
  - Inicializamos o dicionário de visitados e a trilha contendo o vértice inicial.
  - Chamamos a função verificar_caminho_hamiltoniano() para tentar construir o caminho completo.
  - Se for bem-sucedida, retornamos a trilha encontrada.
  - Se nenhum vértice for capaz de formar um Caminho Hamiltoniano, retornamos None.

- **Retorno:**
  - Uma lista contendo o Caminho Hamiltoniano encontrado;
  - None caso não exista caminho possível.

## Entrada do Programa
- O grafo é definido diretamente no código como um dicionário onde:
  - As chaves representam os vértices;
  - Os valores são listas com os vértices vizinhos.
- Exemplo:
```bash
  grafo_exemplo = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
```
  
## Saída da Execução

- Se um Caminho Hamiltoniano for encontrado:
  - Saída: "Caminho Hamiltoniano encontrado: [0, 1, 3, 2]"
- Se nenhum Caminho Hamiltoniano existir:
  - Saída: "Não existe Caminho Hamiltoniano."


## Complexidade

### Ciclos de Complexidae
- O problema do Caminho Hamiltoniano pertence à classe NP-completo.
- É NP porque, dado um caminho, podemos verificar em tempo polinomial se ele visita todos os vértices exatamente uma vez.
- É NP-completo porque é tão difícil quanto qualquer outro problema em NP (reduzível ao Caixeiro Viajante, que também é NP-completo).

### Complexidade Assintótica de Tempo
- O algoritmo implementado usa backtracking, com complexidade de tempo O(n!), onde n é o número de vértices.

### Teorema Mestre
- O Teorema Mestre se aplica a algoritmos divisão-e-conquista, mas o algoritmo de backtracking não segue uma recursão do tipo

### Análise dos Casos
- Melhor:  O primeiro caminho testado já é Hamiltoniano	
  - O(n²)
- Médio: O caminho é encontrado após testar algumas combinações	
  - O(k * n²)
- Pior: Nenhum caminho é Hamiltoniano	
  - O(n!)

- Obs.: para grafos maiores, o tempo cresce exponencialmente.
