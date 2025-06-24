from functools import partial

valores = [1, 2, 3]

resultado = map(lambda x: x * 2, valores)
print(list(resultado))  

valores = [1, 2, 3, 4]

resultado = filter(lambda x: x % 2 == 0, valores)
print(list(resultado))  

#muito maneiro isso aqui viu. 
def potencia(base, expoente):
    return base ** expoente

quadrado = partial(potencia, expoente=2)
print(quadrado(5))  

cubo = partial(potencia, expoente=3)
print(cubo(2)) 