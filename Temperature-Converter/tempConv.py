import sys

# Convert Fahrenheit to Celsius
def F_to_C():
    input_F = input("Enter Fahrenheit value: ")
    C_Conv = (float(input_F)-32.0)*(5/9)
    C_Out = str(C_Conv) + '°C'
    print(C_Out)

# Convert Celsius to Fahrenheit
def C_to_F():
    input_C = input("Enter Celsius value: ")
    F_Conv = (float(input_C)*(9/5))+32.0
    F_Out = str(F_Conv) + "°F"
    print(F_Out)

# Execute the program
def start():
    choice = input("Enter F for Fahrenheit or C for Celsius: ")
    if choice == "F" or choice == "f":
        F_to_C()
    elif choice == "C" or choice == "c":
        C_to_F()
    else:
        sys.exit() # End program if choice is invalid

start()