nota= int(input ("Ingrese su nota: "))

if nota < 0 or nota > 100:
    print ("Nota invalida")

elif nota < 60:
    print ("F")

elif nota <= 69:
    print ("D")

elif nota <= 79:
    print ("C")

elif nota <= 89:
    print ("B")

else:
    print ("A")
