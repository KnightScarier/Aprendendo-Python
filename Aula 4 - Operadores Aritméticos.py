# --Aula 4 - Operadores Aritméticos--

# --Comandos Utilizados--

"""
print(...)
"""

# Tipos de Operadores Aritméticos

""" 
+ Soma

- Subtração

* Multiplicação

** Exponenciação

/ Divisão

// Divisão Inteira

% Resto da divisão ou Módulo

"""

# Exemplos de Tipos de Operadores Aritméticos
# para testar os códigos, basta retirar as aspas triplas
"""
# Soma
print(1 + 1)

# Subtração
print(2 - 1)

# Multiplicação
print(2 * 2)

# Exponenciação
print(5 ** 2)

# Divisão
print(5 / 2)  # Resultado: 2.5 = Var_Float

# Divisão Inteira # Resultado: 2 = Var_Inteiro - Se dá pelo fato de que '//' retorna apenas valores inteiros
print(5 // 2)

# Resto da divisão ou Módulo
print(5 % 2)  # Caso o resultado retornar com casas decimais, será apresentado 1'
print(5 % 5)  # Caso o resultado não retornar com casas decimais, apresentará '0'
"""

# Ordem de Procedência
"""
1º () - Parênteses
2º ** - Valores Exponenciais
3º * Multiplicação, / Divisão, % Módulo e // Divisão Inteira
4º + Soma e - Subtração
"""

# Exemplo de Ordem de Procedência
# para testar os códigos, basta retirar as aspas triplas
"""
print(5 + 5)  # Resultado: 10
print(5 + 5 * 2)  # Resultado = 15, pois o Python reconhece pela ordem, que 5*2 = 10 + 5 = 15

# Exemplo de Prioridade na Ordem de Procedência
print((5 + 5) * 2)  # Resultado = 20, pois o Python reconhece primordialmente o que está em parênteses.
"""
