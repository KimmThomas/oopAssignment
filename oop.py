class Person:
    def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender


    def introduce(self):
        print(f"Hello, I am {self.name}, {self.age} years old and I am a {self.gender}.")

person1 = Person("Godfrey", 30, "Male") 

person1.introduce()