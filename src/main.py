from os import system
from time import sleep

from colorama import Fore, Style

import view
from map import Map
from test import generate
from type import Type


def menu():
    print()
    print(f"   {Fore.CYAN}CALCULADORA DE PERCURSO")
    print(f"      {Fore.CYAN}by @srwesleyramos")
    print()
    print(f"  {Fore.YELLOW}1. {Fore.WHITE}Importar mapa")
    print(f"  {Fore.YELLOW}2. {Fore.WHITE}Apresentar mapa atual")
    print(f"  {Fore.YELLOW}3. {Fore.WHITE}Gerar mapa aleatório")
    print(f"  {Fore.YELLOW}4. {Fore.WHITE}Verificar viabilidade")
    print(f"  {Fore.YELLOW}5. {Fore.WHITE}Caminho ao objetivo")
    print(f"  {Fore.YELLOW}6. {Fore.WHITE}Caminho de retorno")
    print(f"  {Fore.YELLOW}7. {Fore.WHITE}Apresentar percurso")
    print(f"  {Fore.YELLOW}8. {Fore.WHITE}Apresentar dados{Style.RESET_ALL}")
    print()

    option = input(f"  {Fore.YELLOW}>>{Style.RESET_ALL} ")

    if option == "1":
        import_map()
    elif option == "3":
        generate_map()
    else:
        if world is None:
            print()
            print(f" {Fore.RED}O mapa ainda não foi carregado pelo sistema.{Style.RESET_ALL}")
            return

        if not world.check() and option != "2":
            print()
            print(f" {Fore.RED}O mapa fornecido é inválido.{Style.RESET_ALL}")
            return

        if option == "2":
            render_map()
        elif option == "4":
            check_map()
        elif option == "5":
            render_robot()
        elif option == "6":
            render_cheese()
        elif option == "7":
            render_path()
        elif option == "8":
            render_stats()


world: Map = None


def import_map():
    global world

    print()
    print(f" Qual o nome do arquivo?")
    print()

    path = input(f"  {Fore.YELLOW}>>{Style.RESET_ALL} ")

    try:
        with open(path, 'r') as text_buffer:
            text_content = text_buffer.read()

        world = Map()
        world.load(text_content.split("\n"))

        print()
        print(f" {Fore.GREEN}O novo mapa foi carregado com sucesso.{Style.RESET_ALL}")
    except FileNotFoundError:
        print()
        print(f" {Fore.RED}O arquivo informado é inválido.{Style.RESET_ALL}")


def generate_map():
    global world

    world = Map()
    world.load(generate())

    print()
    print(f" {Fore.GREEN}O mapa foi gerado com êxito.{Style.RESET_ALL}")


def check_map():
    print()
    print(" O mapa carregado " + (
        f"{Fore.GREEN}é viável" if world.check() else f"{Fore.GREEN}não é viável") + f"{Style.RESET_ALL}.")


def render_map():
    view.render_raw(world.grid)


def render_robot():
    print()
    print(', '.join(map(str, world.find(world.robot[0], Type.QUEIJO, []))))


def render_cheese():
    print()
    print(', '.join(map(str, world.find(world.cheese[0], Type.ROBO, []))))


def render_path():
    view.render_path(world)


def render_stats():
    going = world.find(world.robot[0], Type.QUEIJO, [])
    back = world.find(world.cheese[0], Type.ROBO, [])

    print()
    print(f" {Fore.YELLOW}. {Fore.WHITE}Posição do robô: {world.robot[0]}")
    print(f" {Fore.YELLOW}. {Fore.WHITE}Posição do queijo: {world.cheese[0]}")
    print(f" {Fore.YELLOW}. {Fore.WHITE}Tamanho do mapa: {len(world.grid)}x{len(world.grid[0])}")
    print(f" {Fore.YELLOW}. {Fore.WHITE}Passos para objetivo: {len(going)}")
    print(f" {Fore.YELLOW}. {Fore.WHITE}Passos para retorno: {len(back)}")
    print(f" {Fore.YELLOW}. {Fore.WHITE}Passos totais: {len(going) + len(back)}{Style.RESET_ALL}")
    print()


while True:
    system('cls')
    menu()
    sleep(8)
