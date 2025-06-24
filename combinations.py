from itertools import combinations, permutations, product

itens = ['a', 'b', 'c']

print("Combinations de 2:")
for c in combinations(itens, 2):
    print(c)

print("\nPermutations de 2:")
for p in permutations(itens, 2):
    print(p)

print("\nProduct com repeat=2:")
for pr in product(itens, repeat=2):
    print(pr)