# Desenvolva uma calculadora que calcule impostos progressivos baseados em
# diferentes faixas de renda, com simulações de cenários e comparações anuais.
# Requisitos técnicos:
# . Use range para iterar pelas faixas de imposto
# . Implemente try-except para validação de valores monetários
# . Use if-elif-else para aplicar diferentes alíquotas
# . Crie função para cálculos de cada faixa
# . Use while para simulações múltiplas 

def Calcular_imposto(renda):
    faixas = [10000, 30000, 70000, float('inf')]
    aliquotas = [0.05, 0.10, 0.15, 0.20]
    for i in range(len(faixas)):
        if renda <= faixas[i]:
            return renda * aliquotas[i]
    return 0 

while True:
    try:
        renda = input("Informe sua renda anual (ou 'sair' para terminar): ")
        if renda.lower() == 'sair':
            break
        renda = float(renda)
        imposto = Calcular_imposto(renda)
        print(f"Imposto devido: R$ {imposto:.2f}")
    except ValueError:
        print("Valor inválido, tente novamente.")
