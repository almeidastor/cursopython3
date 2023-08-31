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


#1.7.DESAFIO PRÁTICO (TESTE DE CONHECIMENTO ATÉ AQUI)
"""
* Criar variaveis para nome (str) e idade (int)
* Altura (float) e peso (float) de uma pessoa
* Criar uma variavel com o ano atual
* Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
* Obter o imc de uma pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String (com as chaves)
"""
nome = 'Regiane'
idade = 29
altura = 1.75
peso = 75
ano_atual = 2023
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print('meu nome é {}, {} de idade, altura: {}, ano de nascimento: {}, ano atual: {}, ano de nascimento {}, imc: {:2f}'.format(nome, idade, altura, peso, ano_atual, ano_nascimento, imc))


#1.8.INPUT ENTRADA DE DADOS DO USUÁRIO

input("Qual seu nome? ") #Exibe o cursor para digitar

nome = input('Qual seu nome? ')
idade  = input('Qual sua idade? ')
ano_nascimento = 2023 - int(idade) #converte idade para um inteiro

print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')

#1.8.1.CALCULADORA QUE SÓ FAZ SOMA

numero_1 = int(input('Digite um número: ')) #conversão direta pra numero
numero_2 = int(input('Digite outro número: ')) #conversão direta pra numero

print (numero_1 + numero_2)


#1.9.CONDIÇÕES IF, ELIF, E ELSE
#se verdadeiro
if True:
    print("Verdadeiro") #4 espaços para hierarquia

    num_1 = 2
    num_2 = 4
    print(num_1 + num_2)

#se falso
if False:
    print("Verdadeiro")
print("A minha expressão não é verdadeira")

#com  else
if False:
    print("Verdadeiro")
else:
    print("A minha expressão não é verdadeira")

# com o elif
if False:
    print("Verdadeiro")
elif True:
    print("Agora é verdadeiro")
elif False:
    print("Agora não é verdadeiro")
else:
    print("A minha expressão não é verdadeira")



#1.10.OPERADORES RELACIONAIS + IFELIFELSE
"""
= : Atribuição de valor
==: Igualdade
> : Maior que
< : Menor que
>=: Maior ou igual a
!=: Diferente
"""

print (2 == 2) #Imprime True
print (2 == 1) #Imprime False
print (2 == "2") #Imprime False

num_1 = 1
num_2 = 2
expressao = (num_1 >= num_2)

print(expressao)


#1.11.OPERADORES LÓGICOS + IFELIFELSE
"""
and : Verdadeiro E Verdadeiro
or
not
in
not in
"""

a = 2
b = 2
c = 3
compare = a == b and b < c
print(compare) #Exibe True na tela

#(Verdadeiro E Verdadeiro) = Verdadeiro
a == b and b < c

#(Verdadeiro OU Verdadeiro) = Verdadeiro
a == b or b < c

#(NOT) = Inverte o valor
a=2
b=3
if not b > a : #Adicionando o Não antes de b> que A
    print("B é maior que A")
else:
    print("A é maior que B") #Resultado que exibirá

#Verificação de uma variavel vazia
a=""
b= 0
if not a or b :
    print("Preencha o valor de A")
    print("Preencha o valor de B") #0 é considerado um booleano falso


#Verifica se há um valor contido na variavel
nome = "Luiz Otávio"
if "u" in nome:
    print("Existe a letra U no seu nome")
else:
    print("Não existe a letra U no seu nome")

#Verifica se não há um valor contido na variavel
nome = "Luiz Otávio"
if "vio" in nome:
    print("Executei")
else:
    print("Existe o texto")

#Checagem de usuário e senha
usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = 'Luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd  == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')


#1.12. len - QUANTIDADE DE CARACTERES
usuario = input ("Digite seu usuario: ")
qtd_caracteres = len(usuario) #Conta a quantidade de caracteres da variavel

if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")



