"""
Validador de dinero y transporte

Tenemos que preguntar cuanto dinero tiene el usario

Tenemos que preguntar que tipo de transporte quiere el usario

Tenemos que mostrarle 3 opciones
1-Combi
2-Taxi
3-Uber

Dependendiendo de la opcione elgida validar el precio

Combi cuesta 10
Taxi cuesta 50
Uber cuesta 100

y validar si el dinero que tiene le alcanza para pagar el transporte

Si le alcanza mostrar un mensaje que diga

"Ok perfecto puedes viajer en <nombre del transporte>"

Si no le alcanza mostrarle un mensaje que diga

"Lo siento no te alcanza para <transporte elegido> pero te alcanza para
mostrar lo que le alcance >"

"""

combi = 1
taxi = 2
uber = 3

costo_combi = 10
costo_taxi = 50
costo_uber = 100

alcanza = False

#Solicitar Datos
dinero = float(input("¿Cuanto dinero tiene?\n"))
transporte_seleccionado = int(input("Seleccione Tipo de Transporte:\n1-Combi\n2-Taxi\n3-Uber\n"))

#Verifica Si Alcanza
if transporte_seleccionado == uber and dinero >= costo_uber: alcanza = True
if transporte_seleccionado == taxi and dinero >= costo_taxi: alcanza = True
if transporte_seleccionado == combi and dinero >= costo_combi: alcanza = True

if alcanza:
    if transporte_seleccionado == uber: 
        print("Ok perfecto puedes viajer en Uber")

    if transporte_seleccionado == taxi: 
        print("Ok perfecto puedes viajer en Taxi")

    if transporte_seleccionado == combi: 
        print("Ok perfecto puedes viajer en Combi")

#En caso de no alcanzar
else:
    if transporte_seleccionado == uber: 
        print("Lo siento no te alcanza para viajar en Uber")

    if transporte_seleccionado == taxi: 
        print("Lo siento no te alcanza para viajar en Taxi")

    if transporte_seleccionado == combi: 
        print("Lo siento no te alcanza para viajar en Combi")

    #BUSCA ALTERNATIVA
    if dinero >= costo_combi and dinero < costo_taxi: 
        print("Pero puedes viajar en Combi")
        
    if dinero >= costo_taxi and dinero < costo_uber: 
        print("Pero puedes viajar en Taxi")