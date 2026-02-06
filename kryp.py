
print("Select a mode\n1 = encrypt\n2 = decrypt\n")

prompt = int(input(">"))


if prompt == 1:
    Krypter = input("Skriv det du vil kryptere: ")
    print(Krypter[::-1])

elif prompt == 2:
    Dekrypter = input("Skriv det du vil dekryptere: ")
    print(Dekrypter[::-1])
else:
    print("invalid input")



krypter = input("")
print(Krypter[::-1])