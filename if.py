cars = ["audi", "bmw", "ferrari", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("hold the anchovies!")


answer = 17
if answer != 42:
    print("That's not the correct answer!. please try again")

age = 19
if age >= 18:
    print("You are old enough to vote")

age = 17
if age >= 18:
    print("You're old enough to vote!")
    print("Have you registered yet?")
else:
    print("Sorry, you are too young to vote")


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza.")


requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we're out of green peppers right now")
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza")

# usando várias listas
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, We dont have " + requested_topping + ".")

print("\nFinished making your pizza")
