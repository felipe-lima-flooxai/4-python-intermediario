def calcular_total(*args):
    return sum(args)

def exibir_info_cliente(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave.title()}: {valor}")



livro = ("Dom Quixote", "Miguel de Cervantes", 29.90)
titulo, autor, preco = livro

print(f"Título: {titulo}, Autor: {autor}, Preço: R${preco:.2f}")


total = calcular_total(10.50, 25.30, 15.00, 8.75)
print(f"Total da compra: R${total:.2f}")



exibir_info_cliente(nome="Maria", email="maria@exemplo.com", telefone="987654321")