class Cat:
    species = 'mammal'
    legs = 4
    fur = 'long hair'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '%s is %d years old' % (self.name, self.age)

    # Instance Method

    def eat(self, cups_of_food):
        self.cups_of_food = cups_of_food
        return "%s ate %d cups of food" % (self.name, self.caps_of_food)

ash = Cat('Ash', 4)

print(ash.eat(1))