#1.13.DOCUMENTAÇÕES E FUNÇÃO BUILT-IN UTEIS

#https://docs.python.org/pt-br/3/tutorial/

#1.13.1.String Methods
"""
São funções que conferem se a string pode ser convertida em números
isnumeric: Confere true se forem numeros inteiros e positivos
isdigit:
isdecimal
"""
num1 =input("insira um numero")
print(num1.isdecimal())

if num1.isdigit():
    num1 = int(num1) #converte para inteiro
    print(num1)
else:
    print("Não pude converter os números")

#tratamento de erros
try:
    num1 = float(num1)
    print(num1)
except:
    print("ERROR")


#1.14.PASS E ELLIPSIS COM PLACEHOLDERS
"""
Python não define blocos de código {}, então para deixar um lugar pronto para posteriormente escrever o código
podemos utilizar a palavrinha pass que é feita especialmente para evitar erros de identação
"""

valor = False
if valor:
    pass #Também pode ser usado ...
    ... #Ellipsis e pass possuem a mesma função nessa situação
else:
    print("tchau")


#1.15.EXERCICIOS PROPOSTOS
"""
Faça um programa que peça para o usuário digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro
"""
#RESPOSTA
num1 = input("Digite um número inteiro: ")
if num1.isdigit():
    num1 = int(num1)
    if num1%2 == 0:
        print("Numero par")
    else:
        print("Numero impar")
else:
    print("esse não é um numero inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada
bom dia: 0-11, boa tarde:12-17, boa noite: 18-23
"""
#RESPOSTA
hora = int(input("digite a hora atual hh"))
if hora >= 00 and hora <= 11:
    print ("Bom dia")
elif hora >= 12 and hora <= 17:
    print("Boa tarde")
elif hora >= 18 and hora <= 23:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto", se tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6
escreva "Seu nome é muito grande
"""
nome = input("Digite seu primeiro nome: ")
qtd_caracteres = len(nome)

if qtd_caracteres<=4:
    print("Seu nome é curto")
elif qtd_caracteres>=5 and qtd_caracteres<=6:
    print("Seu nome é normal")
elif qtd_caracteres>6:
    print("Seu nome é muito grande")


#1.15.FORMATANDO VALORES EM PYTHON
"""
FORMATANDO VALORES COM MODIFICADORES

:s - Texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
print('{:.2f}'.format(2/3)) #formata para apenas 2 casas decimais depois do numero inteiro (0.67)
print( f'{2/3:.2f}') #formato fstrings (0.67)
print(f'{"regiane":s}') #formato de strings
print(f'{1:0>10}') #preenchendo com 0's a esquerda de 1 até atingir quantidade de 10 (000 000 000 1)
print(f'{1150:0^10}') #preenchendo com 0's em torno do numero 1150 até atingir a quantidade de 10 (000 1150 000)
print(f'{1150:.2f}') #duas casas decimais depois de 1150 (1150.00)
print(f'{"regiane":#^25}') #preenche com # centrallizando o nome no meio até atingir 25 caracteres (#########regiane#########
print('{:@>10}'.format("Regiane")) #preenche com @ a esquerda do nome até completar 10 caracteres (@@@Regiane)
print('{n:0<10}'.format(n="Regiane")) #preenche com 0's a direita do nome até completar 10 caracteres (Regiane000)
print('{1}'.format("Regiane","Almeida")) #imprime com a numeração do indice (Almeida)

nome = "Regiane almeida"
print(nome.lower()) #tudo minusculo (regiane almeida
print(nome.upper()) #tudo maiusculo (REGIANE ALMEIDA)
print(nome.title()) #primeiras letras maiusculas (Regiane Almeida)


#1.16.INDICES E FATIAMENTO DE STRINGS EM PYTHON

"""
* String indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

Você pode conferir tudo isso em
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
#INDICES
#Positivos   [012345678]
#Negativos  -[987654321]
texto      = 'Python s2'
print (texto[2]) #Exibe t na tela
print (texto[-2]) #Exibe s na tela

#FATIAMENTO
#Para pegar o caractere 5, precisa colocar o numero 6
nova_string = texto[2:6] #Exibe thon na tela
nova_string = texto[-9:-3] #Exibe Python na tela

nova_string = texto[:6] #Para pegar desde o começo, só omitir o primeiro caractere
nova_string = texto[7:] #Para pegar do caractere para o final, só omitir o ultimo caractere
nova_string = texto[0:6:2] #Para pegar do primeiro caractere para o 5, pulando de 2 palavras (:2 é o step)
nova_string = texto[0:6:3] #Para pegar do primeiro caractere para o ultimo, pulando de 3 caracteres (:3 é o step)


#1.17.WHILE - ESTRUTURA DE REPETIÇÃO EM PYTHON
"""
Utilizado para realizar ações enquanto uma condição for verdadeira
"""

while True:
    nome = input("qual seu nome? ")
    print(f'Olá {nome}!') #loop infinito

print('Não será executado')

x=0
while x < 10:
    print(x)
    x = x + 1 #ou x+=1
print("Acabou")

x=0
while x < 10:
    if x ==3:
        x=x+1
        continue #o programa não executará o laço do mesmo bloco, vai dar seguimento ao código
        break #termina o laço
    print(x)
    x = x + 1
print("Acabou")

while True:
    print("Calculadora")
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input('Deseja sair? s ou n? ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número")
        continue

    if sair == 's':
        break

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "/":
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)
    else:
        print("operador inválido")


#1.18.WHILEELSE - REPETIÇÃO COM ACUMULADORES EM PYTHON

#1.18.1.CONTADOR
contador = 0
while contador < 10:
    print(contador)
    contador +=1


#1.18.2.ACUMULADOR
contador = 1
acumulador = 50
while contador <=10:
    print(contador, acumulador)
    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print("Cheguei no else")
print("Isso será executado")



#1.19.ITERANDO STRINGS COM WHILE EM PYTHON

#        indices
#        0123456..........................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase) #conta os 34 elementos
contador = 0
nova_string = ''

while contador < tamanho_frase:
    print(frase[contador] , contador)
    print('###############')
    nova_string += frase[contador]
    contador +=1
print(nova_string) #o rato roeu a roupa do rei de roma

input_do_usuario = input('Qual a letra que você gostaria de tornar maiuscula? ')
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string) #o Rato Roeu a Roupa do Rei de Roma

