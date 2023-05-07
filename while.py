current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nEnter quit to end the program"
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

# usando 'break'

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# usando 'continue' em um laço

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# evitando loops infinitos
x = 1
while x <= 5:
    print(x)
    x += 1  # se você omitir essa linha o laço executará para sempre (crash)
