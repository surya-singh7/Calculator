from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from pi_value import get_pi
from sin_func import sin_function
from cos_func import cos_function
from tan_func import tan_function
from degree_to_radian import degree_to_radian
from radian_to_degree import radian_to_degree
from square_root import square_root
from power import power
from logarithm import logarithm
from factorial_func import factorial_function
while True:
    print("  CALCULATOR")
    print("+      Addition")
    print("-      Subtraction")
    print("*      Multiplication")
    print("/      Division")
    print("pi     Pi Value")
    print("sin    Sin(x)")
    print("cos    Cos(x)")
    print("tan    Tan(x)")
    print("dtr    Degree To Radian")
    print("rtd    Radian To Degree")
    print("sqrt   Square Root")
    print("^      Power")
    print("log    Logarithm")
    print("fact   Factorial")
    print("exit   Exit Calculator")

    choice = input("\nEnter operation: ").lower()

    try:
        if choice == "+":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))
        elif choice == "-":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))
      
        elif choice == "*":

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            print("Result:", multiply(a, b))

        elif choice == "/":

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            print("Result:", divide(a, b))

        elif choice == "pi":

            print("Pi Value:", get_pi())

        elif choice == "sin":

            x = float(input("Enter angle in degrees: "))

            print("Result:", sin_function(x))

        elif choice == "cos":

            x = float(input("Enter angle in degrees: "))

            print("Result:", cos_function(x))

        elif choice == "tan":

            x = float(input("Enter angle in degrees: "))

            print("Result:", tan_function(x))

        elif choice == "dtr":

            deg = float(input("Enter degree value: "))

            print("Result:", degree_to_radian(deg))

        elif choice == "rtd":

            rad = float(input("Enter radian value: "))

            print("Result:", radian_to_degree(rad))

        elif choice == "sqrt":

            x = float(input("Enter number: "))

            print("Result:", square_root(x))

        elif choice == "^":

            a = float(input("Enter base number: "))
            b = float(input("Enter power: "))

            print("Result:", power(a, b))

        elif choice == "log":

            x = float(input("Enter number: "))

            print("Result:", logarithm(x))

        elif choice == "fact":

            x = float(input("Enter integer number: "))

            print("Result:", factorial_function(x))

        elif choice == "exit":

            print("Calculator Closed.")
            break

        else:

            print("Invalid Operation! Try Again.")

    except ValueError:

        print("Error! Invalid number entered.")

    except Exception as e:

        print("Unexpected Error:", e)