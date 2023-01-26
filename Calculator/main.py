import sys
from calculator import Calculator


def main():
    calc = Calculator()
    n = "\n---------------------------------------------------"
    while True:
        try:
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
            print(calc.mode)

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
    main()
