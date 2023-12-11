#pede o numero do usuario 
numero = int(input(f"para descobrir onde é seu DDD digite seu telefone: "))
#salva os dois primeiros digitos da variavel
numero = int(str(numero)[:2])
#ele vai comparar os dois primeiros digitos do numero de telefone
if numero == 61:
    print("brasilia")
elif numero == 71:
    print("salvador")   
elif numero == 11:
    print("salvador")
elif numero == 21:
    print("Rio de jameiro")
elif numero == 32 :
    print("juiz de fora")
elif numero == 19 :
    print("campinas")
elif numero == 27 :
    print("vitoria")
elif numero == 31 :    
    print("belo horizonte")
else:
    print("DDD nao encontrado")                                             