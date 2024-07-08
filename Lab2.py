#While loops
#While loops are used to repeat a block of code while a certain condition is true.
#The syntax of a while loop is as follows:
i=0
while i<5:
    print(i)
    i+=1
#Iterating through list
print("LIST")
myList=["a","b","c","d"]
i=0
while i<len(myList):
    print(myList[i])
    i+=1

#for loop
print("FOR LOOP")
i=0
for i in range(5):
    print(i)
print("List")
for i in myList:
    print(i)
print("CONTINUE STATEMENT")
for i in myList:
    if i=="b":
        continue
    print(i)
print("Break STATEMENT")
for i in myList:
    if i=="c":
        break
    print(i)
print("FUNCTIONS")
#Functions 
def myFunction(a,b): #a and b are parameters
    print(a+b)

myFunction(10,4)
def printfun(country="PAKISTAN"): #Pakistan is default parameter
    print(country)

printfun()  #When called without parameter default parameter is used
printfun("Palestine")  # Default Parameter can be changed by passing a parameter

def listfun(myList):
    for i in myList:
        print(i)
        
listfun(myList)
def returnfun(a,b):
    return a*b

a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
print(returnfun(a,b)) #return function returns the value of the function
print(f"{a} * {b} = {returnfun(a,b)}") #format using f and placeholders{}

#CLasses
print("Classes ")
class myclass:
    x=5

obj1=myclass
print(obj1.x)

#The above class is just a simple class syntax
##init functions
class Cars:
    def __init__(self,brand,model,color): # self parameter represents the instance of object created
        self.brand=brand
        self.model=model
        self.color=color
    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nColor {self.color}")
        

obj1=Cars("Toyota","2023","Black")
obj1.display()
