from Snack import Snack

class serviciosSnacks():
    NOMBRE_ARCHIVO = "snacks.txt"
    
    def __init__(self):
        self.snacks = []

        #Revisar si el archivo existe y cargar los snacks iniciales
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as file:
                self.snacks = self.obtener_snacks()
                
        except FileNotFoundError:
            print(f"El archivo {self.NOMBRE_ARCHIVO} no existe. Se creará uno nuevo.")

            self.crear_archivo_snacks()
            self.cargar_snacks_iniciales()
            self.snacks = self.obtener_snacks()

        except Exception as e:
            print(f"Error al cargar los snacks: {e}")
        
        else:
            print("Snacks cargados correctamente.")
        
        finally:    
            print("Proceso de carga inicial de snacks, finalizado.")
    
    # Método para crear el archivo de snacks si no existe   
    def crear_archivo_snacks(self):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as file:
                file.write("")  # Crear un archivo vacío
                print(f"Se ha creado el archivo: {self.NOMBRE_ARCHIVO}")
        except Exception as e:
            print(f"Error al crear el archivo de snacks: {e}")










    
        # Cargar snacks al inicio
    
    # Método para cargar los snacks iniciales
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack("Chips", 1.50),
            Snack("Galletas", 2.00),
            Snack("Chocolate", 1.75)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks(snacks_iniciales)

        # Método para guardar snacks en el archivo
    
    # Método para guardar los snacks
    def guardar_snacks(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as file:
                for snack in snacks:
                    file.write(snack.escribirSnack() + '\n')      
            print(f"Snacks guardados correctamente en {self.NOMBRE_ARCHIVO}.")
        except Exception as e:
            print(f"Error al guardar los snacks: {e}")

    # Método para obtener todos los snacks
    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as file:
                for line in file:
                    id_snack, nombre, precio = line.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f"Error al obtener los snacks: {e}")
        finally:
            return snacks
            
        # Método para agregar un nuevo snack
    
    # Método para agregar snacks
    def agregar_snack(self, nombre="", precio=0.0):
        nuevo_snack = Snack(nombre, precio)
        self.snacks.append(nuevo_snack)
        self.guardar_snacks([nuevo_snack])
        print(f"Snack {nombre} agregado correctamente.")

    # Método para eliminar un snack por ID
    def eliminar_snack(self, id_snack):
        snack_eliminado = None
        for snack in self.snacks:
            if snack.get_id_snack() == id_snack:
                snack_eliminado = snack
                break

        if snack_eliminado:
            self.snacks.remove(snack_eliminado)
            self.actualizar_archivo_snacks()
            print(f"Snack {snack_eliminado.get_nombre()} eliminado correctamente.")
        else:
            print(f"Snack con ID {id_snack} no encontrado.")
        
    # Método para actualizar el archivo de snacks
    def actualizar_archivo_snacks(self):
        try:
            with open(self.NOMBRE_ARCHIVO, 'w') as file:
                for snack in self.snacks:
                    file.write(snack.escribirSnack() + '\n')
        except Exception as e:
            print(f"Error al actualizar el archivo de snacks: {e}")

    # Método para mostrar todos los snacks
    def mostrar_snacks(self):
        if not self.snacks:
            print("No hay snacks disponibles.")
        else:
            for snack in self.snacks:
                print(snack)

    # Metodo get snack
    def get_snack(self):
        return self.snacks

    # Método para buscar un snack por nombre
    def buscar_snack_por_nombre(self, nombre):
        snacks_encontrados = [snack for snack in self.snacks if snack.get_nombre().lower() == nombre.lower()]
        if snacks_encontrados:
            for snack in snacks_encontrados:
                print(snack)
        else:
            print(f"No se encontraron snacks con el nombre {nombre}.")

