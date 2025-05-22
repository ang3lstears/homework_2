print('nomer 1')
class Animal:
    def speak(self):
        return "издает звук"
class MixinSwim:
    def swim(self):
        return "плавает"
class MixinFly:
    def fly(self):
        return "летает"
class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"
class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"
animals = [Duck(), Penguin()]
for animal in animals:
    print(f"{animal.speak()} и он {animal.swim()} ", end="")
    if isinstance(animal, MixinFly):
        print(f"и {animal.fly()}.")
    else:
        print(".")
print('nomer 2')

class Writer:
    def write(self):
        return "пишет текст"
class Painter:
    def draw(self):
        return "рисует картину"
class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"
    def draw(self):
        return "выразительно рисует пейзаж"
creatives = [Writer(), Painter(), CreativePerson()]
for creative in creatives:
    if isinstance(creative, Writer):
        print(creative.write())
    if isinstance(creative, Painter):
        print(creative.draw())