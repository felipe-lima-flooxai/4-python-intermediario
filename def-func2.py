def listar_itens(*itens):
    """Recebe um número variável de argumentos"""
    print("Itens recebidos:")
    for item in itens:
        print(f"- {item}")


lista = input().split()
listar_itens(lista)

#IMPORTANTE!
def exemplo(a, b, *args):
    print(f"a: {a}, b: {b}, args: {args}")

exemplo(1, 2, 3, 4, 5)  # a: 1, b: 2, args: (3, 4, 5)