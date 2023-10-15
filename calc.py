import time,os
#functions
def addition(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
#user input for function to use
options = int(input("1. Addtion \n2. Subtraction \n3. multiply \n4. divide \n:"))

os.system("clear")
#user input for variable
FirstNumber = float(input("Enter your first number: "))
SecondNumber = float(input("Enter your second number: "))

os.system("clear")

#conditions
if(options == 1):
    Result = addition(FirstNumber, SecondNumber)

elif(options == 2):
    Result = subtract(FirstNumber, SecondNumber)    

elif(options == 3):
    Result = multiply(FirstNumber, SecondNumber)

elif(options == 4):
    Result = divide(FirstNumber, SecondNumber)

else:
    print("choose correct option!!!")
    exit()    
#result
print("loading.")
time.sleep(0.3)
os.system("clear")
print("loading..")
time.sleep(0.3)
os.system("clear")
print("loading...")
time.sleep(0.3)
os.system("clear")
print(Result)