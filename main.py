import random

print ("Gerador de Senha")

caract = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,;:}{?Çç0123456789"

num = input("Quantas senhas deseja gerar? ")
num = int(num)

tam = input("Quantos caracteres deseja ter em sua senha? ")
tam = int(tam)

print("\nAqui está sua senha: \n")
for i in range(num):
  senha = ""
  for c in range(tam):
    senha += random.choice(caract)
  print(senha)