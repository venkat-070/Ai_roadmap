class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hi, I am "+self.name+" and I am "+str(self.age)+" years old.")
    def is_adult(self):
        if self.age >=18:
            print(self.name +" is an adult.")
        else:
            print(self.name+" is not an adult.")
    def birthday(self):
        self.age += 1
        print("Happy Birthday! "+self.name+" you are "+str(self.age)+" years old.")
    def __str__(self):
        return "Name: "+self.name+", Age: "+str(self.age)

person1 = Person("Ravi",22)
person2 = Person("Karthik",13)
print(person1)
print(person2)