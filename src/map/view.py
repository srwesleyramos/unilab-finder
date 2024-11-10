import os
import time
from typing import List

from colorama import init, Fore, Style

from src.map.map import Map
from src.map.type import Type

init(autoreset=True)


def renderMap(world: List[List[str]]):
    # TODO: refatorar toda a função

    print("")
    print(f"+{"─" * (len(world[0]) * 2 + 1)}+")

    for rows in world:
        print("│", end=" ")

        for column in rows:
            if column == "0":
                column = Fore.BLACK + column + Style.RESET_ALL

            if column == "1":
                column = Fore.LIGHTBLACK_EX + column + Style.RESET_ALL

            if column == "7":
                column = Fore.MAGENTA + column + Style.RESET_ALL

            if column == "9":
                column = Fore.YELLOW + column + Style.RESET_ALL

            print(column, end=" ")

        print("│")

    print(f"+{"─" * (len(world[0]) * 2 + 1)}+")
    print()


def renderQueue(grid, robot, queue):
    while len(queue) > 0:
        os.system('cls')

        grid[robot[0]][robot[1]] = '0'

        robot = queue.pop(0)

        grid[robot[0]][robot[1]] = '7'

        renderMap(grid)

        time.sleep(0.300)


def renderPath(world: Map):
    # Copiando a matriz para outro objeto

    grid = [row[:] for row in world.grid]

    # Criando a fila com as posições #1

    robot = world.robot[0]
    queue = [row[:] for row in world.find(robot, Type.QUEIJO, [])]

    renderQueue(grid, robot, queue)

    # Criando a fila com as posições #2

    robot = world.cheese[0]
    queue = [row[:] for row in world.find(robot, Type.ROBO, [])]

    renderQueue(grid, robot, queue)
