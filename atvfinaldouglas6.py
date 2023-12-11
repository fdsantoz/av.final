#crio uma lista e outra para os numeros positivos
lista = []
positivos = []
#usei um range para repetir
for i in range(0,7):
    val = float(input("Digite um valor: "))
    #adiciono os valores a lista 
    lista.append(val)
#identifico os positivos
for val in lista:
    if val > -1 :
        #adiciono a variavel
        positivos.append(val)
#uso a função len pra mostrar a quantidade de numeros positivos
quantidade= len (positivos)
 
# divido e consigo a media dos numeros positivos 
media = (sum(positivos)) / quantidade

#mostro o resultado da media e quantidade de numeros positivos
print(f"tem {quantidade}numeros\n valores positivos{positivos}")
print(f"A media dos numeros positivos é {media}")
