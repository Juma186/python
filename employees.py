class Employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position)

employee1 = Employee("Julian","CEO",500000)
print(employee1.name,employee1.position,employee1.salary)

employee2 = Employee("Julie","Managing Director",250000)
print(employee2.name,employee2.position,employee2.salary)\
employee3 = Employee("Kylie","HR",105000)
employee4 = Employee("Francis","Director",250000)
