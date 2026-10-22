from insect import Insect

class Thelyphonus(Insect):
    def __init__(self, name, legs, sound, age, tail_length):
        # Передаем age в родительский класс
        super().__init__(name, legs, sound, age)
        self.tail_length = tail_length

    def move(self):
        return f"{self.name} (возраст {self.age} лет) бежит по земле, виляя хвостом длиной {self.tail_length} см."

    def make_sound(self):
        return f"{self.name} шипит и брызгает уксусом: {self.sound}"