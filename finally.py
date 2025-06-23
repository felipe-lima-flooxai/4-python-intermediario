def abrir_arquivo(nome):
    try:
        arquivo = open(nome, "r")
        conteudo = arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    else:
        print("Arquivo lido com sucesso:")
        print(conteudo)
    finally:
        print("Encerrando operação de leitura.\n")

abrir_arquivo("exemplo.txt")
abrir_arquivo("inexistente.txt")