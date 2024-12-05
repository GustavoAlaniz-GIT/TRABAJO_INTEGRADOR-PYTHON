'''
TRABAJO INTEGRADOR: TICKETERA

ESTRUCTURA DEL PROGRAMA:

Planificación:

1) Estructura del menú principal:

    Presentar las opciones al usuario.
    Navegar a las funciones correspondientes (alta_ticket, leer_ticket, salir).

2) Alta de ticket:

    Solicitar al usuario los datos necesarios.
    Generar un número de ticket aleatorio.
    Mostrar el ticket generado.
    Preguntar si se desea crear otro ticket.
    Almacenar los tickets en memoria y posteriormente en un archivo usando pickle.

3) Leer ticket:

    Solicitar el número de ticket.
    Cargar los datos almacenados con pickle.
    Mostrar el ticket correspondiente o un mensaje si no existe.
    Preguntar si desea buscar otro ticket.

4) Salir del programa:

    Confirmar la salida del programa.
    Guardar los datos en un archivo con pickle antes de salir.

5) Persistencia de datos:

    Al iniciar el programa, intentar cargar datos previos desde un archivo con pickle.
    Al cerrar, guardar los datos nuevamente en el archivo.

'''

import pickle
import random

# Archivo donde se almacenarán los tickets
TICKETS_FILE = "tickets.pkl"

# Cargar datos almacenados si existen
def cargar_tickets():
    try:
        with open(TICKETS_FILE, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

# Guardar datos en el archivo
def guardar_tickets(tickets):
    with open(TICKETS_FILE, "wb") as file:
        pickle.dump(tickets, file)

# Generar un número de ticket aleatorio
def generar_numero_ticket():
    return random.randint(1000, 9999)

# Función para dar de alta un ticket
def alta_ticket(tickets):
    while True:
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese el sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Describa el problema: ")
        
        numero_ticket = generar_numero_ticket()
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }
        
        print("\nTicket generado:")
        print(f"Ticket No: {numero_ticket}")
        print(f"Nombre: {nombre}, Sector: {sector}, Asunto: {asunto}, Problema: {problema}")
        print("\nPor favor, recuerde el número de su ticket.")
        
        continuar = input("\n¿Desea crear otro ticket? (s/n): ").strip().lower()
        if continuar != 's':
            break

# Función para leer un ticket
def leer_ticket(tickets):
    while True:
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            if numero_ticket in tickets:
                ticket = tickets[numero_ticket]
                print("\nInformación del ticket:")
                print(f"Ticket No: {numero_ticket}")
                for key, value in ticket.items():
                    print(f"{key}: {value}")
            else:
                print("\nEl ticket no existe.")

            continuar = input("\n¿Desea leer otro ticket? (s/n): ").strip().lower()
            if continuar != 's':
                break
        except ValueError:
            print("Por favor, ingrese un número de ticket válido.")

# Menú principal del programa
def menu_principal():
    tickets = cargar_tickets()
    while True:
        print("\n--- BIENVENIDO A LA TICKETERA DE ALANIZ ---")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            alta_ticket(tickets)
        elif opcion == '2':
            leer_ticket(tickets)
        elif opcion == '3':
            confirmar = input("¿Está seguro de que desea salir? (s/n): ").strip().lower()
            if confirmar == 's':
                guardar_tickets(tickets)
                print("¡Gracias por usar el sistema de tickets!")
                break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu_principal()
