import random


class NumberGuessingGame:
    def __init__(self):
        """
        Define the range
        """
        self.LOWER = 1
        self.HIGHER = 100
        self.is_running = True
        self.MAX_CHANCES = 10

    def get_random_number(self):
        """
        Method to generate the random number
        :return:
        """
        return random.randint(self.LOWER, self.HIGHER)

    def logic(self, userNumber, random_num, chances):
        if userNumber == random_num:
            print(f"Yeah ! You got is in {chances + 1} step{'s' if chances > 1 else ''}!")
            self.is_running = False
        elif userNumber < random_num:
            print("The number that you've entered is less than the random number...")
        elif type(userNumber) != int:
            print("Please enter a integer number")
            userNumber = self.ask_number_user()
            self.logic(userNumber, random_num, chances)
        else:
            print("The number that you've entered is greater than the random number...")
        chances += 1

    def ask_number_user(self):
        return int(input("Enter the guessed number : "))

    def start(self):
        """
        Method to start the game
        :return:
        """
        random_num = self.get_random_number()

        print(f"The random number was been generated from {self.LOWER} to {self.HIGHER}")

        self.is_running = True
        chances = 0
        while self.is_running:
            try:
                while chances < self.MAX_CHANCES:
                    userNumber = self.ask_number_user()
                    self.logic(userNumber, random_num, chances)
                    chances += 1
                else:
                    print(f"... Phew ! You lost the game. You are out of chances")
            except Exception as e:
                print(f"An error was raised : {e}\nExiting")
                break
