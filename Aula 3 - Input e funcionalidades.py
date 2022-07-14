# --Aula 3 - Input e suas funções--

# <-- Relembrando a Aula 2 - Tipos de Variáveis e Suas Funções-->

"""
str, bool, int, ou float
"""

# --Comandos Utilizados--

"""
Aula 2 - (print,\n,{})
Input
"""

# Aula 2 - Ricardo
# para testar o código, basta retirar as aspas triplas

"""
nome = "Ricardo"
idade = 24
peso = 70.55

print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso é {peso}kg")
"""

# Como utilizar o Input
# para testar o código, basta retirar as aspas triplas

"""
nome = str(input("Insira seu Nome: "))
idade = int(input("Insira sua Idade: "))
peso = float(input("Insira seu peso: "))


print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso é {peso}kg")

# Por que utilizar dessa maneira? E se não especificarmos as variáveis?
"""

##Obs: Para que não haja erros de formatação, como no exemplo abaixo:


# Observe que o 'input' não está especificando qual a variável (str,int,bool ou float) do dado inserido
# para testar o código, basta retirar as aspas triplas

"""
nome = input("Insira seu Nome: ")
idade = input("Insira sua idade: ")
peso = input("Insira seu Peso: ")

# Aqui veja que ao executar, retornará a <class 'str'> - Variável de String
print(f"Meu nome é: {nome}{type(nome)}")
# Assim como no dado 'idade' <class 'str'> sendo neste caso, a variável Int para Idade
print(f"Minha idade é: {idade}{type(idade)}")
# Assim como no dado 'peso' <class 'str'> sendo neste caso, a variável Float para Idade
print(f"Meu peso é: {peso}{type(peso)}")
"""

# Diferença entre um dado String e um dado Inteiro

# Perceba que no parâmetro 'string' há a presença de aspas pois o dado de 'string' retornará um texto

string = "10"  # parâmetro de str

# Perceba que na variante 'inteiro' não há a presença de aspas, pois o dado de 'inteiro' retornará um número
inteiro = 10  # parâmetro de int

# Exemplos da diferença entre essas variáveis com códigos

# Perceba que neste código, a soma se dá porque 'inteiro' é equivalente a 10, aplicado no parâmetro anterior
print(inteiro + 10)  # por isso, este código retornará 10+10 = 20
print(string + "10")  # por isso, este código retornará "10"+"10" = 1010, pois considera ambos como texto.

# para melhor visualização: da diferença que há entre eles
# para testar o código, basta retirar as aspas triplas

"""
string = "10"
inteiro = 10

print(type(string))
print(type(inteiro))
"""
