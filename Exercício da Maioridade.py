#Crie um programa que leia o ano de nascimento algumas pessoas.
#No final, mostre quantas ainda não atingiram a maioridade e quantas já atingiram.
cont = 0
cont2 = 0
import datetime #eu poderia importar de outra forma -> from datetime import date
ano = datetime.date.today().year
for c in range(1,8):
    while True:
        try:
            nasci = int(input(f"Pessoa {c} -> Qual é o ano do seu nascimento?"))
            break
        except ValueError:
            print("ERRO.Digite o ano do seu nascimento!Apenas Números.\nNão use letras.")
    idade = ano - nasci
    if idade >= 18:
        cont+= 1
    else:
        cont2+= 1
print(f"Das 7 pessoas, {cont} já atingiram a maioridade e {cont2} ainda não atingiram a maioridade.")
