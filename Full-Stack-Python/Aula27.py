"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1]) #Escrevendo a string de trás para frente
print(variavel[0:9:2]) # Pulando as letras de 2 em 2 no caso
print(len(variavel))
#len conta os caracteres, no caso 9
#Espaço conta como caractere 