# Desenvolva um gerador de senhas que crie senhas seguras baseadas em critérios
# específicos, com validação de força e opções de personalização avançadas.
# Requisitos técnicos:
#  Use range para controlar comprimento e iterações
#  Implemente try-except para validação de entrada
#  Use if-elif-else para diferentes níveis de segurança
#  Crie função para validação de força da senha
#  Use while para regeneração até atingir critérios
import random
import string

nivel_permitido=["basico", "medio","forte"]
def nivel_senha (informacoes_senha:str):
    Letras_Maiuscula= string.ascii_uppercase
    Letras_Minusculas= string.ascii_lowercase
    Numeros ="1234567890"
    Caracteres_Escpecial= "!@#$%^&*"
    nivel = informacoes_senha.lower()
    senha = ""
    comprimento = 0
    conjunto_caracteres = ""

    if nivel  == "basico":
       conjunto_caracteres = Letras_Minusculas + Letras_Maiuscula
       comprimento = 3
           
    elif  nivel  == "medio": 
       conjunto_caracteres= Letras_Minusculas + Numeros + Letras_Maiuscula
       comprimento = 6

    elif nivel == "forte":
        conjunto_caracteres= Letras_Minusculas + Numeros +  Letras_Maiuscula + Caracteres_Escpecial
        comprimento = 10
    else:
        pass
    for i in range(comprimento):
       caractere_escolhido = random.choice(conjunto_caracteres)
       senha += caractere_escolhido
    return senha
    
while True:
    try:
     informacoes_senha= input('Qual é o nível de seguranca da senha? (EX: basico, médio ou forte)').strip()
     if not informacoes_senha:
        raise ValueError(f"Você deve digitar uma das seguintes palavras:{','.join(nivel_permitido)}. (EX: basico, médio ou forte) ")
     
     if not informacoes_senha.isalpha():
        raise ValueError("A entrada não deve conter números ou símbolos. Digite apenas as palavras 'basico', 'medio' ou 'forte'.")
     
     if informacoes_senha.lower() not in nivel_permitido:
        raise ValueError(f"Opção inválida. Escolha entre: {', '.join(nivel_permitido)}.")
     break
    except ValueError as e:
       print(f"Entrada Invalida: {e}")  
nivel_escolhido = informacoes_senha.lower()
print("nivel de seguranca escolhido foi: ", informacoes_senha)
senha_final = nivel_senha(nivel_escolhido)
print(f"A senha  é: {senha_final}")
