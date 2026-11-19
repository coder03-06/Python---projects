#List 
colours=["green" , "red" ,"blue","black"]
colours.insert(1,"yellow")
colours[2]="white"
colours.remove("blue")
print(colours)
print(colours[-1])

#Tuple
contact =  ("John" ,"9898989898", 33 , "Trainer")
name, phone, age, designation = contact
print(name)
print(phone)
print(age)
print(designation)

#set
fruits = {"apple" , "banana" , "mango" , "apple"}
fruits.add("orange")
fruits.discard("apple")
print(fruits)


#Dictionary 
student = {
    "name": "John",
    "dept": "CSE",
    "age": 33,
    "marks": "90"
}

print(student["name"])
print(student.get("age"))
student["city"] = "Bangalore"
student["marks"] = "95"
student.pop("age")

print(student)

for key,value in student.items():
    print(key, ":", value)

print(student.keys())
print(student.values())

marks = [90, 80, 70, 60, 50]

#indexing
print(marks[0])
print(marks[-1])
print(marks[-2])

#slicing
print(marks[1:4])
print(marks[:3])
print(marks[2:])
print(marks[::2])
print(marks[::-1])


#function
def greet():
    print("Welcome")
greet()

def greeting(message):
    print(message)
greeting("Welcome")

def calc(a,b):
    return a+b, a*b
total,product = calc(10,20)
print(total)
print(product)

#default argument
def greeting(name="Guest"):
    print("Welcome", name)
greeting("John")
greeting()

#keyword argument
def student_info(name, age, city):
    print(name, age, city)
student_info(age=20, name="John", city="Bangalore")


#Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, designation):
        super().__init__(name, age)
        self.designation = designation

    def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Designation:", self.designation)

e1 = Employee("John", 25 , "Developer")
e2 = Employee("Ann" , 27 , "Software Tester")
e1.display()
e2.display()



    