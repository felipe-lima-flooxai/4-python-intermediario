grupo_a = {"Avengers", "Inception", "The Dark Knight", "Interstellar", "Avingers"}
grupo_b = {"Inception", "The Matrix", "Interstellar", "Jurassic Park", "The Dark Knight"}

print("Grupo A (com erro):", grupo_a)
print("Grupo B:", grupo_b)


grupo_a.remove("Avingers")  
grupo_a.add("Avengers")    

print("\nGrupo A (corrigido):", grupo_a)


comuns = grupo_a & grupo_b
print("\nFilmes comuns:", comuns)


so_a = grupo_a - grupo_b
print("\nSó Grupo A:", so_a)


todos = grupo_a | grupo_b
print("\nTodos os filmes únicos:", todos)


print("\n'The Matrix' está no Grupo B?", "The Matrix" in grupo_b)


grupo_a.add("Pulp Fiction")
print("\nGrupo A após adição:", grupo_a)


grupo_b.remove("Jurassic Park")
print("\nGrupo B após remoção:", grupo_b)