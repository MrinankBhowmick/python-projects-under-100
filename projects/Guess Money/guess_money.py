import random

"""
Guess Money is a simple fun math program.

In this, you have to think of any amount and it will return the total amount that is left in your pocket. 

Have Fun :)
"""


class Guess:
    def calculate_number(self) -> int:
        # Generate a random number between 1 and 1000
        return random.randint(1, 10000)

    def print_statement(self):
        # Calculate the additional money based on the random number
        add_money = self.calculate_number()

        # Print instructions and steps
        print("\nGuess Money : A simple fun math program.\n")
        print(
            "Rules : Do not enter any amount that you are thinking. The player just have to press enter and that's it and if you are weak in simple calculations then take a calculator and then play.\n"
        )
        input("Click enter to proceed\n")

        # Explaining steps
        input(
            "Think any amount of money you have in your pocket.\nEg : Let suppose you have 100 ₹ in your pocket.\n"
        )
        input(
            "Now, borrow the same amount of money from your friend.\nEg : Borrow 100 ₹ from your friend.\n"
        )
        input("Add both amount you have.\nEx : Your 100 + Friend 100 = 200 ₹.\n")
        input(
            f"Add {add_money} in the total amount.\nEg : Let the third amount be 50 ₹ so, add 50 ₹ in 200 ₹ and it become 250 ₹.\n"
        )
        input(
            "Spend the amount that you borrowed from your friend for buying something.\nEg : Spend 100 ₹ of your friend to purchase some cookies.\n"
        )
        input(
            "Now, from the rest of amount, Donate the amount that you have initially.\nEg : You have 100 ₹ initially so, donate 100 from left amount.\n"
        )
        print(f"You have {add_money / 2} ₹ left in your pocket.\n")


obj = Guess()
obj.print_statement()
