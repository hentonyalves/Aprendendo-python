"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não 
continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos 
"""
from os import system
system('cls')
maioridade = 0 
homens = 0
mulheres = 0
while True:
    system('cls')
    print(20*'=' + ' CADASTRO DE PESSOAS ' + 20*'=')
    idade = int(input('\nIdade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    if sexo not in 'mf':
        while True:
            sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
            if sexo in 'mf':
                break
    if idade >= 18:
        maioridade += 1 
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    escolha = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if escolha not in 'sn':
        while True:
            escolha = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
            if escolha in 'sn':
                break  
    if escolha == 'n':
        break
system('cls')
print(20*'*' + ' RESULTADOS ' + 20*'*')
print(f'\n>> Quantidade de pessoas com mais de 18 anos: {maioridade}\n>> Quantidade de homens cadastrados: {homens}\n>> Quantidade de mulheres com menos de 20 anos: {mulheres}\n')

