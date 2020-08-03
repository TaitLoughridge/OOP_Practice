class Car:
    whells = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return 'The %s %s is form %d' % (self.make, self.model, self.year)

toyota = Car('Toyota', 'Camry', 1992)
honda = Car('Honda', 'Civic', 2019)

print(toyota)
print(honda)