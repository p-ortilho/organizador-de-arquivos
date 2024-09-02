from colorama import Fore
import os
import shutil

class Organize:
    __extensoes = {
        '.jpg': 'Imagens',
        '.png': 'Imagens',
        '.gif': 'Imagens',
        '.mp4': 'Videos',
        '.doc': 'Documentos',
        '.pdf': 'Documentos',
        '.txt': 'Documentos',
        '.zip': 'Zips'
    }

    def __init__(self, diretorio:str) -> None:
        self.__diretorio = diretorio

    def organizar(self):
        # Caminho do meu diretorio
        # os.path.expanduser('~') -> retorna C:\\Users\\nome'
        self.__diretorio = os.path.join(os.path.expanduser('~'), self.__diretorio)
        for arquivos in os.listdir(self.__diretorio):
            # Cria o caminho dos arquivos
            arquivos_diretorio = os.path.join(self.__diretorio, arquivos)
            # Corta cada extensao dos arquivos
            extensao = os.path.splitext(arquivos)[1].lower()

            if extensao in self.__extensoes:
                # Cria o caminho das pastas dicionario
                diretorio_arquivos_caminho = os.path.join(self.__diretorio, self.__extensoes[extensao])
                if os.path.isdir(diretorio_arquivos_caminho):
                    # Move os arquivos
                    shutil.move(arquivos_diretorio, diretorio_arquivos_caminho)
                    print(Fore.GREEN, f'Arquivos movidos com sucesso! {arquivos}', Fore.RESET)
                else:
                    # Cria pasta não existente
                    os.mkdir(os.path.join(self.__diretorio, self.__extensoes[extensao]))
                    print(Fore.BLUE, f'Pasta criada com sucesso! {self.__extensoes[extensao]}', Fore.RESET)