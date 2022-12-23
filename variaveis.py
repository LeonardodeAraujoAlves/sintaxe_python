#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:40:15 2022

@author: laa
"""

#Trabalhando com variáveis com python

#variaveis globais
num1=num2=res=0

def cn():
    #variavel local
    global canal
    #para transformar uma varivel local em global usa se a palavra reservada global
    canal = "CFB cursos"
    print(canal)


print(canal)