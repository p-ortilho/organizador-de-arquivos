# :snake: Organizador de Arquivos

![Files Image](10838253_4560004.jpg "File Organize")

O objetivo deste script é atuar como um organizador de arquivos para as principais pastas do Windows. Ele automatiza o processo de separar e organizar os arquivos, criando subpastas para tornar tudo mais organizado. 

## :open_file_folder: Funcionalidades

- **Organização Automática**: O script verifica a pasta que o usuario passa como argumento durante a execução do script, movendo os arquivos para subpastas correspondentes com base em suas extensões. Para sua execução é necessário ter o `python` instalado. 

- **Extensões Suportadas**:
  - Imagens: `.jpg`, `.png`, `.gif`
  - Vídeos: `.mp4`
  - Documentos: `.doc`, `.pdf`, `.txt`
  - Arquivos compactados: `.zip`
- **Criação de Pastas**: Caso uma subpasta para uma determinada extensão não exista, o script cria essa pasta automaticamente.

## :heavy_exclamation_mark: Como Usar

1. **Clonar o repositório**:
   ```
   git clone https://github.com/p-ortilho/organizador-de-arquivos.git
   ```

2. **Instalar as dependências**:
   ```
   pip install -r requirements.txt
   ```

3. **Execute o --help para entender como o script funciona**:
   ```
   python main.py --help
   ```
4. **Exemplo de execução**:
   ```
   python main.py downloads
   ```
   Nesse exemplo a pasta que vai ser organizada será a Downloads.
5. **Exemplo de execução com subpastas**:
   ```
   python main.py downloads\\subpasta
   ```
   Você também pode organizar subpastas presentes dentro das pastas principais, pasta adicionar o caminho da basta conforme o exemplo. 

Um ponto importante é que caso você deseja, pode organizar qualquer pasta dentro do seguinte dominio de diretorio: `C:\Users\seu_usuario`.

**Exemplo de execução**
   ```
   python main.py pasta_teste
   ```
O caminho dessa pasta seria da seguinte maneira `C:\Users\seu_usuario\pasta_teste`




## :wrench: Execução

1. O script define o caminho para a pasta de Downloads do usuário.
2. Em seguida, percorre todos os arquivos dentro dessa pasta.
3. Com base nas extensões dos arquivos, ele decide em qual subpasta cada arquivo deve ser movido.
4. Se a subpasta não existir, ela é criada.
5. Os arquivos são movidos para as subpastas apropriadas e uma mensagem é exibida no terminal, indicando o sucesso da operação.



