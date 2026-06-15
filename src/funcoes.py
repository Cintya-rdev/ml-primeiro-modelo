# ========================
# FUNÇÕES
# ========================

# Função simples — sem retorno
def saudar(nome):
    print(f"Olá, {nome}! Bem-vinda ao Python!")

saudar("Cintya")
saudar("Turma")

# Função com retorno
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

# Usando a função
notas_calculo = [7.5, 8.0, 9.5, 6.0]
notas_fisica = [8.0, 7.0, 9.0, 8.5]

media_calculo = calcular_media(notas_calculo)
media_fisica = calcular_media(notas_fisica)

print(f"\nMédia de Cálculo: {media_calculo:.2f}")
print(f"Média de Física: {media_fisica:.2f}")

# Função com múltiplos retornos
def analisar_notas(notas):
    media = calcular_media(notas)
    maior = max(notas)
    menor = min(notas)
    return media, maior, menor

# Usando a função
media, maior, menor = analisar_notas(notas_calculo)
print(f"\n--- Análise de Cálculo ---")
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")