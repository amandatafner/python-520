# Imprime os numeros de 10 ate 98
for i in range(10, 99):
    print(i)

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

#Imprime os numeros de 1 ate 9
for i in lista:
    print(i)  

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]    

soma = 0
contador = 0

for numero in lista:
    soma = soma + numero
    contador = contador + 1

media = soma / contador 

print(media)