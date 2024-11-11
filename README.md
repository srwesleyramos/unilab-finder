# Trabalho Final - Simulação de Robô Rato

Desenvolva um programa para simular um robô rato em busca de queijo em diferentes mapas. O programa deve permitir a importação de mapas e a visualização do caminho do robô até o objetivo. Além de encontrar o queijo, o robô deve retornar à posição inicial. Funções adicionais devem fornecer dados quantitativos e informativos sobre o mapa e as ações do robô.

## Requisitos do Programa

1. **Representação do Mapa**
    - O mapa será representado por uma matriz de dados.
    - Os elementos do mapa são: espaço livre, parede, robô e queijo.
    - Cada elemento será representado por um índice inteiro:
        - 1: parede
        - 0: espaço livre
        - 7: robô
        - 9: queijo


2. **Configuração do Mapa**
    - O mapa pode ter dimensões e quantidades variadas de elementos.
    - Cada mapa terá apenas um robô e um queijo, com posições já definidas.
    - Os mapas serão importados a partir de arquivos de texto.


3. **Resultados**
    - O programa deve exibir o caminho do robô até o queijo como uma sequência de coordenadas e o total de passos.
    - O robô será testado em três mapas de tamanhos variados.

## Menu do Programa

1. **Importar Mapa**
    - Permitir ao usuário digitar o nome ou o caminho do arquivo do mapa.


2. **Apresentar Mapa Atual**
    - Exibir visualmente o mapa importado.
    - Caso não haja um mapa carregado, informar ao usuário.


3. **Gerar Mapa Aleatório**
    - Criar um mapa aleatório seguindo as regras de ter um robô e um queijo.


4. **Verificar Viabilidade do Mapa**
    - Analisar se o robô consegue encontrar o queijo no mapa atual.


5. **Caminho ao Objetivo**
    - Mostrar o caminho do robô da posição inicial até o queijo.


6. **Caminho de Retorno**
    - Exibir o caminho de volta do robô da posição do queijo até a inicial.


7. **Apresentar Graficamente o Percurso**
    - Exibir a trajetória do robô no mapa, passo a passo.


8. **Dados Informativos**
    - Posição inicial do robô.
    - Posição do queijo.
    - Dimensão do mapa (ex: 8x9) e contagem de paredes, robôs e queijos.
    - Quantidade de passos para atingir o objetivo e retornar à posição inicial.
    - Total de passos para encontrar o queijo e retornar ao ponto de partida.

## Restrições

1. O robô não conhece a posição do queijo, devendo buscar exploratoriamente.

2. Movimentos são restritos a passos horizontais ou verticais.

3. Diagonais não são permitidas.

4. O robô só pode mover-se por espaços livres (0) ou pela posição do queijo (9).

5. Cada opção do menu deve ser implementada como uma função independente, incluindo o menu.