#1.20.FOR IN - ESTRUTURA DE REPETIÇÃO EM PYTHON
"""
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
for letra in texto:
    print(letra)

#1.20.1.FUNÇÃO RANGE
for numero in range (5,10,2): #start=5, stop=10, step=2
    print(numero)

for numero in range (20,10,-2): #start=20, stop=10, step=-2
    print(numero)

#1) Multiplos de 8
for n in range (0,100,8):
    print(n)

#2) Multiplos de 8
for n in range (100):
    if n % 8 == 0:
        print(n)

#3) Texto em maiusculo
text = 'Python'
nova_string = ""

for letra in text:
    if letra == 't':
        nova_string = nova_string + letra.upper() #deixa todas as letras T maiuscula
        continue #passa para o próximo código
    else:
        nova_string += letra
print(nova_string)


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

#del
del(l3[0:4]) #Remove uma série de elementos

#max-min
l2= [4,5,6]
print(max(l2)) #maior valor da lista
print(min(l2)) #menor valor da lista

#Range
"""
A função range cria uma cadeia de objetos, porem não em formato de lista e sim em formato de objeto range
"""
l2=range(1,9) #range(1,9)

"""
O Python tem uma função chamada list que converte um objeto iterável em uma lista
"""
l2= list(range(1,9)) #[1, 2, 3, 4, 5, 6, 7, 8]
l2= list(range(1,9,2)) #De 1 a 9 pulando de 2 em 2

#1.21.2.JOGO
secreto = 'perfume'
digitados = []
chances = 5

while True:
    if chances <=0:
        print('você perdeu')
        break

    letra = input("Digite uma letra: ")

    if len(letra)> 1:
        print("Ahhh, isso não vale, digite apenas 1 letra")
        continue

    digitados.append(letra)
    if letra in secreto:
        print(f"Uhuul, a letra {letra} existe na palavra secreta")
    else:
        print(f"Affz, a letra {letra} não existe na palavra secreta")
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
            print(f'Que legal, VOCÊ GANHOU!!! a palavra era {secreto_temporario}')
            break
    else:
            print(secreto_temporario)

    if letra not in secreto:
        chances-=1

    print(f'você ainda tem {chances} chances')


#1.22.FOR ELSE EM PYTHON
"""

