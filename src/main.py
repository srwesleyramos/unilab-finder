import os
import time

from map.map import Map
from src.map import view
from src.map.type import Type

world = None

while True:
    time.sleep(1.5)
    os.system('cls')

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
        print()
        print(" Qual o nome do arquivo?")
        print()

        path = input('  >> ')

        try:
            with open(path, 'r') as text_buffer:
                text_content = text_buffer.read()

            world = Map()
            world.load(text_content)

            print()
            print(" O novo mapa foi carregado com sucesso.")
        except FileNotFoundError:
            print()
            print(" O arquivo informado é inválido.")

    elif option == "3":
        # TODO: adicionar geração de mapa aleatório
        pass

    else:
        if world is None:
            print()
            print(" O mapa ainda não foi carregado pelo sistema.")
            continue

        if option == "2":
            view.renderMap(world.grid)

        elif option == "4":
            print()
            print(" O mapa carregado " + ("é viável." if world.check() else "não é viável."))

        elif option == "5":
            print()
            print(', '.join(map(str, world.find(world.robot[0], Type.QUEIJO, []))))

        elif option == "6":
            print()
            print(', '.join(map(str, world.find(world.cheese[0], Type.ROBO, []))))

        elif option == "7":
            view.renderPath(world)

        elif option == "8":
            # TODO: adicionar apresentação dos dados
            pass
