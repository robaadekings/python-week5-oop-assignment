#Activity 1: Superhero Class with Inheritance 
class Superhero:
    def __init__(self, name: str, power: str, secret_identity: str):
        self.name = name
        self.power = power
        self.secret_identity = secret_identity
        self.health = 100

    def use_power(self):
        print(f"{self.name} uses {self.power}! ⚡")

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! ❤️‍🩹 Health: {self.health}")

    def __str__(self):
        return f"Superhero: {self.name} | Power: {self.power} | Secret Identity: {self.secret_identity}"


# Inheritance: A TechHero is a Superhero with additional abilities
class TechHero(Superhero):
    def __init__(self, name: str, power: str, secret_identity: str, gadget: str):
        super().__init__(name, power, secret_identity)
        self.gadget = gadget

    def use_gadget(self):
        print(f"{self.name} activates {self.gadget}! 🤖")

    def use_power(self):  # Overriding parent method
        print(f"{self.name} uses advanced tech: {self.power}! 🚀")


#Activity 2: Polymorphism with Vehicles
class Vehicle:
    def __init__(self, name: str):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road! �")


class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky! ✈️")


class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water! ⛵")


# Example Usage
if __name__ == "__main__":
    vehicles = [
        Car("Tesla"),
        Plane("Boeing 747"),
        Boat("Titanic")
    ]

    for vehicle in vehicles:
        vehicle.move()  # Polymorphism: Same method, different behavior