class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))

    def contact(self):
        print('My email and phone are %s, and %s' % (self.email, self.phone))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
sonny.contact()
jordan.greet(sonny)
jordan.contact()



