from module import Organize
from colorama import Fore
import sys


if __name__ == '__main__':
    argumentos = sys.argv[1].capitalize()
    if argumentos == '--help':
        print(Fore.CYAN, 'Organizador de arquivos funciona nos principais diretórios do computador, são eles:')
        print('- Desktop\n- Documents\n- Music\n- Videos\n- Pictures', Fore.RESET)
        print(Fore.GREEN, 'Exemplo de comando: python main.py Documents', Fore.RESET)
    else:
        try:
            org = Organize(argumentos)
            org.organizar()
        except Exception as error:
            print(Fore.RED, error, Fore.RESET)