# Big O Notation — Resumo

## Conceito geral

- Big O não é uma medida de performance absoluta, mas sim de **escalabilidade**.
- Descreve como o tempo de execução ou uso de memória cresce com o tamanho da entrada (n).
- A análise assintótica observa o comportamento do algoritmo conforme _n → ∞_.
- Tipos de complexidade:
  - **Temporal:** tempo de execução.
  - **Espacial:** memória usada adicionalmente.

---

## 🕒 Complexidade Temporal (Tempo de execução)

- **O(1) — Constante**

  - Tempo não varia com o tamanho da entrada.
  - Ex.: Acessar o primeiro elemento de um array (`arr[0]`).

- **O(log n) — Logarítmica**

  - Cresce lentamente conforme aumenta n.
  - Ex.: Busca binária (Binary Search).

- **O(n) — Linear**

  - Cresce proporcionalmente ao tamanho da entrada.
  - Ex.: Percorrer todos os elementos de um array.

- **O(n log n) — Quase linear**

  - Cresce mais rápido que linear, mas ainda eficiente.
  - Ex.: Merge Sort, Quick Sort (em média).

- **O(n²) — Quadrática**

  - Cresce com o quadrado do tamanho da entrada.
  - Ex.: Bubble Sort, Selection Sort (loops aninhados).

- **O(n³) — Cúbica**

  - Três loops aninhados.
  - Ex.: Multiplicação de matrizes ingênua.

- **O(2ⁿ) — Exponencial**

  - O tempo dobra a cada elemento adicional.
  - Ex.: Força bruta para subconjuntos ou combinações.

- **O(n!) — Fatorial**
  - Cresce mais rápido que exponencial.
  - Ex.: Gerar todas as permutações de uma lista.

---

## 💾 Complexidade Espacial (Uso de memória)

- **O(1) — Constante**

  - Memória fixa, independente de n.
  - Ex.: Encontrar o maior elemento de um array (apenas uma variável extra).

- **O(log n) — Logarítmica**

  - Memória proporcional à profundidade da recursão.
  - Ex.: Busca binária recursiva.

- **O(n) — Linear**

  - Memória proporcional ao tamanho da entrada.
  - Ex.: Criar uma cópia de um array.

- **O(n log n) — Quase linear**

  - Uso moderado de memória.
  - Ex.: Merge Sort (subarrays temporários).

- **O(n²) — Quadrática**
  - Memória proporcional ao quadrado da entrada.
  - Ex.: Matrizes NxN, grafos com matriz de adjacência.

---

### 💡 Dicas rápidas

- Ordem de crescimento: **Constante < Logarítmica < Linear < Quase linear < Quadrática < Cúbica < Exponencial < Fatorial**
- Big O considera **a ordem dominante**, ignorando constantes e termos menores.
- Ex.: `O(2n + 10)` → simplificado para `O(n)`.
