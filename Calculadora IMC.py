#calculadora IMC

peso= float (input ("Ingrese su peso: "))
altura= float (input ("Ingrese su altura: "))

if peso / altura ** 2  < 18.5 :
    print ("Bajo peso")

elif peso / altura ** 2 == 18.5 or peso / altura **2 <= 24.9:
    print ("Normal")

elif peso / altura ** 2 ==  25 or peso / altura ** 2 <= 29.9:
    print ("Sobrepeso")

else:
   print ("Obesidad")









