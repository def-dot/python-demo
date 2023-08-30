class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Cat(Pet):
    def speak(self):
        print(f"喵喵喵......{self.name}")


class Dog(Pet):
    def speak(self):
        print(f"汪汪汪......{self.name}")


def pattern_t():
    class PetFactory:
        def __init__(self, pet_class):
            self.pet_class = pet_class

        def create(self, name):
            return self.pet_class(name)


    obj = PetFactory(Cat).create("Kitty")
    obj.speak()
    obj = PetFactory(Dog).create("Wang")
    obj.speak()


if __name__ == "__main__":
    pattern_t()


