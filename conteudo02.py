#1.21.LISTAS EM PYTHON
"""
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista_1 = [1,2,3,"Regiane",True,10.5] #Em uma lista podemos elencar diversos tipos

#Indice    0    1    2    3    4
#nIndice  -5   -4   -3   -2   -1
lista =  ["A", "B", "C", "D", "E"]

print(lista[1]) #B
print(lista_1[-1]) #10.5
print(lista_1[0:3]) #1,2,3
print(lista_1[::-1]) #inverte a lista

#1.21.1.FUNÇÕES
#Concatenação
l1= [1,2,3]
l2= [4,5,6]
l3= l1+l2
print(l3) #[1, 2, 3, 4, 5, 6]

#Extend
l1.extend(l2) #[1, 2, 3, 4, 5, 6]
l1.extend('a') #[1, 2, 3, 4, 5, 6, 'a']

#Append
l2.append('b') #[4, 5, 6, 'b']

#Insert
l2.insert(0, 'banana') #insere a palavra banana no indice 0 - ['banana', 4, 5, 6, 'b']

#Pop
l2.pop()  #Remove o ultimo elemento da lista
print (l2)

