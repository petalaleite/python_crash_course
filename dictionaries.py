# um dicionário simples

alien_0 = {"color": "green", "points": 5}
print(alien_0)

# acessando valores em um dicionário
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points")

# adicionando novos pares

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# começando com um dicionário vazio

alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# modificando valores em um dicionário

alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is " + alien_0["color"] + ".")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("Alien new x-position: " + str(alien_0["x_position"]))

# removendo pares chave-valor

del alien_0["points"]
print(alien_0)

#

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(
    "Sara's favorite language is " + favorite_languages["sarah"].title() + "."
)

person = {
    "first_name": "Ed",
    "last_name": "Eddington",
    "age": 21,
    "city": "SP",
}

print(person["first_name"])

# percorrendo todos os pares com um laço

user_0 = {"username": "efermi", "first": "enrico", "last": "fermi"}
print(user_0.items())

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# percorrendo todas as chaves de um dicionário com um laço

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name)

friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(
            f"Hi, {name.title()}, I see your favorite language is {favorite_languages[name].title()}!"
        )

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll")

print(favorite_languages.keys())

# percorrendo as chaves de um dicionário em ordem usando um laço

for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll")

# percorrendo todos os valores de um dicionário com uma laço

for language in favorite_languages.values():
    print(language.title())

# Quando colocamos set() em uma lista que contenha itens duplicados, Python
# identifica os itens únicos na lista e cria um conjunto a partir desses itens.
for language in set(favorite_languages.values()):
    print(language.title())

# uma lista de dicionários

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# um exemplo mais realista envolveria mais três alienígenas, com um código
# que gere automaticamente cada alienígena
aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)

# uma lista em um dicionário

pizza = {"crust": "thick", "toppings": ["pepperoni", "extra cheese"]}
print(
    f'You ordered a {pizza["crust"]}-crust pizza with the following toppings:'
)
for topping in pizza["toppings"]:
    print("\t" + topping)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n {name.title()}'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# um dicionário em um dicionário

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {"first": "marie", "last": "curie", "location": "paris"},
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull Name: " + full_name.title())
    print("\tlocation: " + location.title())


# preenchendo um dicionário com dados de entrada do usuário

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like yo climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "would like to climb" + response + ".")
