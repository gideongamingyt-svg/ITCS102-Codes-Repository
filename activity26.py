from activity25 import taga_triangle
from activity25 import box
from activity25 import sum
from activity25 import my_factorial


while True:
    print("MINI MENU")
    print("SELECT AN OPTION")
    print("1 = Triangle")
    print("2 - SUM")
    print("3 - Box")
    print("4 - Factorial")
    print("5 - EXIT")
    choose = int(input("Which option to go --->    "))

    if choose == 1:
        print("TAGA TRIANGLE")
        size = int(input("SIZE NG TRIANGLE --> "))
        taga_triangle(size)
        continue
    elif choose == 2:
        print("SIMPLE SUMMTION")
        num1 = int(input("number 1 --> "))
        num2 = int(input("number 2 --> "))
        PRINT(f"the sum of {num1} and {num2} is {sum(num1, num2)}")
        continue
    elif choose == 3:
        print("BOX")
        size = int(input("SIZE NG BOX --> "))
        box(size)
        continue
    elif choose == 4:
        print("FACTORIAL")
        num = int(input("INPUT ANY NUMBER --> "))
        print("The factorial of", num," is", my_factorial(num))
        continue
    elif choose == 5: 
        print("SYSTEM EXIT")
        break
    else:
        print("INVAILD CHOISE")
        continue