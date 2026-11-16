#classes can represent real world objects and behavior that can be modified or changed
#if we want properties to be blank until we create an instance of a class we can use instance variables
#instance variables can be set or changed upon the creation of an object or instance
#class variables - pre-set values that come with every instance, but they can be still be changed later

#create a class called dog.  Dog will have a few properties - name, age, and animal
#dog will always have the class variable of animal = 'dog'
#but every dog will have a different name and age when they are created.  name and age are our instance variables


class Dog:
    #class variable
    #anytime we create a new dog instance animal will always = 'dog'
    animal = "dog"

    #instance variables are used in arguments/parameters when creating an instance in order to set properties upon creation
    #constructor - initializes instance variables with some data that the user or other parts of the program give it.  It is null until set

    #constructors are just special built-in functions/methods in a class
    #they use some special keywords like self to create instance variables

    #self - an INDIVIDUAL instance value or data (its own internal state)
    # __init__ - constructor keyword in python

    #constructor...it is a function/method so we use the def keyword like making a normal function
    def __init__(self,name,age):
        #define how we will set the values on creation
        #instance creation will look like dog1 = Dog(name,age)
        self.name = name
        self.age = age

    #we can make other functions/methods that all dogs can use..this is the other advantage of a class..grouping by behavior
    #all dogs bark...so lets make a bark method/function
    def bark(self):
        print("WOOOOOFFFF")


#create a dog instance.. We need to give it two arguments for name and age
dog1 = Dog("Braxton",10)
print(dog1.name)
print(dog1.age)
print(dog1.animal)
#to call a function with an instance we use the dot notation and then function_name()
dog1.bark()

print("************************")

#this is the power of classes, I can now create another dog with a different name and age but with the same animal variables
dog2 = Dog("Zilla", 3)
print(dog2.name)
print(dog2.age)
print(dog2.animal)
dog2.bark()