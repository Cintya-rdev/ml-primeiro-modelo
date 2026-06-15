# ========================
# NUMPY
# ========================
import numpy as np

# Array NumPy — como vetor do MATLAB!
notas = np.array([7.5, 8.0, 9.5, 6.0, 8.5])

print("--- NumPy ---")
print("Notas:", notas)
print("Média:", np.mean(notas))
print("Maior:", np.max(notas))
print("Menor:", np.min(notas))
print("Desvio padrão:", np.std(notas).round(2))

# Operações matemáticas em todas as notas de uma vez
print("\nNotas + 0.5 (bônus):", notas + 0.5)
print("Notas × 2:", notas * 2)

# ========================
# PANDAS
# ========================
import pandas as pd

# DataFrame — como uma tabela Excel!
dados = {
    "Nome": ["Ana", "Bia", "Carlos", "Diana", "Eduardo"],
    "Nota": [7.5, 8.0, 9.5, 6.0, 8.5],
    "Aprovado": [True, True, True, False, True]
}

df = pd.DataFrame(dados)

print("\n--- Pandas ---")
print(df)

print("\nResumo estatístico:")
print(df["Nota"].describe())

print("\nSó os aprovados:")
print(df[df["Aprovado"] == True])
