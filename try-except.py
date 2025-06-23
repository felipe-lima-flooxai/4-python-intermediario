def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero!"
    except TypeError:
        return "Erro: tipos incompatíveis!"
    else:
        return f"Resultado: {resultado}"
    finally:
        print("Operação finalizada.")

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))