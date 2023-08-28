def  descuento(monto):
    result= monto*0.05
    print ("Su total sin descuento es de:",monto)
    print("El precio del producto con un 5% de descuento es:",monto-result)
 

monto = float(input("Ingrese el monto de compra:"))
descuento(monto)