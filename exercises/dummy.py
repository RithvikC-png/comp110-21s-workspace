
phrase: str = str(input("What phrase would you like to repeat? "))
count: int = int(input("How many times would you like to repeat? "))


if count <= 0:
    print("No beat")
while count > 0:
    print((phrase + " ") * count)
    count = count - count