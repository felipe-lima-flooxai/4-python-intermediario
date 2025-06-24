with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Linha 1\n")
    f.write("Linha 2\n")

with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print("Conteúdo atual:")
    print(conteudo)

with open("arquivo.txt", "a", encoding="utf-8") as f:
    f.write("Linha 3\n")

with open("arquivo.txt", "r", encoding="utf-8") as f:
    print("Conteúdo após adição:")
    print(f.read())