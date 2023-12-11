#colocando o salario
salario = float(input("qual o seu salario atual? "))
#os calculos do aumento
if salario > 0 and salario <= 400:
   aumento = (salario*15)/100
   comaumento = salario + aumento
   #mostrando o novo salario do aumento e a porcentagem
   print(f"novo salario: {comaumento} \n reajuste ganho: {aumento} \n em porcentual: 15%")
elif salario > 400.01 and salario < 800:
   aumento = (salario*12)/100
   comaumento = salario + aumento
   print(f"novo salario: {comaumento} \n reajuste ganho: {aumento} \n em porcentual: 12%")
elif salario > 800.01 and salario < 1200:
   aumento = (salario*10)/100
   comaumento = salario + aumento
   print(f"novo salario: {comaumento} \n reajuste ganho: {aumento} \n em porcentual: 10%")
elif salario > 1200.01 and salario <2000:
    aumento = (salario*7)/100
    comaumento = salario + aumento
    print(f"novo salario: {comaumento} \n reajuste ganho: {aumento} \n em porcentual: 7%")
else:
   aumento = (salario*4)/100
   comaumento = salario+aumento
   print(f"novo salario: {comaumento} \n reajuste ganho: {aumento} \n em porcentual: 4%")
   