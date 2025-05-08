# Escibe esta linea de codigo:
print("Bienvenido al Entrenamiento con Python, vamos a disfrutar al maximo esta sesión")

"""
Descuento en una compra:
Si compras mas de $1000, obtienes un descuento del 20%
Pide el monto de la compra y muestra el precio Final
"""

# Pedir datos por teclado al usuario in entero float decimal str cadena de caracteres bool boolenao

compra = float(input("Digite el valor de la compra:"))

# Si compras mas de $1000, obtienes un descuento de 20%
# Siempre que la salida tenga mas de un camino de resolución, debo implementar condicionales

# operadores conbinados 
# operadores de asignación *, operadores aritmeticos +-/*. operadores logicos and y, or o, not,
# operadores de comparación ==, !=, >,<,>=,>=

if compra > 1000:
    descuento = compra * 0.2
    # compre * compra - descuento # operador de asignación
    compra -= descuento # operador de asignación compuesto
    print (f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")