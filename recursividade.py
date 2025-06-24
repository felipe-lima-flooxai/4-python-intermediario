def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def somar_lista(lista):
    if not lista:
        return 0
    return lista[0] + somar_lista(lista[1:])

print(fatorial(5))

print(fibonacci(6))

print(somar_lista([1, 2, 3, 4]))