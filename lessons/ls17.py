"""Examples of dictionaries."""

# Establish a type with dick[key type, value type]
# Empty dictionary literal is {}
players: dict[str, int] = {}
# Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 5

print(players)