def greet_user(username):
    """Exibe uma saudação simples"""
    print("Hello, " + username.title() + "!")


greet_user("jack")


def describe_pet(anima_type, pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a " + anima_type + ".")
    print("My " + anima_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")

# argumentos nomeados

describe_pet(anima_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", anima_type="hamster")

# valores default


def describe_pet(pet_name, anima_type="dog"):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a " + anima_type + ".")
    print("My " + anima_type + "'s name is " + pet_name.title() + ".")


describe_pet("willie")
# quando um argumento explícito para animal_type for especificado,
# Python ignorará o valor default do parâmetro


def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de forma elegante"""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

# deixando um argumento opcional


def get_formatted_name(first_name, middle_name, last_name):
    """Devolve um nome completo formatado de forma elegante"""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)


def get_formatted_name(first_name, last_name, middle_name=""):
    """Devolve um nome completo formatado de forma elegante"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee")
print(musician)


# devolvendo um dicionário


def build_person(first_name, last_name):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)


def build_person(first_name, last_name, age=""):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)


# /! usando uma função com um laço while


def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de forma elegante"""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at anytime to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# passando uma lista para uma função


def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# passando um número arbitrário de argumentos


def make_pizza(*toppings):
    """Exibe list de ingredientes pedidos."""
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# misturando argumentos posicionais e arbitrários


def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
    )
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# usando argumentos nomeados arbitrários


def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)

# armazenando funções em módulos

import nome_do_modulo

nome_do_modulo.nome_da_funcao()
from nome_do_modulo import nome_da_funcao
from nome_do_modulo import nome_da_funcao as nf
import nome_do_modulo as nm

# importando todas as funções de um módulo

from nome_do_modulo import *
