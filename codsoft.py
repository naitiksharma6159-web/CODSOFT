def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1 , n2):
    return n1 / n2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

operation = input("select operation from 1, 2, 3, 4 : ")


n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

if operation == "1":
    print(f"(n1) + (n2) = ", add(n1,n2))
elif operation == "2":
    print(f"(n1) + (n2) = ", substract(n1 , n2))
elif operation == "3":
    print(f"(n1) * (n2) = ", multiply(n1 ,n2))
elif operation == "4":
    print(f"n1) / (n2) = ", divide(n1 , n2))

else:
    print("invalid outout")


print("thank for using codsoft")