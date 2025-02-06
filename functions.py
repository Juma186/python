# Built-in functions/standard library functions

y = max(70,45,60,78,38)
print("the maximum is ", y)

x = min(70,45,60,78,38,7)
print("the minimum is ", x)


# user defined functions
def name():
    print("Juma")

name() # calling a function

def product():
    x = 10
    y = 20
    print(x * y)

product()

# Parameter/Variable and Arguments/Variable
def add(a,b):
    print(a + b)

add(5,6)
add(9,5)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)


employee("Juma",'Male',"CEO","600000","39")
employee("Leslie",'Female',"Secretary","120000","30")
employee("Migel",'Male',"HR","300000","54")

# Write a program that displays details of 5 students
#Use a user-defined function with the help of parameter and arguments
#Fullname, age, coarse , gender

def student(fullname,gender,age,coarse,):
    print(fullname,gender,age,coarse)

student("James Collins","Male",20,"Engineering")
student("Kira Nicole","Female",24,"Electrician")
student("Mark Nairi","Male",25,"Medic")
student("Marcus Thea","Male",26,"Aviation")
student("Lis Jordyn","Female",28,"Psychology")