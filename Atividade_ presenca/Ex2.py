#Desenvolva um sistema de autenticação que permita ao usuário fazer login com 
#tentativas limitadas. O sistema deve ter diferentes níveis de usuário e implementar 
#bloqueio temporário após falhas consecutivas. 
import time
from getpass import getpass
funcionarios = [
    ["maria", "senha123"],
    ["joao", "senha456"]
]

usuarios = [
    ["Enzo", "senha012"],
    ["Noah", "senha789"]
]

def validar_credenciais(nome, senha):
    if [nome, senha] in funcionarios:
        return "funcionario"
    elif [nome, senha] in usuarios:
        return "usuario"
    else:
        return None
Limite_Tentativas=5
i=0
def bloqueio ():
  
  print(" Tentativas excedidas. Tente novamente mais tarde.")
  bloqueio=30
  for i in range (bloqueio, 0,-1):
   print(f"Tempo restante: {i} segundos...")
   time.sleep(1)
  print("Bloqueio finalizado!") 

while i<Limite_Tentativas:
  i+=1
  try:
    nome_usuario= input('Informe seu nome de Usuário:').strip()
    senha_usuario= getpass('Por favor, informe sua senha: ').strip()
    
    if not nome_usuario or not senha_usuario:
     raise ValueError("Nome de usuário ou senha não podem estar vazios.")
   
    nivel = validar_credenciais(nome_usuario, senha_usuario)
    if nivel:
      print(f"Seja bem vindo {nivel}(a): {nome_usuario} ")
      break 
    else:
      print(f'Dados invalidos tente novamente. Você tem mais ({Limite_Tentativas- i}) tentativa(s).)')
  except ValueError as e:
    print(f" Erro de Entrada: {e}. Você tem mais ({Limite_Tentativas- i}) tentativa(s).")
if i >=Limite_Tentativas:
  bloqueio()

