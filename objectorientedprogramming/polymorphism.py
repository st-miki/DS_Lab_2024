class Animal:
    def color(self):
        pass

    def size(self):
        pass

    def eats(self):
        pass


class Deer(Animal):
    def color(self):
        print("The deer is black.")

    def size(self):
        print("The deer is medium-sized.")

    def eats(self):
        print("The deer eats grass.")


class Bear(Animal):
    def color(self):
        print("The bear is brown.")

    def size(self):
        print("The bear is large.")

    def eats(self):
        print("The bear eats fish.")


# Polymorphism in action
def describe_animal(animal):
    animal.color()
    animal.size()
    animal.eats()


# Create objects
deer = Deer()
bear = Bear()

# Use polymorphism
print("Describing the deer:")
describe_animal(deer)

print("\nDescribing the bear:")
describe_animal(bear)