"""
variavel = ['Luiz Otavio','Joaozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print("Não existe uma paavra que começa com j")


#1.23.SPLIT, JOIN E ENUMERATE EM PYTHON
"""
* Split: Dividir uma String # str
* Join: Juntar uma lista # str
* Enumerate: Enumerar elementos da lista # list / iteraveis
"""

#1.23.1.SPLIT
string = "O Brasil é o Pais do futebol, o Brasil é penta"
lista = string.split(' ')
print(lista) #['O', 'Brasil', 'é', 'o', 'Pais', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']
lista = string.split(',')
print(lista) #['O Brasil é o Pais do futebol', ' o Brasil é penta']

#1.23.2.JOIN
lista = ['O', 'Brasil', 'é', 'o', 'Pais', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']
string2 = ",".join(lista)
print(string2) #O,Brasil,é,o,Pais,do,futebol,,o,Brasil,é,penta


#1.23.3.ENUMERATE
lista = ['Luiz', 'Joao', 'Maria']
for indice, nome in enumerate (lista):
    print(indice,nome)
    #0 Luiz
    #1 Joao
    #2 Maria


#1.24.DESEMPACOTAMENTO DE LISTAS EM PYTHON
"""
"""
lista = ['Luiz', 'Joao', 'Maria', 1,2,3,4,5,6,100]
n1,n2, *outra_lista, ultimo_da_lista = lista
print(n1,n2) #Luiz Joao
print(outra_lista) #['Maria', 1, 2, 3, 4, 5, 6, 100]
print(ultimo_da_lista) #100

*outra_lista, n1,n2, ultimo_da_lista = lista
print(outra_lista, n1,n2,ultimo_da_lista) #['Luiz', 'Joao', 'Maria', 1, 2, 3, 4] 5 6 100


#1.25.TROCANDO O VALOR DE VARIÁVEIS EM PYTHON
"""
"""
x = 10
y = 'Luiz'
z = 'Otavio'
x, y = y, x

print(f'x= {x} y= {y}') #x= Luiz y= 10

x, y, z = z, x, y
print(f'x= {x} y= {y} z= {z}') #x= Otavio y= Luiz z= 10


#1.26.OPERAÇÃO TERNÁRIA EM PYTHON
"""
"""
logged_user = True
msg = 'Usuario logado' if logged_user else 'usuario precisa logar'
print(msg) #Usuario logado

idade = 17
e_de_maior = (idade >=18)
msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
print(msg) #Não pode acessar


#1.27.EXPRESSÃO CONDICIONAL COM OPERADOR OR
"""
"""
nome = input('Qual seu nome? ')
print (nome or 'Você não digitou nada!') #Você não digitou nada!
print (nome or None or False or 'Você não digitou nada!') #Você não digitou nada!


#1.28.DESAFIO DE CONTADORES
"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

contador = 10
acumulador = 0

for acumulador in range (0,9):
    print(acumulador,contador)
    contador -= 1

for p, r in enumerate (range(10,1, -1)):
    print(p,r)

