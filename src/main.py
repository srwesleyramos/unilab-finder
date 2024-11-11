from os import system
from time import sleep

import view
from map import Map
from test import generate
from type import Type


def menu():
    sleep(3)
    system('cls')

    print()
    print("   CALCULADORA DE PERCURSO")
    print("      by @srwesleyramos")
    print()
    print("  1. Importar mapa")
    print("  2. Apresentar mapa atual")
    print("  3. Gerar mapa aleatório")
    print("  4. Verificar viabilidade")
    print("  5. Caminho ao objetivo")
    print("  6. Caminho de retorno")
    print("  7. Apresentar percurso")
    print("  8. Apresentar dados")
    print()

    option = input("  >> ")

    if option == "1":
        importMap()
    elif option == "3":
        generateMap()
    else:
        if world is None:
            print()
            print(" O mapa ainda não foi carregado pelo sistema.")
            return

        if not world.check() and option != "2":
            print()
            print(" O mapa fornecido é inválido.")
            return

        if option == "2":
            renderMap()
        elif option == "4":
            checkMap()
        elif option == "5":
            renderRobot()
        elif option == "6":
            renderCheese()
        elif option == "7":
            renderPath()
        elif option == "8":
            renderStats()


world: Map = None


def importMap():
    global world

    print()
    print(" Qual o nome do arquivo?")
    print()

    path = input('  >> ')

    try:
        with open(path, 'r') as text_buffer:
            text_content = text_buffer.read()

        world = Map()
        world.load(text_content.split("\n"))

        print()
        print(" O novo mapa foi carregado com sucesso.")
    except FileNotFoundError:
        print()
        print(" O arquivo informado é inválido.")


def generateMap():
    global world

    world = Map()
    world.load(generate())

    print()
    print(" O mapa foi gerado com êxito.")


def checkMap():
    print()
    print(" O mapa carregado " + ("é viável." if world.check() else "não é viável."))


def renderMap():
    view.renderRaw(world.grid)


def renderRobot():
    print()
    print(', '.join(map(str, world.find(world.robot[0], Type.QUEIJO, []))))


def renderCheese():
    print()
    print(', '.join(map(str, world.find(world.cheese[0], Type.ROBO, []))))


def renderPath():
    view.renderPath(world)


def renderStats():
    going = world.find(world.robot[0], Type.QUEIJO, [])
    back = world.find(world.cheese[0], Type.ROBO, [])

    print()
    print(f" . Posição do robô: {world.robot[0]}")
    print(f" . Posição do queijo: {world.cheese[0]}")
    print(f" . Tamanho do mapa: {len(world.grid)}x{len(world.grid[0])}")
    print(f" . Passos para objetivo: {len(going)}")
    print(f" . Passos para retorno: {len(back)}")
    print(f" . Passos totais: {len(going) + len(back)}")
    print()


while True:
    menu()
