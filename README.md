# Nomeador automático (Python)

Este é um script de automação em lote desenvolvido em Python para otimizar a organização de arquivos locais. O objetivo principal do projeto é eliminar o trabalho repetitivo de renomear arquivos individualmente, aplicando uma nomenclatura sequencial padronizada de forma instantânea.

## Como o projeto funciona

O script é totalmente autossuficiente e inteligente:
1. **Criação de Diretórios:** Ao ser executado, ele verifica e cria automaticamente as pastas `nomes aleatorios` (onde ficam os arquivos originais) e `nomes renomeados` (onde os novos arquivos serão salvos).
2. **Entrada Única:** O programa solicita ao usuário um "nome base" apenas uma vez no início do fluxo.
3. **Automação Sequencial:** Ele percorre todos os arquivos da pasta original, extrai a extensão de cada um (como `.jpg`, `.png`, `.pdf`) e gera um novo arquivo numerado sequencialmente (ex: `Projeto_1.jpg`, `Projeto_2.jpg`), garantindo que o formato do arquivo nunca seja quebrado.

## Tecnologias e Conceitos Aplicados

Para construir a lógica desse projeto do zero, utilizei bibliotecas nativas do Python (`os` e `shutil`), aplicando os seguintes conceitos:
* **Manipulação de Caminhos Dinâmicos:** Uso de `os.path.join` para garantir que o script funcione em qualquer sistema operacional (Windows, Mac ou Linux).
* **Tratamento de Diretórios:** Uso de `os.makedirs(..., exist_ok=True)` para evitar erros caso as pastas já existam ou ainda não tenham sido criadas.
* **Isolamento de Extensões:** Manipulação e preservação do formato do arquivo através da função `os.path.splitext`.
* **Otimização de Laços de Repetição:** Estruturação de um loop `for` limpo e eficiente com um contador numérico, eliminando desvios condicionais desnecessários.
