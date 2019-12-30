## Classes & String Formatting

#def main():
    #print("Before MyClass")

# class MyClass:
#     variable = "temp"

#     def f1(self):
#         print("Message inside {0} {1} class".format("my","first"))


#myobject1 = MyClass()
# print(myobject1.variable)
#print(myobject1.f1)

# if __name__ == '__main__':
#     myobject1 = MyClass()
#     print(myobject1.f1)
#     print("After class assignment")



## Constructor Method 
## __init__ - is the method initiated whenever a class object is created
## self is the parameter that the methods have a way of referring to object attributes
# Code Reference - https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

class Shark:
    def __init__(self,name):
        self.name = name 
    
    def swim(self):
        print(self.name + "is swimming")

def main():
    sammy = Shark("Sammy")
    sammy.swim()

if __name__ == "__main__":
    main()
