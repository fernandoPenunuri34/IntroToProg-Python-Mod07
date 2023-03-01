# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with exceptions and pickle in a class,
#              When the program starts, to calculate different metrics
# ChangeLog (Who,When,What):
# LLopez,2.25.2023,Created started script
# LLopez, 2.17.2023,Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle
import sys

class Calculator:
    # Constructor to initialize the object with one numbers
    def __init__(self, num1):
        self.num1 = num1

    # Method to add 2 numbers
    def mtstofeet(self):
        return self.num1 * 3.28084

    # Method to subtract 2 numbers
    def feedtomts(self):
        return self.num1 / 3.28084

    # Method to multiply 2 numbers
    def kgtolbs(self):
        return self.num1 * 2.2

    # Method to divide 2 numbers
    def lbstokg(self):
        # Check if dividing by zero
        return self.num1 / 2.2

    def cont(self):
        while True:
            stringContinue = input("\nDo you want to continue? (Y/N)")
            if stringContinue.lower() == "n":
                sys.exit()  # terminate the program if the user does not want to continue
            elif stringContinue.lower() != "y":
                print("Invalid input. Please enter Y or N.")
                continue  # continue to the next iteration if the user enters an invalid input
            else:
                main()

def main():
    try:
        print("\nOperation type:\n1) Meters to feets\n2) Feets to mts\n3) Kg to lbs\n4) Lbs to kg")
        # Ask the user to select an equation type
        string_eqtype = input("What would you want to do (type a number 1-4): ")
        # check if the input is valid
        if string_eqtype not in ['1', '2', '3', '4']:
            raise ValueError("Invalid equation type")


        if string_eqtype == "1":
            num2 = "feets"
            num3 = "mts"
        elif string_eqtype == "2":
            num2 = "mts"
            num3 = "feets"
        elif string_eqtype == "3":
            num2 = "lbs"
            num3 = "Kg"
        elif string_eqtype == "4":
            num2 = "Kg"
            num3 = "lbs"

        # ask the user to input 2 numbers
        num1 = float(input("Enter the value: "))

        # create a calculator object with the 2 numbers
        calculator = Calculator(num1)

        # map equation type strings to their corresponding method calls
        operations = {
            '1': calculator.mtstofeet,
            '2': calculator.feedtomts,
            '3': calculator.kgtolbs,
            '4': calculator.lbstokg
        }

        # perform the selected operation
        result = round(operations[string_eqtype](), 2)

        # Print the result of the operation
        print(f"\nResult: {result}" + " " + num2)

        try:
            # Save calculator object to file using pickle
            with open('calculator.pickle', 'wb') as f:
                pickle.dump(calculator, f)
        except IOError as e:
            print(f"Error occurred while saving data to file: {e}")
        except pickle.PickleError as e:
            print(f"Error occurred while pickling data: {e}")

        try:
            # Load calculator object from file using pickle
            with open('calculator.pickle', 'rb') as f:
                calculator = pickle.load(f)
        except IOError as e:
            print(f"Error occurred while reading data from file: {e}")
        except pickle.UnpicklingError as e:
            print(f"Error occurred while unpickling data: {e}")

        print("\nThis was calculated from:")
        print(f"Value: {calculator.num1}" + " " + num3)

        # ask the user if they want to continue or exit
        calculator.cont()

    # Catch and handle exceptions
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the main function if the script
if __name__ == '__main__':
    main()