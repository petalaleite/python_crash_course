class Dog:
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self, name, age) -> None:
        """Inicializa os atributos name e age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado em resposta a um comando"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title() + " rolled over!")


# uma função que faz parte de uma classe é um método
# o método __init__() é um método especial que Python executa automaticamente
# sempre que criamos uma nova instância baseada na classe
# O parâmetro self é obrigatório na definição do método e deve estar antes
# dos demais parâmetros
# Toda chamada de método associada a uma classe passa self, que é uma
# referência à própria instância
# Qualquer variável prefixada com self está disponível a todos
# os métodos da classe

# Criando uma instância a partir de uma classe

my_dog = Dog("Willie", 6)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# chamando métodos

my_dog.sit()
my_dog.roll_over()

# criando várias instâncias

your_dog = Dog("lucy", 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()


# trabalhando com classes e instâncias


class Car:
    """Uma tentativa simples de representar um carro"""

    def __init__(self, make, model, year) -> None:
        """Inicializa os atributos que descrevem um carro"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

# definindo um valor default para um atributo


class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # valor default

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modificando valores de atributos
# modificando o valor de um atributo diretamente

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modificando o valor de um atributo com um método


class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car("audi", "a4", 2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(2)

# incrementando o valor de atributo com um método


class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro"""
        self.odometer_reading += miles


my_used_car = Car("subaru", "outback", 2013)
print(my_used_car.get_descriptive_name())

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.increment_odometer(500)
my_used_car.read_odometer()
