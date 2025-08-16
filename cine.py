print ("Bienvenido a Caribbean Cinemas.")

print('''
OFERTAS DISPONIBLES:
      
     1- Menores de 12 años pagan RD$150.

     2- Entre 12 y 17 años pagan RD$200.

     3- Entre 18 y 59 años pagan RD$300.

     4-  Mayores de 60 años pagan RD$180.
'''
)

edad= int (input ("Ingresa tu edad: "))

if edad < 0 or edad > 120:
    print ("Edad invalida.")

elif edad < 12:
    print (f"Monto a pagar: RD$ {150}")

elif edad <= 17:
    print (f"Monto a pagar: RD$ {200} ")

elif edad <= 59:
    print (f"Monto a pagar: RD$ {300}")

else:
    print (f"Monto a pagar: RD$ {180}")