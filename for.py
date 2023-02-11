#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 10:13:20 2023

@author: laa
"""
#loop for em python

#criando uma lista 

carros = ["Fusca","Kyumaru","Uno"]
print(carros[0])

#imprimindo usando o loop for

for x in carros:
    print(x)
# o for do python se parece com um forEach
    
#Utilizando for com if

for x in carros:
    print(x)
    if(x =="Kyumaru"):
        print(" Toyota")
        break
print("\n\n\n\nFim do programa")    