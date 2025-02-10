class Person:
    def __init__(self, name, age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name, "is speaking")

person1 = Person("John",23,"Pilot")
print(person1.name)
person1.speak()

person2 = Person("Kira",33,"Teacher")
print(person2.name)
person2.speak()


