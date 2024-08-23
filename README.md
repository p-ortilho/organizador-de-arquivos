# Organizador de Downloads

Este script Python organiza os arquivos dentro da pasta de Downloads do usuário, movendo-os para subpastas específicas de acordo com suas extensões de arquivo.

## Funcionalidades

- **Organização Automática**: O script verifica a pasta de Downloads do usuário e move os arquivos para subpastas correspondentes com base em suas extensões.
- **Extensões Suportadas**:
  - Imagens: `.jpg`, `.png`, `.gif`
  - Vídeos: `.mp4`
  - Documentos: `.doc`, `.pdf`, `.txt`
  - Arquivos compactados: `.zip`
- **Criação de Pastas**: Caso uma subpasta para uma determinada extensão não exista, o script cria essa pasta automaticamente.

## Requisitos

- Python 3.12
- Módulo `colorama`: Para instalar, execute `pip install colorama`

## Como Usar

1. **Clonar o repositório**:
   ```
   git clone https://github.com/p-ortilho/Organizador-de-Downloads
   ```

2. **Instalar as dependências**:
   ```
   pip install colorama
   ```

3. **Executar o script**:
   ```
   python main.py
   ```

## Funcionamento

1. O script define o caminho para a pasta de Downloads do usuário.
2. Em seguida, percorre todos os arquivos dentro dessa pasta.
3. Com base nas extensões dos arquivos, ele decide em qual subpasta cada arquivo deve ser movido.
4. Se a subpasta não existir, ela é criada.
5. Os arquivos são movidos para as subpastas apropriadas e uma mensagem é exibida no terminal, indicando o sucesso da operação.



