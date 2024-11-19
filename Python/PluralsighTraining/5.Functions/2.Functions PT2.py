def greeting(name):
    print("Hello", name)

name1 = input("Whats your name?:\n")
greeting(name1)

name2 = input("Whats your name:\n")
greeting(name2)


#New example?

def addition(a,b):
    return a + b

num1 = float(input("Enther yours first number:\n"))
num2 = float(input("Enter your second number:\n"))

result = addition(num1, num2)
print("The result is", result)