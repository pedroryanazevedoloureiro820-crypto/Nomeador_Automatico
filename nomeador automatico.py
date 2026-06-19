import os
import shutil

pasta_nomeador = os.getcwd()  # Obtém o diretório atual do projeto

pasta_nomes_aleatorios = os.path.join(pasta_nomeador,"nomes aleatorios") # Define o caminho para a pasta de nomes aleatórios
os.makedirs(pasta_nomes_aleatorios, exist_ok=True)

pasta_renomeada = os.path.join(pasta_nomeador,"nomes renomeados") # Define o caminho para a pasta onde os arquivos renomeados serão armazenados
os.makedirs(pasta_renomeada, exist_ok=True)

nomes_aleatorios = os.listdir(pasta_nomes_aleatorios) # Lista todos os arquivos na pasta de nomes aleatórios

contador = 1 # Inicializa um contador para numerar os arquivos renomeados

novo_nome = input(f'Digite o novo nome para o arquivo: ') # Solicita ao usuário o novo nome para o arquivo

for nome in nomes_aleatorios:
    
    origem = os.path.join(pasta_nomes_aleatorios, nome)
    
    destino = os.path.join(pasta_renomeada, novo_nome + "_" + str(contador) + os.path.splitext(nome)[1]) # Define o caminho de destino para o arquivo renomeado
    
    contador += 1
    shutil.copy(origem, destino) # Copia o arquivo para a pasta de destino com o novo nome
print("Arquivos nomeados com sucesso!")

