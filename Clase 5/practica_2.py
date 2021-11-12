
user = ""
password = ""

is_login = False
intentos_restantes = 3;

while  not is_login and intentos_restantes > 0: 
    user = input("usuario = ")
    password = input("contraseña = ")

    if user == 'admin' and password == '1234':
        is_login = True
        print("Bienvenido admin")

    else:
        intentos_restantes -=1
        print("Usuario o contraseña incorrectos por favor intenta de nuevo")
        if intentos_restantes>0:
             print("Intentos Restantes: ",intentos_restantes)

if not is_login:
    print("cantidad de intentos excedida")