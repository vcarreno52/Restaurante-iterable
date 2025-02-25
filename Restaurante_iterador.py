class MenuItem:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self._precio = precio
        self.cantidad = cantidad

    def get_precio(self):
        return self._precio

    def total_price(self):
        return self.get_precio() * self.cantidad


class menu_infantil(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, figurita: str):
        super().__init__(nombre, precio, cantidad)
        self.figurita = figurita

    def total_price(self):
        if self.figurita == "dinosaurio":
            return super().total_price() + 2000
        else:
            return super().total_price()


class menu_adultos(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, bebida: str, tamaño: str):
        super().__init__(nombre, precio, cantidad)
        self.bebida = bebida
        self.tamaño = tamaño

    def total_price(self):
        if self.tamaño == "Grande":
            return super().total_price() * 1.5
        else:
            return super().total_price()


class menu_ancianos(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, bebida: str):
        super().__init__(nombre, precio, cantidad)
        self.bebida = bebida


class menu_ansiosos(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, ansiolítico: int):
        super().__init__(nombre, precio, cantidad)
        self.ansiolítico = ansiolítico

    def total_price(self):
        if self.ansiolítico < 1:
            return super().total_price()
        elif self.ansiolítico == 1:
            return super().total_price() * 1.5
        else:
            return super().total_price()


class menu_alcólicos(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, alcohol: str, tipo: str):
        super().__init__(nombre, precio, cantidad)
        self.alcohol = alcohol
        self.tipo = tipo

    def total_price(self):
        if self.tipo == "cóctel":
            return super().total_price() + 5000
        elif self.cantidad > 1:
            return super().total_price() + 2000
        else:
            return super().total_price()


class menu_vegetariano(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, verduras: str):
        super().__init__(nombre, precio, cantidad)
        self.verduras = verduras


class menu_para_compartir(MenuItem):
    def __init__(self, nombre: str, precio: float, cantidad: int, platillo: str):
        super().__init__(nombre, precio, cantidad)
        self.platillo = platillo

    def total_price(self):
        if self.cantidad > 1:
            return super().total_price() * 0.9
        else:
            return super().total_price()


def precio_total(*menus):
    total = 0
    for menu in menus:
        total += menu.total_price()
    return total


Mi_menu_ansioso = menu_ansiosos("Setralanina", 12000, 1, 3)
total_ansioso = Mi_menu_ansioso.total_price()
print(total_ansioso)

Mi_menu_infantil = menu_infantil("Menu sorpresa", 10000, 1, "dinosaurio")
total_infantil = Mi_menu_infantil.total_price()
print(total_infantil)

Mi_menu_compartir = menu_para_compartir("Plato grande", 20000, 2, "Pizza")
total_compartir = Mi_menu_compartir.total_price()
print(total_compartir)

Mi_menu_alcoholico = menu_alcólicos("Margarita", 12000, 1, "Tequila", "cóctel")
total_alcoholico = Mi_menu_alcoholico.total_price()
print(total_alcoholico)

Mi_menu_alcoholico_segunda_bebida = menu_alcólicos("Margarita", 12000, 2, "Tequila", "bebida")
total_alcoholico_segunda = Mi_menu_alcoholico_segunda_bebida.total_price()
print(total_alcoholico_segunda)

total_final = precio_total(Mi_menu_ansioso, Mi_menu_infantil, Mi_menu_compartir, Mi_menu_alcoholico_segunda_bebida)
print(f"El precio total es: {total_final}")

class MenuIterable:
    def __init__(self):
        self.menus = []
    
    def add_menu(self, menu):
        self.menus.append(menu)
    
    def __iter__(self):
        return iter(self.menus)
    
    def total_price(self):
        return sum(menu.total_price() for menu in self.menus)

# Creación de la instancia iterable
todos_los_menus = MenuIterable()

todos_los_menus.add_menu(menu_ansiosos("Setralanina", 12000, 1, 3))
todos_los_menus.add_menu(menu_infantil("Menu sorpresa", 10000, 1, "dinosaurio"))
todos_los_menus.add_menu(menu_para_compartir("Plato grande", 20000, 2, "Pizza"))
todos_los_menus.add_menu(menu_alcólicos("Margarita", 12000, 1, "Tequila", "cóctel"))

total_final = todos_los_menus.total_price()
print(f"El precio total es: {total_final}")

# Iterando sobre el objeto iterable
for menu in todos_los_menus:
    print(f"{menu.nombre}: {menu.total_price()}")