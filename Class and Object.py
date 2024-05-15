# class Person():
#     "This is a person class"
#     name = "John"
#     age = 20
#
#
#     def say_hi(self):
#         print("Hi!")
#
# print(Person.age)
# print(Person.name)
#
# print(Person.say_hi)
#
# print(Person.__doc__)
#
# class Cars:
#     def __init__(self,brand):
#         self.brand = brand
#
#     def brand_name(self):
#         print("This is a ",self.brand,"car")
#
# c1 = Cars('BMW')
# c1.brand_name()

# # Class Inheritance
# class Person:
#     def __init__(self,f_name,l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def getname(self):
#         print(self.f_name,self.l_name)
#
#     def isStudent(self):
#         return False
#
# p1 = Person("Leo", "Messi")
# print(p1.getname(),p1.isStudent())
#
# class Student(Person):
#     def isStudent(self):
#         return True
#
# p2 = Student("Virat ","Kohli")
# print(p2.getname(),p2.isStudent())




