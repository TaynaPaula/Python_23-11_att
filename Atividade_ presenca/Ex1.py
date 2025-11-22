#  Crie uma função que receba uma lista de valores (que podem ser números, strings ou 
#outros tipos) e retorne uma nova lista contendo apenas os números primos válidos. A 
#função deve tratar exceções para valores inválidos e usar estruturas condicionais para 
#validação.

def Verificar_primos(lista):
    primos = []
    Lista_Primos = [2, 3, 5, 7, 11, 13, 17]
    for item in lista:
        try:
            num = int(item)
            if num in Lista_Primos:
                primos.append(num)
        except ValueError:
            pass 
    return primos

Lista_Inicial = []
for i in range(10):
    valor = input("Digite letras e números para verificação: ")
    Lista_Inicial.append(valor)
print(f"Sua lista original: {Lista_Inicial}")
primos_encontrados = Verificar_primos(Lista_Inicial)
print(f"Primos válidos encontrados: {primos_encontrados}")
  