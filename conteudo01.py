#CURSO PYTHON 3 - DO BÁSICO AO AVANÇADO

#1.MÓDULO BÁSICO (LINGUAGEM DE PROGRAMAÇÃO)

#1.1.COMENTÁRIOS

#Insira seu comentário de uma linha
"""
Insira seu comentário
de mais linhas
"""
print("hello world") #Comentário inserido na linha do código



#1.2.COMANDO PRINT
print("hello world") #com aspas duplas
print('hello world') #com aspas simples

print('hello', 'world') #Saida: Hello World;
print ('hello' ,'world', sep="-") #Saida: hello-world;

print ('hello' ,'world', sep="-", end="")
print ('hello' ,'world', sep="-")  #Saida: hello-worldhello-world

print ('hello' ,'world', sep="-", end="###")
print ('hello' ,'world', sep="-") #Saida: hello-world###hello-world



#1.3.TIPOS DE DADOS PRIMITIVOS
"""
Tudo em python é um objeto, incluindo os tipos primitivos
O python é uma linguagem de tipagem dinamica, significa que se eu colocar o texto entre aspas, 
o python sabe que é uma string

str - String : Textos 'Exemplo' "Exemplo"
int - Inteiro: Numeros negativos e positivos 123456 -1 0 10 -10
float - real/ponto flutuante: casas decimais 5.2 -10.9
bool - booleano/lógico: TRUE/FALSO 5==5
"""

#1.3.1.STRING
print("Essa é uma 'string' (str).") #Inserindo a palavra string dentro da frase
print('Esse é meu \"texto\" (str).') #Inserindo caractere de escape para inserir a palavra texto
print(r'Esse é meu \n texto (str).') #Não executa códigos contidos como comandos






