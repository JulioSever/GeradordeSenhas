import random  #Importando a biblioteca 'Random' para gerar números aleatórios
import string  #Importando a biblioteca 'String' para gerar letras
from time import sleep   #Importando a biblioteca 'Sleep' para apresentação do titulo do programa


print('='*60)
print('      Seja bem vindo ao gerador de senhas automatico!!')
print('='*60)
sleep (3)


opcao = ""
while opcao != "N":
    tamanho = int(input("Digite o tamanho desejado da senha: "))
    usar_letras_maiusculas = True if input("Usar letras maiúsculas? (S/N): ").upper() == "S" else False
    usar_letras_minusculas = True if input("Usar letras minúsculas? (S/N): ").upper() == "S" else False
    usar_numeros = True if input("Usar números? (S/N): ").upper() == "S" else False
    usar_caracteres_especiais = True if input("Usar caracteres especiais? (S/N): ").upper() == "S" else False

    caracteres = ""
    if usar_letras_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_letras_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(senha)

    opcao = input("Deseja gerar outra senha? (S/N): ").upper()