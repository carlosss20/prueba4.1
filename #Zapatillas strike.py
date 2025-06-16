#Zapatillas strike
agenda = {}
codigo_secreto = "EstoyEnListaDeReserva"
pares_disp = 20
pares_reservados = 0 

def menu():
    print("1.- Reservar zapatillas ")
    print("2.- Buscar reservas  ")
    print("3.- Cancelar reserva ")
    print("4.- Salir ")

def reservar_zapatillas(): 
    global pares_disp, pares_reservados, agenda
    if pares_disp >= 1:
        while True: 
            print("-- Reservar zapatillas --")
            try:
                nombre = input("Nombre del comprador: ")

                if nombre.isalpha: 
                    break
                else:
                    print("Ingrese un nombre valido!")
                    
            except ValueError: 
                print("Ingrese un nombre valido!")
        if nombre in agenda:
            print("Reservas maximas realizadas. Cerrando aplicacion")
            exit()
        else:
            while True:
                secreto = input("Digite la palabra secreta para confirmar la reserva: ")
                if secreto == codigo_secreto:
                    print(f"Reserva realizada con exito para {nombre}")
                    pares_reservados = pares_reservados + 1
                    pares_disp=pares_disp - 1 
                    agenda[nombre] = {'stock': 1}
                    break
                else: 
                    print("Error: codigo secreto incorrecto. Reserva no realizada.")

    else:
        print("No quedan pares disponibles. Cerrando aplicacion ")
        exit()

def buscar():
    global pares_disp, pares_reservados, agenda
    if not agenda:
        print("No hay reservas registradas.")
    else: 
        busc = input("Nombre del comprador a buscar: ")
        if busc in agenda:
            datos = agenda[busc]
            
            print("-- RESERVA ENCONTRADA --")
            print(F"Nombre: {busc}")
            print(f"Pares reservados: {datos['stock']}")

            extra = input("¿Desea pagar adicional para VIP y reservar un par extra?(s/n): ")
            
            if extra.isalpha() and len(extra) == 1:
                if extra == "s": 
                
                    if datos['stock'] == 2:
                        print("Maximo de reservaciones realizadas!")
                    else:
                        print(f"Reserva actualizzada a VIP. Ahora {busc} tiene 2 pares reservados")

                        pares_reservados = pares_reservados + 1
                        pares_disp=pares_disp - 1 
                        datos['stock'] = 2
                else:
                    print("Manteniendo reserva actual")
        else:
            print("Persona no se encuentra registrada")

def cancelar(): 
    nom = input("Ingrese el nombre de la reserva que busca cancelar: ")
    if nom in agenda:
        
        datos = agenda[nom]
        print(f"La reserva de {nom} ha sido cancelada")
        pares_disp = pares_disp + 1
        pares_reservados = pares_reservados - 1
    else:
        print("No se encontro ninguna reserva con ese nombre") 

def cuerpo():
    
    while True:
        try:
            opc = int(input("Seleccione una opcion (1-4): "))

        except ValueError: 
            print("Ingrese una opcion valida!")
            continue

        if 1 <= opc <= 4:
            break 

        else: print("Ingrese una opcion valida!")

    if opc == 1: 
        reservar_zapatillas()
    if opc == 2: 
        buscar()
    if opc == 3: 
        cancelar()
    elif opc == 4: 
        print("Cerrando el programa")
        exit()

    else:
        print("Debe ingresar una opcion valida")

def principal():
    while True:
        menu()
        cuerpo()

principal()
