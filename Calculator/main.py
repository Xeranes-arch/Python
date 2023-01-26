"""
Main of Calculator

Usage:
    main.py
    main.py set <m> <n1> <n2> <r>
"""
version = 1.0

import docopt
import sys
from calculator import Calculator


def main():
    calc = Calculator()

    if calc.mode != None:
        doc = True
    
    calc.mode = options['<m>']
    calc.n_1 = options['<n1>']
    calc.n_2 = options['<n2>']
    calc.round_to = options['<r>']
    n = "\n---------------------------------------------------"
    while True:
        try:
            if not doc:
                # Get user inputs
                calc.mode = check_q(input("You have the following Choices:"
                                        "\n1) Add \n2) Subtract \n3) Multiply \n4) Divide \n5) Set decimal place to round to \nq) Quit"
                                        "\nInput mode:"))
                if calc.mode == 5:
                    calc.round_to = int(
                        input("Input new decimal place to round to:"))
                    continue
                calc.n_1 = check_q(input("Input Number_1:"))
                calc.n_2 = check_q(input("Input Number_2:"))
            else:
                doc = False

            # Calc
            if calc.mode == 1:
                calc.addition()
            elif calc.mode == 2:
                calc.subtraction()
            elif calc.mode == 3:
                calc.multiplication()
            elif calc.mode == 4:
                try:
                    calc.division()
                except ZeroDivisionError:
                    print(
                        "Zero Division is nono bro." + n)
                    continue
            

            # Round and print
            calc.round()
            print("Result is: " + str(calc.res) + n)
            input("Press Enter to go again.")

        # Catch Errors
        except KeyboardInterrupt:
            print("\nAight boss. Shuting down.")
            sys.exit()
        except ValueError:
            print("That's probably not a number you gave me there." + n)


def check_q(input):
    """Checks if the player wishes to quit."""
    if input == "q":
        print("Quiting! Bye!")
        sys.exit()
    return input


if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    main()
