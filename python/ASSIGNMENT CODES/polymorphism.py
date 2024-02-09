class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
obj_ind = India()
obj_usa = USA()
func(obj_ind)
func(obj_usa)





#Method Overloading:
class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Example usage for method overloading
math_ops = MathOperations()
result1 = math_ops.add(2, 3)
result2 = math_ops.add(2, 3, 4)

print("Result 1:", result1)
print("Result 2:", result2)



# Method Overriding:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]
# Call the speak method on each object
for animal in animals:
    print(animal.speak())