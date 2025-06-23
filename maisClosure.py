def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def executa(funcao, a, b):
    def interna():
        print(f"Executando {funcao.__name__} com {a} e {b}...")
        return funcao(a, b)
    return interna

adiar_soma = executa(soma, 3, 5)
adiar_multiplicacao = executa(multiplicacao, 3, 5)
print("Nada ainda")

print("Executando soma agora:")
print("Resultado:", adiar_soma())

print("\nExecutando multiplicação agora:")
print("Resultado:", adiar_multiplicacao())