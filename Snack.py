class Snack:
    # Atributo de clase
    __contador_snack = 0  # Atributo privado de clase

    # Constructor
    def __init__(self, nombre='', precio=0.0):
        Snack.__contador_snack += 1
        self.__id_snack = Snack.__contador_snack  # Atributo privado
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado

    def __str__(self):
        return f"Snack(id: {self.__id_snack}, nombre: {self.__nombre}, precio: {self.__precio})"

    def escribirSnack(self):
        return f"{self.__id_snack},{self.__nombre},{self.__precio}"

    # Métodos para acceder a los atributos privados (getters)
    def get_id_snack(self):
        return self.__id_snack

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    # Métodos para modificar los atributos privados (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio >= 0.0:  # Validación simple
            self.__precio = precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    # Método de clase para acceder al contador
    @classmethod
    def get_contador_snack(cls):
        return cls.__contador_snack
