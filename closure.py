def saudacao_generator(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

bom_dia = saudacao_generator("Bom dia")
print(bom_dia("Felipe"))

#é uma closure porque além de ser high-order, também salva o estado de variáveis do escopo xterno
#no caso guarda o valor de saudação

