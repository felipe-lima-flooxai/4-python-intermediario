frase = "gato gato cachorro peixe gato cachorro"
contagem = {}

for palavra in frase.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)