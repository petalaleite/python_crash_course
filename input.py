message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell me who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "  # cria uma string multilinha
# += acrescenta a nova string no final da string
# que estava armazenada o prompt.
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age)

age = int(age)  # converte o valor para uma representação numérica
print(age >= 18)

height = input("How tall are you? ")
height = int(height)

if height >= 150:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")


prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program\n\t"

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)


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
    print(name + " would like to climb " + response + ".")

print(responses)
