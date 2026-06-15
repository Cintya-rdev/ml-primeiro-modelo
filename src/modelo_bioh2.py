# ================================================
# MODELO DE ML — PREVISÃO DE CONSUMO DE SUBSTRATO
# Fermentação Escura para Produção de Biohidrogênio
# ================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ========================
# 1. SIMULANDO OS DADOS
# ========================
np.random.seed(42)  # garante que os dados simulados são sempre iguais
n = 100             # 100 experimentos simulados

pH = np.random.uniform(5.0, 7.5, n)
temperatura = np.random.uniform(25, 40, n)
tempo = np.random.uniform(6, 48, n)
conc_inicial = np.random.uniform(5, 30, n)

# Consumo de substrato — fórmula simulada com base em lógica biológica
consumo = (
    2.5 * conc_inicial +
    1.2 * tempo +
    0.8 * temperatura -
    3.0 * np.abs(pH - 6.5) +  # pH ótimo próximo de 6.5
    np.random.normal(0, 2, n)  # ruído experimental
)

# Montando o DataFrame
df = pd.DataFrame({
    "pH": pH.round(2),
    "Temperatura": temperatura.round(1),
    "Tempo": tempo.round(1),
    "Conc_Inicial": conc_inicial.round(2),
    "Consumo": consumo.round(2)
})

print("--- Primeiras linhas dos dados ---")
print(df.head())
print("\n--- Resumo estatístico ---")
print(df.describe().round(2))

# ========================
# 2. PREPARANDO OS DADOS
# ========================
X = df[["pH", "Temperatura", "Tempo", "Conc_Inicial"]]
y = df["Consumo"]

# Dividindo em treino (80%) e teste (20%)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDados de treino: {len(X_treino)} experimentos")
print(f"Dados de teste: {len(X_teste)} experimentos")

# ========================
# 3. TREINANDO O MODELO
# ========================
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
print("\nModelo treinado com sucesso! ✓")

# ========================
# 4. AVALIANDO O MODELO
# ========================
y_previsto = modelo.predict(X_teste)

mse = mean_squared_error(y_teste, y_previsto)
r2 = r2_score(y_teste, y_previsto)

print(f"\n--- Métricas de Avaliação ---")
print(f"R² (acurácia): {r2:.4f}")
print(f"Erro médio quadrático: {mse:.4f}")

# ========================
# EQUAÇÃO DO MODELO
# ========================
b0 = modelo.intercept_
b1, b2, b3, b4 = modelo.coef_

print("\n--- Equação da Regressão Linear ---")
print(f"Consumo = {b0:.4f}")
print(f"        + {b1:.4f} × pH")
print(f"        + {b2:.4f} × Temperatura")
print(f"        + {b3:.4f} × Tempo")
print(f"        + {b4:.4f} × Conc_Inicial")

# ========================
# 5. VISUALIZANDO OS RESULTADOS
# ========================
b0 = modelo.intercept_
b1, b2, b3, b4 = modelo.coef_

equacao = (f"Consumo = {b0:.2f} + {b1:.2f}·pH + {b2:.2f}·Temp\n"
           f"        + {b3:.2f}·Tempo + {b4:.2f}·Conc_Ini")

plt.figure(figsize=(8, 5))
plt.scatter(y_teste, y_previsto, color="steelblue", alpha=0.7, label="Previsões")
plt.plot([y_teste.min(), y_teste.max()],
         [y_teste.min(), y_teste.max()],
         color="red", linestyle="--", label="Previsão perfeita")

# R² no canto superior esquerdo
plt.text(0.05, 0.95, f"R² = {r2:.4f}",
         transform=plt.gca().transAxes,
         fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Equação no canto inferior direito
plt.text(0.55, 0.08, equacao,
         transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

plt.xlabel("Consumo Real (g/L)")
plt.ylabel("Consumo Previsto (g/L)")
plt.title("Real vs Previsto — Consumo de Substrato")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/modelo_bioh2.png")
plt.show()
print("\nGráfico salvo em outputs/modelo_bioh2.png")

# ========================
# 6. FAZENDO UMA PREVISÃO
# ========================
print("\n--- Simulando um novo experimento ---")
novo_experimento = pd.DataFrame({
    "pH": [6.5],
    "Temperatura": [35.0],
    "Tempo": [24.0],
    "Conc_Inicial": [20.0]
})

previsao = modelo.predict(novo_experimento)
print(f"pH: 6.5 | Temperatura: 35°C | Tempo: 24h | Conc. Inicial: 20 g/L")
print(f"Consumo previsto: {previsao[0]:.2f} g/L")