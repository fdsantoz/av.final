# crio uma lista de numeros e outra com numeros pares
lista = []
pares = []
# crio um for e range para pedir os 5 numeros
for numeros in range(0,6):
    numero = int(input(" Digite um numero inteiro "))
    lista.append(numero)
#indentifico os numeros pares
for inteiros in lista:
    if inteiros % 2 == 0:
        pares.append(inteiros)
# uso a funçao len para indentificar o numeros pares
par = len(pares)
print(f"São {par} numeros pares \n Os valores pares são {pares}")