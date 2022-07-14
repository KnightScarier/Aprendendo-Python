# --Aula 5 - Operadores Lógicos--

# --Comandos Utilizados--

"""
print(...)
print(type(...))
"""

# Tipos de Operadores Lógicos

""" 
> Maior

>= Maior ou Igual

< Menor

<= Menor ou Igual

== Igual

!= Diferente

"""

# Exemplos de Tipos de Operadores Lógicos

# Utilização de '=='
# para testar os códigos, basta retirar as aspas triplas
"""
igual_1 = "Geraldo"  # parâmetro de str
igual_2 = "Roberto"  # parâmetro de str

print(igual_1 == igual_2)  # "==" identifica que o Parâmetro de 'igual_1' não é igual ao parâmetro de 'igual2'
print(type(igual_1 == igual_2))  # O Resultado retorna que a Variante é da classe "bool" = 'False' [-> Aula 1]
"""

# Caso 1 - '=='
# Retornará como "<class 'bool'> = False", pois uma var 'int' não é o mesmo que uma 'str'
"""
igual_3 = 99  # parâmetro de int
igual_4 = "Roberto"  # parâmetro de str

print(igual_3 == igual_4)  # "==" identifica que o Parâmetro de 'igual_3' não é igual ao parâmetro de 'igual_4'
"""

# Caso 2 - '=='
# Retornará como "<class 'bool'> = False", pois o valor de 'igual_5' é diferente do valor de 'igual_6'
"""
igual_5 = 99  # parâmetro de int
igual_6 = 9 # parâmetro de int

print(igual_5 == igual_6)  # Se dá pelo fato de '9' não ser igual a '99'
"""


# Caso 3 - Solução - '=='
# Retornará como "<class 'bool'> = True", pois a class de ambos é 'bool'
"""
iguals_5 = 99
iguals_6 = 9

print(type(iguals_5) == type(iguals_6))  # com o comando type adicionado, fará a comparação das classes, não dos valores
"""

# Utilização de '>'
# Retornará como "True", pois 'maior1' é maior que 'maior2'
"""
maior1 = 10.10
maior2 = 5.1

print(maior1 > maior2)
"""

# Utilização de '>='
# Retornará como "True", pois 'maiorigual1' é maior que 'maiorigual2'
# Também retornará como "True", se 'maiorigual1' possuir o mesmo valor que 'maiorigual2'
"""
maiorigual1 = 50.5
maiorigual2 = 50.2

print(maiorigual1 > maiorigual2)
"""

# Utilização de '<'
# Retornará como "False", pois 'menor1' é menor que 'menor2'
"""
menor1 = 50.5
menor2 = 50.2

print(menor1 < menor2)
"""

# Utilização de '<='
# Retornará como "False", pois 'menorigual1' é menor que 'menorigual2'
# Também retornará como "True", se 'menorigual1' possuir o mesmo valor que 'menorigual2'
"""
menorigual1 = 22.8
menorigual2 = 7.7

print(menorigual1 <= menorigual2)
"""

# Utilização de '!='
# Retornará como "True", pois 'diferente1' possui valor não semelhante à 'diferente2'
"""
diferente1 = 22.8
diferente2 = 7.7

print(diferente1 != diferente2)
"""

# Exemplo de uso da Aula 4 + Aula 5 (Operadores Aritméticos + Lógicos)
# Resultado: "False", pois a prioridade Aritmética é '()', sendo "15" do 1º resultado diferente de "20" do 2º resultado
"""
print(5 + 5 * 2 == (5 + 5) * 2)
"""
