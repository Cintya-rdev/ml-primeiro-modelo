# ========================
# LISTAS E LOOPS
# ========================

# Criando listas
notas = [7.5, 8.0, 9.5, 6.0, 8.5]
disciplinas = ["Cálculo", "Física", "EngEcon", "FenTrans", "Python"]

# Acessando elementos (começa do índice 0!)
print("Primeira nota:", notas[0])
print("Última nota:", notas[-1])
print("Segunda disciplina:", disciplinas[1])

# Tamanho da lista
print("\nQuantidade de disciplinas:", len(disciplinas))

# Adicionando e removendo
notas.append(9.0)  # adiciona no final
print("\nNotas após adicionar:", notas)

notas.remove(6.0)  # remove o valor 6.0
print("Notas após remover 6.0:", notas)

# ========================
# LOOPS
# ========================

# Loop básico — percorre a lista
print("\n--- Minhas disciplinas ---")
for disciplina in disciplinas:
    print(disciplina)

# Loop com índice
print("\n--- Notas com índice ---")
for i in range(len(notas)):
    print(f"Nota {i+1}: {notas[i]}")

# Calculando a média
soma = 0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"\nMédia das notas: {media:.2f}")
