from insect import Insect

class Shrimp(Insect):
    def __init__(self, name, legs, sound, age, color):
        # Передаем age в родительский класс
        super().__init__(name, legs, sound, age)
        self.color = color

    def move(self):
        return f"{self.name} цвета {self.color} (возраст {self.age} лет) плывет задом наперед."

    def make_sound(self):
        return f"{self.name} щелкает клешнями: {self.sound}"