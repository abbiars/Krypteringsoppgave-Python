
print("Select a mode\n1 = encrypt\n2 = decrypt\n")

prompt = int(input(">"))

def kryptering(Krypter):




def dekryptering(Dekrypter):



def checkInt(inp):
    if inp != type(int):
        print("the input provided is not a Int")
    else:
        return

if prompt == 1:
    Krypter = input("Skriv det du vil kryptere: ")

elif prompt == 2:
    Dekrypter = input("Skriv det du vil dekryptere: ")
else:
    print("invalid input")



krypter = input("")
print(Krypter[::-1])