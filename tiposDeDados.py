#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:47:05 2022

@author: laa
"""

#inteiro
x = 1
"""
Para imprimir a informação
deve se usar uma operação de casting
para string com o str()
"""
print("O valor :" + str(x))
print("Tipo da variavel " +str(type(x)))

#tipo float
print("####################################")
      

y = 1.5

print("O valor :" + str(y))
print("Tipo da variavel " +str(type(y)))

print("####################################")

#tipo booleano

gato = True

print("O valor :" + str(gato))
print("Tipo da variavel " +str(type(gato)))

print("##################################")
#string

nome = "Leonardo"
print("O valor :" + str(nome))
print("Tipo da variavel " +str(type(nome)))

print("##################################")

#numeros complexos
n1 = 5
n2 = 2
comp = complex(n1,n2)
print("O valor :" + str(comp))
print("Tipo da variavel " +str(type(comp)))

print("###################################")
      #coleções
 #list
lista = ["Carro","Avião","Navio"]
print("Valor :" + lista[0])
lista[0] = "Sanyon"
print("Valor :" + lista[0])

#lista com quantidade de itens

listaComItens = range(0,10)#tamanho fixo
print("Valor :" + str(listaComItens[0]))
print("Tipo da variavel " +str(type(listaComItens)))
#tublas
tupla = ("Carro",1,2.5)
print(tupla[0])

#dictionary
#elemento chave valor

dicionario={
        "linguagem":"python",
        "ide":"spyder"
        
        }

#imprimindo 
print("chaves :" + dicionario["linguagem"])


     

      