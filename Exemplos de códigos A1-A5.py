# --Exemplos de Códigos--

# --Simulação - Aumento salarial com Operadores Aritméticos--

# Exemplo 1 - Simples
"""
salario = 2300

aumento = salario + salario * 20//100

print(f"O salário antigo era de R$: {salario}\nCom 20% de aumento será R$: {aumento}")
"""

# Exemplo 2 - Boostcode
"""
salario1 = int(input("Insira o salário que receberá reajuste: R$ "))
porcentagem = int(input(f"Insira a % que deseja calcular do valor {salario1}: "))
reajuste = salario1 * porcentagem / 100

print(f"Valor Bruto: R${salario1}")
print(f"{porcentagem}% do Salário de R${salario1} é R${salario1 * porcentagem / 100}")
print(f"O salário de {salario1} com {porcentagem}% de aumento é: R$ {salario1 + reajuste}")
print(f"O salário de {salario1} com {porcentagem}% de desconto é: R$ {salario1 - reajuste}")
"""

# --Simulação - Cálcula de Notas Escolares--
"""
nota1 = float(input("Insira a PRIMEIRA nota \n"))
nota2 = float(input("Insira a SEGUNDA nota \n"))
nota3 = float(input("Insira a TERCEIRA nota \n"))
nota4 = float(input("Insira a QUARTA nota \n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média entre as notas: \n{nota1}\n{nota2}\n{nota3}\n{nota4}")
print(f"Resulta em: {media:.2f}")
"""

# --Simulação - Cálcula de Notas Escolares--
"""
valor = int(input("Insira um valor \n"))

print(f"O sucessor do valor {valor} é: {valor + 1}\nE seu antecessor é: {valor - 1}")
"""

# --Simulação - Km rodados de Carro de Aluguel--
"""
km_rodados = float(input("Insira a Quantidade de Km Rodados: \n"))
dias_alugados = int(input("Insira a quantidade de dias alugados: \n"))
total_a_pagar = dias_alugados * 60 + km_rodados * 0.15

print(f"Total de Km Rodados {km_rodados:.0f} ")
print(f"Total de dias alugados {dias_alugados}")
print(f"O Total à pagar pelo uso do veículo é: R${total_a_pagar:.2f}")
"""
