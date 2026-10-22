class Insect:
    def __init__(self, name, legs, sound, age):
        self.name = name
        self.legs = legs
        self.sound = sound
        self.age = age

    def __str__(self):
        return f"Насекомое: {self.name}, Ног: {self.legs}, Возраст: {self.age} лет"

    def move(self):
        return f"{self.name} просто ползет."

    def make_sound(self):
        return f"{self.name} издает звук: {self.sound}"