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
"""
nome = "Ricardo"
idade = 24
peso = 70.55

print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso é {peso}kg")
"""

# Como utilizar o Input

nome = str(input("Insira seu Nome: "))
idade = int(input("Insira sua Idade: "))
peso = float(input("Insira seu peso: "))


print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso é {peso}kg")

# Por que utilizar dessa maneira? E se não especificarmos as variáveis?

"""
##Obs: Para que não haja erros de formatação, como no exemplo abaixo:
"""

# Observe que o 'input' não está especificando qual a variável (str,int,bool ou float) do dado inserido
# para testar o código, basta tirar as aspas triplas

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
