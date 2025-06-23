from math import sqrt
import numbers
from functools import total_ordering

# Erben tut die Klasse 2D nichts.
# Man kann auch die Dekorator Functions an Klassen übergeben
@total_ordering
class Vector2D:
    # die init methode returnt nie etwas, wenn eine Methode kein eigenen Statment hat dann wird None returnt
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:  # Es muss ein else Fall sein, sonst er immer triggern würde
            raise TypeError("You must pass in int or float values for x or y!")

    # Eine Exception rausschmeißen wenn x oder y keine Zahl ist


    # __call__ funktion ist dafür da, wenn wir ein Objekt später nochmal aufrufen wollen
    # d.h. auf das Objekt würden wir den runden Klammernpaar, intern die call methode einmal aufrufen
    def __call__(self, *args, **kwds) -> None:
        print("Calling the __call__ method!")

    def __repr__(self) -> str: # wenn wir ein Objekt printen wollen, returnt ein String
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str: # wenn wir ein Objekt zu einem String casten wollen, returnt ein String
        return f"({self.x}, {self.y})"

    def __abs__(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    # other_vector: da wir beim equal unsere eigene Objektinstanz mit einem anderen Objekt vergleichen wollen
    # deshalb kommt dieser Parameter neben dem self mit in eq methode rein
    # wo wir schauen ob x, y werte gleich sind
    # other_vector muss auch ein 2D Ojbekt sein, weil es sonst nicht gehen würde
    def __eq__(self, other_vector: object) -> bool:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You pass in Vector to the Instance!")
        return self.x == other_vector.x and self.y == other_vector.y # dann liegen alle Werte gleich vor

    def __lt__(self, other_vector: object) -> bool: # bei den Vector macht es eigentlich gar keinen Sinn
        # return self.x < other_vector.x and self.y < other_vector.y alternativ
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You pass in Vector to the Instance!")
        return (self.x, self.y) < (other_vector.x, other_vector.y)

    def __add__(self, other_vector: "Vector2D") -> "Vector2D":
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You pass in Vector to the Instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: "Vector2D") -> "Vector2D":
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You pass in Vector to the Instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    # mul: wir multiplizieren entweder mit einer Zahl oder mit einem Vector --> Abfragen
    def __mul__(self, other: "Vector2D" | float) -> float | "Vector2D":
        if isinstance(other, Vector2D):
            # Skalares Produkt (Dot Product)
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            # Skalare Multiplikation
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError("Multiplication only supports Vector2D or scalar (int/float) types.")

    def __truediv__(self, other: float) -> "Vector2D":
        if not isinstance(other, float):
            raise TypeError("You pass in Vector to the Instance!")
        return Vector2D(self.x / other, self.y / other)
# Erstellen wir ein Objekt davon:


v1 = Vector2D(1.0, 1.0)
v2 = Vector2D(-1.1, -1.1)

print(repr(v1))
print(str(v1))
print("")
print(repr(v2))
print(str(v2))
print(" ")
print(v1 + v2)
print(v1 * v2)
print(v1 / 5.0)
print(v2 / 3.0)
print(" ")
print(v1 < v2)
print(v1 > v2)
print(v1 == v2)
print(v1 != v2)
