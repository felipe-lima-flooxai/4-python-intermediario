def aplicar_operacao(func, x, y):
    return func(x, y)

def soma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

print(aplicar_operacao(soma, 2, 3))        
print(aplicar_operacao(multiplicar, 2, 3)) 

#aplicar_operacao é a função de alta ordem
#as outras duas não, são funções normais