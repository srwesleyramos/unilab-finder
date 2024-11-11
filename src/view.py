from os import system
from time import sleep

from map import Map
from type import Type


#
# Renderizar apenas o mapa
#

def renderRaw(grid):
    print()
    print("─" * (len(grid[0]) * 2 + 3))

    for rows in grid:
        print(f"│ {" ".join(list(map(lambda obj: obj.getIcon(), rows)))} |")

    print("─" * (len(grid[0]) * 2 + 3))
    print()


#
# Atualizar grid e renderizar mapa
#

def executeQueue(grid, position, queue):
    while len(queue) > 0:
        system('cls')

        grid[position[0]][position[1]] = Type.LIVRE

        position = queue.pop(0)

        grid[position[0]][position[1]] = Type.ROBO

        renderRaw(grid)

        sleep(0.300)


#
# Renderizar o robô indo para o queijo e voltando
#

def renderPath(world: Map):
    # Copiando a matriz para outro objeto

    grid = [row[::] for row in world.grid]

    # Criando a fila com as posições #1

    position = world.robot[0]
    queue = [row[::] for row in world.find(position, Type.QUEIJO, [])]

    executeQueue(grid, position, queue)

    # Criando a fila com as posições #2

    position = world.cheese[0]
    queue = [row[::] for row in world.find(position, Type.ROBO, [])]

    executeQueue(grid, position, queue)
