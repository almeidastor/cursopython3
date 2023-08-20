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
print(type('Luiz')) #Retorna o tipo utilizado no código: Saida <class 'str'>
print(type(int('20'))) #Retorna o tipo convertido no código: Saida <class 'int'>

#1.3.1.STRING
print("Essa é uma 'string' (str).") #Inserindo a palavra string dentro da frase
print('Esse é meu \"texto\" (str).') #Inserindo caractere de escape para inserir a palavra texto
print(r'Esse é meu \n texto (str).') #Não executa códigos contidos como comandos



#1.4.OPERADORES ARITMÉTICOS
"""
+ : Soma ou concatenação
- : Subtração
* : Multiplicação
/ : Divisão
// : Divisão inteira
** : Exponenciação
% : Resto da divisão
() : Parenteses - Precedencia
"""

print (10 * 10) #Multiplicação
print (10 - 5) #Subtração
print ((5 + 2) * 10) #Precedencia



#1.5.VARIÁVEIS
"""
Iniciar com letras
Pode conter números
Separar com _
Letras Minúsculas
"""
nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2023
peso = 80
imc = peso / (altura**2)

print ('Nome:', nome)
print ('Idade:', idade)
print ('Altura:', altura)
print ('É Maior', e_maior)

#1.5.1.CÁLCULO DE IMC
print (nome, 'tem', idade, 'anos de idade, e seu imc é', imc)


#1.6.INTRODUÇÃO A FORMATAÇÃO DE STRINGS
print (f'{nome} tem {idade} anos de idade, e seu imc é {imc}') #exibe a mesma formula
print (f'{nome} tem {idade} anos de idade, e seu imc é {imc:.2f}') #altera a quantidade de casas decimais para 2
print ('{} tem {} anos de idade e seu imc é {:2f}'.format(nome, idade, imc)) #formatação por nome
print ('{2} {0} {0} tem {1} anos e seu imc é {2:2f}'.format(nome, idade, imc)) #formatação por numero
print ('{n} tem {i} anos e seu imc é {im:2f}'.format(n=nome, i=idade, im=imc)) #formatação por letra


