from os import system
from time import sleep

from map import Map
from type import Type


#
# Renderizar apenas o mapa
#

def render_raw(grid):
    print()
    print("─" * (len(grid[0]) * 2 + 3))

    for rows in grid:
        print(f"│ {" ".join(list(map(lambda obj: obj.icon(), rows)))} |")

    print("─" * (len(grid[0]) * 2 + 3))
    print()


#
# Atualizar grid e renderizar mapa
#

def execute_queue(grid, position, queue):
    while len(queue) > 0:
        system('cls')

        grid[position[0]][position[1]] = Type.LIVRE

        position = queue.pop(0)

        grid[position[0]][position[1]] = Type.ROBO

        render_raw(grid)

        sleep(0.300)


#
# Renderizar o robô indo para o queijo e voltando
#

def render_path(world: Map):
    # Copiando a matriz para outro objeto

    grid = [row[::] for row in world.grid]

    # Criando a fila com as posições #1

    position = world.robot[0]
    queue = world.find(position, Type.QUEIJO, [])
    execute_queue(grid, position, queue)

    # Criando a fila com as posições #2

    position = world.cheese[0]
    queue = world.find(position, Type.ROBO, [])
    execute_queue(grid, position, queue)
