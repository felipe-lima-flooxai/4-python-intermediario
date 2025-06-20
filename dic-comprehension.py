numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6]
quadrados_unicos = {x ** 2 for x in numeros}
print(quadrados_unicos)

palavras = ["python", "java", "python", "c", "java"]
iniciais = {p[0].upper() for p in palavras}
print(iniciais)

valores = [10, 10.5, "texto", 20, 20.0, "outro"]
numeros = {x for x in valores if isinstance(x, (int, float))}
print(numeros)

frase = "abracadabra"
letras_unicas = {letra for letra in frase if letra not in "aeiou"}
print(letras_unicas)