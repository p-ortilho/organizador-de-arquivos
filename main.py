from colorama import Fore
import os 
import shutil

# caminho do meu diretorio downlods
# os.path.expanduser('~') -> retorna C:\\Users\\nome'
dir = os.path.join(os.path.expanduser('~'), 'Downloads')

extensoes = {
    '.jpg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.mp4': 'Videos',
    '.doc': 'Documentos',
    '.pdf': 'Documentos',
    '.txt': 'Documentos',
    '.zip': 'Zips'
}

# percorre os arquivos dentro de dir
for arquivos in os.listdir(dir):
    # print(arquivos)
    # cria o caminho dos arquivos
    arquivos_dir = os.path.join(dir, arquivos)
    # corta cada extensao dos arquivos
    extensao = os.path.splitext(arquivos)[1].lower()
    # print(extensao)
    if extensao in extensoes:
        pasta_dicionario = extensoes[extensao]
        # print(pasta_dicionario)
        # cria o caminho das pastas dicionario
        pastas_arquivo_caminho = os.path.join(dir, pasta_dicionario)
        # print(pastas_arquivo_caminho)
        # se a pasta existir
        if os.path.isdir(pastas_arquivo_caminho):
            # movendo os arquivos
            shutil.move(arquivos_dir, pastas_arquivo_caminho)
            print(Fore.GREEN, f'Arquivos movidos com sucesso! {arquivos}', Fore.RESET)
        else:
            # cria pasta não existente
            os.mkdir(os.path.join(dir, extensoes[extensao]))
            print(Fore.BLUE, f'Pasta criada com sucesso! {extensoes[extensao]}', Fore.RESET)