magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + " that was a great trick")

print("thank everyone that was a great show")

for value in range(1, 5):
    print(value)

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# ou de forma mais concisa

for value in range(1, 11):
    squares.append(value**2)

print(squares)

players = ["charles", "martina", "michael", "florence", "eli"]
for player in players[:3]:
    print(player.title())
