#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:08:37 2022


@author: mac-prof
"""

# print("Olá, Xerxes!")

# Variáveis

nome = 'Xerxes'
# print(nome)
idade = 16
# print(idade)
peso = 3.4
# print(peso)
diabetico = False
# print(diabetico)
mensagem = f'Paciente {nome}, de {idade} anos tem {peso} quilos.'
# print(mensagem)

# Operações

# print(nome + nome)
# print(idade + idade)
# print(peso + peso)
# print(diabetico + diabetico)

# Listas e Dicionários

interesses = ['Python','Desenhar','Metal']
# print(interesses)
interesses[0] = 'Programar'
# print(interesses)
interesses[2] = 'Ouvir música'
# print(interesses)

# print(interesses[1:3])

interesses_novos = {'Computador':'Programar',
                    'Caderno': 'Desenhar',
                    'Casa': 'Ouvir música'}
# print(interesses_novos['Computador'])
# print(interesses_novos['Caderno'])
# print(interesses_novos['Casa'])

# Controle de fluxo
# for ou "para cada"

# print(f'Eu tenho interesse em {interesses[0]}')
# print(f'Eu tenho interesse em {interesses[1]}')
# print(f'Eu tenho interesse em {interesses[2]}')

# for interesse in interesses:
#     print(f'Eu tenho interesse em {interesse}')
#     if interesse == 'Programar':
#         print('Minha linguagem de programação favorita é Python')
#     elif interesse == 'Ouvir música':
#         print('E meu gênero favorito é Metal.')
#     else:
#         print('E eu gosto de fazer isso.')
# print('E esses são meus interesses')

# while ou enquanto

# continuar = 'Sim'
# while continuar == 'Sim':
#     continuar = input('Quer continuar? ')

n = 10
while n > 1:
    # print(n)
    n = n - 1

# Funções

def somar(a,b):
    soma = a + b
    return soma

resultado = somar(23,36)
print(resultado)
























