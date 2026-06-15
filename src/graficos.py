# ========================
# MATPLOTLIB — GRÁFICOS
# ========================
import matplotlib.pyplot as plt
import numpy as np

# --- Gráfico 1: Barras ---
nomes = ["Ana", "Bia", "Carlos", "Diana", "Eduardo"]
notas = [7.5, 8.0, 9.5, 6.0, 8.5]

plt.figure(figsize=(8, 4))
plt.bar(nomes, notas, color="steelblue")
plt.title("Notas dos Alunos")
plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.ylim(0, 10)
plt.axhline(y=7.0, color="red", linestyle="--", label="Mínimo aprovação")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/notas_alunos.png")
plt.show()
print("Gráfico 1 salvo!")

# --- Gráfico 2: Linha ---
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
temperaturas = [32, 31, 30, 28, 26, 25]

plt.figure(figsize=(8, 4))
plt.plot(meses, temperaturas, marker="o", color="tomato", linewidth=2)
plt.title("Temperatura Média em Cuiabá")
plt.xlabel("Mês")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/temperaturas.png")
plt.show()
print("Gráfico 2 salvo!")

# --- Gráfico 3: Histograma ---
dados = np.random.normal(loc=7.5, scale=1.0, size=200)

plt.figure(figsize=(8, 4))
plt.hist(dados, bins=20, color="mediumseagreen", edgecolor="white")
plt.title("Distribuição de Notas (200 alunos)")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig("outputs/distribuicao.png")
plt.show()
print("Gráfico 3 salvo!")