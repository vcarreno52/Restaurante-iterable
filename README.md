# Restaurante-iterable
#  Restaurante con clase iterable
Este repositorio contiene la implementación de un sistema de menús con clases en Python. Se extiende el código del Reto 3 agregando una nueva clase iterable para manejar pedidos.

## Reto #7
El reto consiste en ampliar la implementación de un sistema de menús utilizando programación orientada a objetos en Python. Se deben definir diversas clases que representen diferentes tipos de menús, cada una con atributos y reglas específicas para calcular el precio total. Además, se debe implementar una nueva clase iterable que permita recorrer los elementos de un pedido, facilitando el acceso a cada ítem y sus atributos mediante un bucle.

        class MenuIterable:
    def __init__(self):
        self.menus = []
    
    def add_menu(self, menu):
        self.menus.append(menu)
    
    def __iter__(self):
        return iter(self.menus)
    
    def total_price(self):
        return sum(menu.total_price() for menu in self.menus)
