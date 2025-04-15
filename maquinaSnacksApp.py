from serviciosSnacks import serviciosSnacks


class maquinaSnacksApp:
    def __init__(self):
        self.serviciosSnacks = serviciosSnacks()
        self.productos = []

    # Método de maquina de snacks
    def maquinaSnack(self):
        salir = False
        print('*** Maquina de Snacks ***')
        self.serviciosSnacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            
            except Exception as e:
                print(f"Error: {e}")
                continue

    # Método de mostrar el menú
    def mostrar_menu(self):
        print(f''' Menu:
            1. Comprar Snacks
            2. Mostrar Ticket de compra
            3. Agregar Snack al Inventario
            4. Mostrar Inventario Snack
            5. Salir''')
        return int(input("Seleccione una opción: "))

    # Método que ejecura la opción seleccionada
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snacks()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.serviciosSnacks.mostrar_snacks()
        elif opcion == 5:
            return True
        else:
            print(f"Opción no válida {opcion}.")
        return False

    # Método para comprar snacks
    def comprar_snacks(self):
        id_snack = int(input("Ingrese el ID del snack que desea comprar: "))
        snacks = self.serviciosSnacks.get_snack()

        snack = next((snack for snack in snacks if snack.get_id_snack() == id_snack), None)

        if snack:
            self.productos.append(snack)
            print('Snack agregado al carrito {snack}')
        else:
            print(f"Snack con ID {id_snack} no encontrado.")

    # Método para mostrar el ticket de compra
    def mostrar_ticket(self):
        if not self.productos:
            print("No hay productos en el carrito.")
            return

        print("Ticket de compra:")
        total = 0
        for snack in self.productos:
            print(snack)
            total += snack.get_precio()

        print("----Ticket de Venta----")
        for producto in self.productos:
            print(f"Snack: {producto.get_nombre()}, Precio: {producto.get_precio()}")
        
        print(f"Total a pagar: {total:.2f}")
    
    # Método para snacks al inventario
    def agregar_snack(self):
        nombre = input("Ingrese el nombre del snack: ")
        precio = float(input("Ingrese el precio del snack: "))
        self.serviciosSnacks.agregar_snack(nombre, precio)
        print(f"Snack {nombre} agregado correctamente.")

# Programa principal

if __name__ == "__main__":
    app = maquinaSnacksApp()
    app.maquinaSnack()