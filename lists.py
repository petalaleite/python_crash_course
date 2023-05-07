bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# acessando elementos de uma lista

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])  # sempre devolve o último elemento da lista

message = "My first bike was a " + bicycles[0].title() + "."
print(message)

names = ["alyda", "aline", "ebraim", "luciano", "pedro", "lais"]
print(names)

# modificando elementos de uma lista

motorcycles = ["honda", "ducatti", "suzuki"]
print(motorcycles)
motorcycles[0] = "yamaha"  # altera o valor do item
print(motorcycles)

# acrescentando elementos
# .append() - acrescenta ao final da lista, só recebe um argumento

motorcycles.append("ducati")
print(motorcycles)

# .insert() - adiciona um elemento em qualquer posição da lista
motorcycles.insert(0, "honda")
print(motorcycles)


# removendo itens de uma lista
# se o index for conhecido - del
del motorcycles[1]
print(motorcycles)


# .pop() - remove o item do final da lista e salva o item
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

# .pop() também pode remover em qualquer posição

first_owned = motorcycles.pop(1)
print(first_owned)


# removendo um item de acordo com o valor - .remove()
# esse método apaga somente a primeira ocorrência do valor
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)


# ordenar uma lista de forma permanente - sort()
cars = ["bmw", "audi", "toyota", "ferrari"]
cars.sort()
print(cars)

cars.sort(reverse=True)  # ordem alfabética inversa
print(cars)

# ordenar temporariamente sem alterar a original - sorted()
print("Original list: ", cars)
print("Sorted list: ", sorted(cars))
print(sorted(cars, reverse=True))


# inverter a ordem original de uma list - reverse()
print(cars)
cars.reverse()
print(cars)


# descobrindo o tamanho de uma lista
print(len(cars))


# usando range() para criar uma lista de números
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


# valor mínimo, valor máximo, soma de uma lista de números
# min()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

# max()
print(max(digits))

# sum()
print(sum(digits))

# * LIST COMPREHENSIONS
# Uma list comprehensions combina o laço for e a criação de novos elementos
# em uma linha, e concatena cada novo elemento automaticamente

squares = [value**2 for value in range(1, 11)]
# primeiro define a expressão para os valores que quer armazenar na lista
# (ex: value**2)

print(squares)

# fatiando uma lista

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[:4])
print(players[2:])
# um índice negativo devolve um elemento a uma determinada
# distância do final de uma lista
print(players[-3:])

# copiando uma lista
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]
print(friends_foods)

my_foods.append("avocado")
friends_foods.append("sushi")
print("My foods list:", my_foods)
print("Friend's foods list: ", friends_foods)

# isso faz python apontar as duas variáveis para uma mesma lista na memória
# então ao modificar uma, a outra consequentemente seria alterada
friends_foods = my_foods


# verificando se um valor está em uma lista
requested_toppings = ["mushrooms", "onions", "pickes"]
print("mushrooms" in requested_toppings)
# A palavra reservada 'in' diz ao python para verificar a
# existência do valor na lista


# verificando se um valor não está em uma lista
banned_users = ["andrew", "carolina", "david"]
user = "marie"
print(user not in banned_users)

# transferindo itens de uma lista para outra

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# removendo todas as instâncias de valores específicos de uma lista

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)
