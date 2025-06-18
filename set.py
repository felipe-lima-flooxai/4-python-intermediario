frutas = {"maçã", "banana", "laranja"}
outras_frutas = set(["kiwi", "banana", "uva"])

print("Frutas:", frutas)
print("Outras frutas:", outras_frutas)

frutas.add("melancia")
print("Após adicionar:", frutas)

frutas.remove("banana")
print("Após remover:", frutas)

print("maçã está no conjunto?", "maçã" in frutas)
print("pera está no conjunto?", "pera" in frutas)

todas_frutas = frutas.union(outras_frutas)
print("União:", todas_frutas)

comum = frutas.intersection(outras_frutas)
print("Interseção:", comum)

so_em_frutas = frutas.difference(outras_frutas)
print("Diferença:", so_em_frutas)

simetrica = frutas.symmetric_difference(outras_frutas)
print("Diferença simétrica:", simetrica)

lista_com_repetidos = ["maçã", "maçã", "banana", "banana", "uva"]
sem_repetidos = set(lista_com_repetidos)
print("Sem repetidos:", sem_repetidos)

frutas.clear()
print("Frutas após clear():", frutas)