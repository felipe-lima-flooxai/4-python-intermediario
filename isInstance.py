lista_mista = [10, "Python", 3.14, [1, 2, 3], 42, "Steam", 9.8, {"chave": "valor"}]

contagem_tipos = {}
for elemento in lista_mista:
    tipo = type(elemento).__name__  
    contagem_tipos[tipo] = contagem_tipos.get(tipo, 0) + 1

print("Contagem de tipos:")
for tipo, quantidade in contagem_tipos.items():
    print(f"{tipo}: {quantidade}")

numeros = [x for x in lista_mista if isinstance(x, (int, float))]

print("\nNúmeros na lista:", numeros)