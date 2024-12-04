'''
TRABAJO INTEGRADOR: TICKETERA

ESTRUCTURA DEL PROGRAMA:

1) Menú Principal:

	Presentar las opciones: Alta de ticket, Leer ticket, y Salir.

	Controlar el flujo de acuerdo con la elección del usuario.
 
2) Alta de Ticket:

	Solicitar los datos: Nombre, Sector, Asunto, Problema.

	Generar un número de ticket aleatorio entre 1000 y 9999.

	Almacenar el ticket en un diccionario o estructura similar.

	Mostrar el ticket generado.

	Preguntar si se desea registrar otro ticket o regresar al menú principal.

3) Leer Ticket:

	Solicitar el número del ticket.

	Buscar el ticket en los datos almacenados.

	Mostrar el ticket correspondiente.

	Preguntar si se desea leer otro ticket o regresar al menú principal.

4) Salir:

	Confirmar la salida antes de cerrar el programa.

'''


import random

# Estructura para almacenar los tickets
tickets = {}

def menu_principal():
    """Despliega el menú principal y gestiona la navegación."""
    while True:
        print("\n--- Bienvenido al Sistema de Tickets ---")
        print("1. Generar un Nuevo Ticket")
        print("2. Leer un Ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            if confirmar_salida():
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Intente de nuevo.")

def alta_ticket():
    """Crea un nuevo ticket y lo almacena."""
    while True:
        print("\n--- Alta de Ticket ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")
        
        # Generar un número de ticket único
        numero_ticket = random.randint(1000, 9999)
        while numero_ticket in tickets:
            numero_ticket = random.randint(1000, 9999)
        
        # Almacenar el ticket
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }
        
        # Mostrar el ticket
        print("\n--- Ticket Generado ---")
        print(f"Número de Ticket: {numero_ticket}")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("\nPor favor, recuerde el número de su ticket.")
        
        # Preguntar si se desea crear otro ticket
        otro = input("\n¿Desea crear otro ticket? (s/n): ").strip().lower()
        if otro != "s":
            break

def leer_ticket():
    """Permite buscar y mostrar un ticket por su número."""
    while True:
        print("\n--- Leer Ticket ---")
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        # Buscar y mostrar el ticket
        ticket = tickets.get(numero_ticket)
        if ticket:
            print("\n--- Detalles del Ticket ---")
            print(f"Número de Ticket: {numero_ticket}")
            for clave, valor in ticket.items():
                print(f"{clave}: {valor}")
        else:
            print("\nEl número de ticket ingresado no existe.")
        
        # Preguntar si se desea leer otro ticket
        otro = input("\n¿Desea leer otro ticket? (s/n): ").strip().lower()
        if otro != "s":
            break

def confirmar_salida():
    """Confirma si el usuario desea salir del programa."""
    confirmacion = input("¿Está seguro de que desea salir? (s/n): ").strip().lower()
    return confirmacion == "s"

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
