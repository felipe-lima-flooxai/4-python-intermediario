#varios list comprehensions diferentes
#ordem: basico, condicional, if-else, aninhado, string, many loops, achatar, func, dict, unicos
quadrados = [x ** 2 for x in range(10)]
print(quadrados)

pares = [x for x in range(21) if x % 2 == 0]
print(pares) 

classificacao = ["Par" if x % 2 == 0 else "Ímpar" for x in range(5)]
print(classificacao) 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = [[linha[i] for linha in matriz] for i in range(3)]
print(transposta)

palavras = ["python", "algoritmo", "dados", "analise", "programação"]
filtradas = [p.upper() for p in palavras if p.startswith('a')]
print(filtradas) 

cores = ["vermelho", "verde"]
tamanhos = ["P", "M", "G"]
combinacoes = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
print(combinacoes)  

lista_aninhada = [[1, 2], [3, 4], [5, 6]]
achatada = [num for sublista in lista_aninhada for num in sublista]
print(achatada)  

def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4]
dobrados = [dobrar(x) for x in numeros]
print(dobrados)  

dados = {"a": 10, "b": -5, "c": 3, "d": -2}
chaves_positivas = [chave for chave, valor in dados.items() if valor > 0]
print(chaves_positivas)

lista_repetida = [1, 2, 2, 3, 4, 4, 5]
unicos = [x for i, x in enumerate(lista_repetida) if x not in lista_repetida[:i]]
print(unicos)  