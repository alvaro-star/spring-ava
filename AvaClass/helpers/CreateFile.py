import os

def create_file(directory, nome_classe_completo, template):
    os.makedirs(directory, exist_ok=True)
    caminho_arquivo = os.path.join(directory, f"{nome_classe_completo}.java")
    
    try:
        with open(caminho_arquivo, "w") as file:
            file.write(template)
        print(f"Arquivo '{nome_classe_completo}.java' criado com sucesso.")
    except IOError as e:
        print(f"Erro ao criar o arquivo: {e}")