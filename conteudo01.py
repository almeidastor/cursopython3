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