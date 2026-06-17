# ================================================
# LIMPEZA E TRATAMENTO DE DADOS
# Simulando dados "sujos" de laboratório
# ================================================
import numpy as np
import pandas as pd

# ========================
# 1. CRIANDO DADOS "SUJOS" DE PROPÓSITO
# ========================
np.random.seed(42)

dados_sujos = {
    "Experimento": ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"],
    "pH": [6.5, 6.8, np.nan, 7.0, 65.0, 6.2, 6.9, 6.5, 7.1, 6.3],  # nan e erro de digitação (65.0)
    "Temperatura": [35.0, 36.0, 34.5, np.nan, 33.0, 37.0, 35.5, -10.0, 36.5, 34.0],  # nan e valor impossível
    "Tempo": [24, 24, 48, 24, 12, 24, 36, 24, np.nan, 24],
    "Consumo": [85.5, 90.2, 78.3, 95.1, np.nan, 82.0, 88.7, 91.0, 86.5, 89.0]
}

df = pd.DataFrame(dados_sujos)

print("--- Dados originais (sujos) ---")
print(df)

# ========================
# 2. IDENTIFICANDO PROBLEMAS
# ========================
print("\n--- Valores faltantes por coluna ---")
print(df.isnull().sum())

print("\n--- Estatísticas (revela valores suspeitos) ---")
print(df.describe())

# ========================
# 3. CORRIGINDO VALORES IMPOSSÍVEIS
# ========================
print("\n--- Corrigindo valores fora da faixa biológica possível ---")

# pH só pode estar entre 0 e 14 (na prática, fermentação entre 4 e 9)
df.loc[df["pH"] > 14, "pH"] = np.nan
print("pH corrigido (valor 65.0 virou NaN)")

# Temperatura não pode ser negativa nesse contexto
df.loc[df["Temperatura"] < 0, "Temperatura"] = np.nan
print("Temperatura corrigida (-10.0 virou NaN)")

print("\n--- Dados após correção de valores impossíveis ---")
print(df)

# ========================
# 4. TRATANDO VALORES FALTANTES (NaN)
# ========================
print("\n--- Estratégias para lidar com NaN ---")

# Opção A: Remover linhas com qualquer NaN
df_remover = df.dropna()
print(f"\nOpção A - Remover linhas com NaN: {len(df_remover)} linhas restantes (de {len(df)})")
print(df_remover)

# Opção B: Preencher com a média da coluna
df_preencher = df.fillna(df.mean(numeric_only=True))
print("\nOpção B - Preencher com a média:")
print(df_preencher.round(2))