#ingresar Edad
edad = int(input("Ingrese su edad\n"))


etapa = ""
#Niñez
if edad >= 5 and edad <=13: etapa = "Niñez"
#Adolescencia
elif edad >= 14 and edad <=17: etapa = "Adolescencia"
#Adultos Jovenes
elif edad >= 18 and edad <=35: etapa = "Adultos Jovenes"
#Adultos
elif edad >= 36 and edad <=64: etapa = "Adultos"
#Tercera Edad
elif edad >= 65: etapa = "Tercera Edad"

#resultado
print("usted se encuentra en la etapa de: ",etapa);
