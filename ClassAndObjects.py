

class Character:
    def __init__(self, name, health, damage, speed) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    def double_speed(self):
        print("Double Speed!" , "\n", self.name)
        self.speed *= 2

    def double_health(self):
        print("Double Health!", "\n", self.name)
        self.health *= 2

    def double_damage(self):
        print("Double Damage!", "\n", self.name)
        self.damage *= 2

    def ultra_buff(self):
        print("Double EVERYTHING!!!", "\n", self.name)
        self.speed *= 2
        self.health *= 2
        self.damage *= 2

    def print_char_details(self):
        print("Name:", self.name)
        print("Health:", {self.health})
        print("Damage:", {self.damage})
        print("Speed:", {self.speed})
        print("\n")

if __name__ == "__main__":
    warrior = Character("Warrior", 100 ,50 ,10)
    ninja = Character("ninja", 80, 40, 40)
    demon = Character("demon", 50 ,20 ,10)
    imp = Character("imp", 20, 10, 10)
    imp2 = Character("imp2", 40, 20, 15)


    warrior.print_char_details()
    ninja.print_char_details()
    demon.print_char_details()
    imp.print_char_details()

    warrior.double_speed()
    ninja.double_health()

    warrior.print_char_details()
    ninja.print_char_details()

    warrior.ultra_buff()

    warrior.print_char_details()
    ninja.print_char_details()
#test
