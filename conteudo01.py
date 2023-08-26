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