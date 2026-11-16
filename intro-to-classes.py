#classes are like combining features from a dictionary with functions that can get the object interactivity
#what is a class?  A class is a blueprint for an object(dict) that contains some data (attributes/fields/properties) and functions(methods)

#functions and methods are pretty much the same thing. Methods need an object to act upon or are part of a class.
#functions do not need a class to be called
#methods use dot notation ( . ) to be called.. object.method_name()

#classes creates instance when called upon.  Instances are like spawns or copies of class structures.  They are concrete manifestation of a class. It allows us to take a blueprint/class and make an actual object out of it

#this of classes like a hous, and then using the blueprints to build that house.  The finished house would be the instance

#instance/objects that belong to a class usually represent bundled data that defines what an object is or represents something in the real world

#to us a class we define it much like we define a function, but use the keyword class

#example - person with name and age...we will use what we call class variables first

class Person:
    #attributes/fields/properties
    name = "Zach"
    age = 41

#right nnow this is not a very useful class but we will make it more useful in another file

#now we need to create an instance of the class...when we do this it will have the data of name and age and will equal Zach and 41
#create an instance  instancename = classname()
instance1 = Person()

#access the properties/variables of a class.  we do this with dot notation
print(instance1.name)
print(instance1.age)

#instances maintain their own state...which means that if we create instance2 and change its properties, it will not affect instance1
instance2 = Person()

#we can change properties by saying instance_name.property = value
instance2.name = "Aly"
instance2.age = 32

print(instance2.name)
print(instance2.age)

print(instance1.name)
print(instance1.age)

