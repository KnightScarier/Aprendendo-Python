# --Aula 2 - Variáveis--

# <-- Tipos de Variáveis e Suas Funções-->

"""
Str, Bool, Int, ou Float
"""

# --Comandos Utilizados--

"""
print = Retorna qualquer tipo de texto em um string
\n = Faz uma quebra de Linha
{} = Cria uma dicionário em Python
"""

# Conceito: Variáveis são espaço de alocamento na memória.

"""
Var: int, float, str e bool

Ex:print(nome) - 'nome' é a função que está ocupando espaço na memória
nome = "Ricardo" - Nome da pessoa que retornará, nesse caso: 'Ricardo'
idade = 22 - idade da pessoa que retornará, nesse caso: '22'
"""

# <-- Exemplo de Funcionalidade dessas variáveis -->

"""
#Classes Aplicadas: (nome e idade)
"""

nome = "Ricardo"  # parâmetro *aplicado*
idade = 22  # parâmetro *aplicado*
peso = 45.77  # parâmetro *aplicado*
sexo = "Masculino"  # parâmetro *aplicado*

"""
Exemplo: 'Antigo' print("Olá, Meu nome é", nome,"Minha idade é", idade,)

Exemplo1: 'Mais Recente' print("Olá, Meu nome é {}\nEu tenho {} Anos".format (nome,idade))

Exemplo2: 'Atual' print(f"Olá, Meu nome é {nome}\nEu tenho {idade} Anos,{peso}\nquilos e meu sexo é {sexo}")
"""

# <-- Exemplo com números -->
"""
Variáveis são espaço de alocamento na memória.

Var: int, float, str e bool
"""

pi = 3.14

# parte_inteira = int(pi)

# print(f"O valor de pi é {pi}\nA parte inteira de pi é {parte_inteira}")

# <-- Variantes do código acima -->

# Código retornará 'pi' como Float

print(f"Pi antes valia : {pi}\nE seu tipo é {type(pi)}")

# Código de variável que retorna apenas a parte inteira de 'pi'
pi = int(pi)

# Código retornará 'pi' como Inteiro *Código 'pi = int (pi)' aplicado*
print(f"Agora pi vale:{pi}\nE seu tipo é {type(pi)}")

# Código passará a retornar 'pi' como uma string
pi = str(pi)
print(f"Pi agora é uma string e seu tipo é {type(pi)}")

# <!-----Exemplo de outro tipo de valor, nas mesmas condições----->

# Para teste apenas excluir as aspas triplas.

# Ex_Float passará a substituir 'pi' do exemplo anterior.
"""
Ex_Float = 1100.5854

parte_inteira = int(Ex_Float)

print(f"O valor de Ex_Float é {Ex_Float}\nA parte inteira de Ex_Float é {parte_inteira}")
"""
# <-- Variantes -->

# Código retornará 'Ex_Float' como Float
"""
print(f"Ex_Float antes valia : {Ex_Float}\n E seu tipo é {type(Ex_Float)}")
"""
# Código de variável que retorna apenas a parte inteira de 'pi'
"""
Ex_Float = int(Ex_Float)
"""
# Código retornará 'pi' como Inteiro *Código 'pi = int (pi)' aplicado*
"""
print(f"Agora Ex_Float vale:{Ex_Float}\nE seu tipo é {type(Ex_Float)}")
"""
# Código passará a retornar 'pi' como uma string
"""
Ex_Float = str(Ex_Float)""
print(f"Ex_Float agora é uma string e seu tipo é {type(Ex_Float)}")
"""
