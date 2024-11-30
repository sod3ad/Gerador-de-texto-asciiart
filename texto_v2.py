import pyfiglet 
from termcolor import colored
import webbrowser

am = "\033[33m"
cy = "\033[36m"
ve = "\033[31m"
br = "\033[37m"

# Créditos: DevMiguel

def opções():
    print(f"{cy}1- VISITAR CRIADOR/REPOSITÓRIO")
    print(f"{cy}2- CONTINUAR PARA O GERADOR")
    
    opcao = input("DIGITE UM NUMERO: ")
    if opcao == '1':
        print(f"{br}REDIRECIONANDO...")
        webbrowser.open("https://github.com/DevMiiguel")
    elif opcao == '2':
        print(f"{br}VOCÊ ESCOLHEU CONTINUAR")
        
opções()


while True:
    T = input(f"{am}DIGITE O TEXTO: ")
    if T.strip():
        break
    else:
              print(f"{ve}É OBRIGATÓRIO DIGITAR ALGO !, TENTE NOVAMENTE")

F = input(f"{am}FONTE: ")

valid_fonts = ['bloody', 'standard', 'script', 'doom', 'block', 'big', 'banner', 'poison', 'alligator']
if F not in valid_fonts:
    F = 'standard'
 
ASCII_art_1 = pyfiglet.figlet_format(T, font = F)

C = input(f"{am}COR (EM INGLÊS): ")

valid_colors = ['red', 'green', 'yellow', 'blue', 'cyan', "magenta", 'white', 'grey',]
if C not in valid_colors:
    C = 'white'

colored_ascii = colored(ASCII_art_1, C)

print(colored_ascii)