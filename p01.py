lista = []
for i in range(3):
    numeros = int(input(f"Digite o numero {i+1}: "))
    lista.append(numeros)
lista.sort(reverse=True)
print(f"Este são os números na ordem inversa:{lista}")