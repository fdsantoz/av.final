# colocando o salario
salario = float(input("qual o valor do seu salario?"))
# calculo de quanto a pessoa vai pagar de imposto de renda 
if salario > 0 and salario < 2000.00:
# mostrando imposto
    print("isento")
elif salario >= 2000.01 and salario < 3000.00:
    imposto = (salario * 8)/100
    print (imposto)
elif salario >= 3000.01 and salario < 4500.00:
    imposto = (salario * 18)/100
    print (imposto)
elif salario >= 4500.00:
    imposto = salario *(28/100)
    print (imposto)