#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#usando a biblioteca os

import os


"""
Created on Sat Feb 11 10:21:13 2023

@author: laa
"""

#coletando dados através do console com a função input
"""
print("Digite o seu nome : ")
nome = input()

print(nome)
"""
#Usando o input de outra forma
"""
nome = input("Digite o seu nome :")
print(nome)

if(nome == "Leonardo"):
    print("Seja bem vindo ",nome)
else:
    print("Usuário desconhecido")
print("Fim ")

"""
#realizando somas com dados do teclado
os.system('clear')#limpeza do console
num1 =int( input("Digite o primeiro valor:"))
num2= int(input("Digite o segundo valor:"))

res = num1 + num2

print("O resultado da soma : "+str(res))   