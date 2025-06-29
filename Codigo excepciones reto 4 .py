class Shape:
    def compute_area(self):
        # ✔ Forzar implementación en subclases
        raise NotImplementedError("Este método debe ser redefinido en la subclase.")
    
    def compute_perimeter(self):
        # ✔ Forzar implementación en subclases
        raise NotImplementedError("Este método debe ser redefinido en la subclase.")


class Rectangle(Shape):
    def __init__(self, width, height):
        # ✔ Validación: Las dimensiones deben ser mayores a cero
        if width <= 0 or height <= 0:
            raise ValueError("El ancho y alto deben ser mayores a cero.")
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        # ✔ Validación: El lado debe ser positivo
        if side <= 0:
            raise ValueError("El lado del cuadrado debe ser mayor a cero.")
        self.side = side

    def compute_area(self):
        return self.side ** 2

    def compute_perimeter(self):
        return 4 * self.side
