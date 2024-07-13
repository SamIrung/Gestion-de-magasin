import colorama
from colorama import Fore, Back, Style
import sys
import os

def clear():
    os.system("cls")
def pause():
    gris()
    os.system("pause")

def bleu():
    colorama.init()
    print(Fore.BLUE)
def vert():
    colorama.init()
    print(Fore.GREEN)
def jaune():
    colorama.init()
    print(Fore.YELLOW)
def blanc():
    colorama.init()
    print(Fore.WHITE)
def rouge():
    colorama.init()
    print(Fore.RED)
def gris():
    colorama.init()
    print(Fore.LIGHTBLACK_EX)
    

def position(x,y):
    colorama.init()
    sys.stdout.write(f"\033[{x};{y}H")


def reiniialser():
    colorama.init()

    print(Style.RESET_ALL)
