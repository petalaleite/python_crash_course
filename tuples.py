# As vezes você vai querer criar uma lista de itens que não poderá mudar.
# As tuplas permitem fazer exatamente isso. Python refere-se as valores
# que não podem  mudar como imutáveis, e uma lista imutável é chamada de tupla.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# percorrendo os valores de uma tuple com um laço for

for dimension in dimensions:
    print(dimension)

# sobrescrevendo uma tupla
# Embora não seja possível modificar uma tupla, podemos atribuir um novo valor
# a uma variável que armazena um tupla

dimensions = (400, 100)
print(dimensions)
