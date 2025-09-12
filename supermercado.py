tipo_cliente= input("Que tipo de cliente es usted (VIP o Regular): " ) .lower ()
compra= float (input ("Monto de la compra: "))

cliente= 'regular'
cliente2 = 'vip'

#cliente vip

if tipo_cliente == 'vip' and compra >= 1000:
    print (f"Monto a pagar: RD$ {compra - (compra * 0.20):.2f} (Descuento del 20%)") 

elif tipo_cliente == cliente2 and compra < 1000:
    print (f"Monto a pagar: RD$ {compra - (compra * 0.10):.2f} (Descuento del 10%)")

#cliente regular

elif tipo_cliente == cliente and compra >= 1000:
    print (f"Monto a pagar: RD$ {compra - (compra * 0.05):.2f} (Descuento del 5%)") 

elif tipo_cliente == cliente and compra < 1000:
    print (f"Monto a pagar: RD$ {compra:.2f} (Sin descuentos)")

else:
    print ("Cliente no permitido.")
