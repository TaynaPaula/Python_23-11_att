# Crie um sistema que analise dados de vendas de uma empresa, calculando
# estatísticas por período, vendedor e região. O sistema deve tratar dados inconsistentes e
# gerar relatórios detalhados. 
# Requisitos técnicos: 
#   Use for com range para iterar por períodos 
#   Implemente try-except para tratar dados inválidos 
#   Use if-elif-else para categorização de desempenho 
#   Crie função para cálculos estatísticos 
#   Use while para menu interativo 
 
def calcular_estatisticas(vendas):
    total = sum(vendas)
    media = total / len(vendas) if vendas else 0
    return total, media

vendedores = ["Ana", "Carlos", "João"]
regioes = ["Sul", "Sudeste", "Nordeste"]

while True:
    try:
        print("Menu de Estatísticas: \n1 - Analisar por período \n2 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "2":
            print("Encerrando análise.")
            break
        vendas = []
        for periodo in range(3):
            valor = input(f"Informe vendas do período {periodo+1}: ")
            try:
                vendas.append(float(valor))
            except ValueError:
                print("Valor inválido! Ignorando este período.")
                vendas.append(0)
        total, media = calcular_estatisticas(vendas)
        if media > 1000:
            print("Desempenho: Excelente")
        elif media > 500:
            print("Desempenho: Bom")
        else:
            print("Desempenho: Regular")
        print(f"Total de vendas: {total}, Média: {media}")
    except Exception as e:
        print("Erro ao processar:", e)
