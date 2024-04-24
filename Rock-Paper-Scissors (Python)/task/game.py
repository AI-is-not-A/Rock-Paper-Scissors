import random


class RockPaperScissorsGame:
    def __init__(self, user, options=""):
        self.user = user
        if options == "":
            self.options = ["rock", "paper", "scissors"]
        else:
            self.options = list(map(lambda option: option.strip(), options.split(",")))
        self.user_option = None
        self.computer_option = None

    def first_option_wins(self):
        index_user = self.options.index(self.user_option)
        index_computer = self.options.index(self.computer_option)
        dif = (index_computer - 1 - index_user) % len(self.options)
        return dif >= (len(self.options) // 2)
    #asdf

    def play_round(self, user_option):
        if user_option not in self.options:
            raise Exception("Invalid input")
        self.user_option = user_option
        self.computer_option = random.choice(self.options)
        self.get_result()

    def get_result(self):
        if self.user_option == self.computer_option:
            print(f"There is a draw {self.user_option}")
            self.user.score += 50
        else:
            if self.first_option_wins():
                print(f"Well done. The computer chose {self.computer_option} and failed")
                self.user.score += 100
            else:
                print(f"Sorry, but the computer chose {self.computer_option}")


class User:
    user_scores = {}

    def __init__(self, name):
        self.name = name.strip()
        self.score = 0
        self.load_user_scores_from_file()
        self.get_user_score()
        print(f"Hello, {self.name}")

    def get_user_score(self):
        value = User.user_scores.get(self.name)
        if value is not None:
            self.score = int(value)

    @staticmethod
    def load_user_scores_from_file():
        with open("rating.txt", "r") as file:
            data = file.readlines()
            for line in data:
                values = line.split()
                User.user_scores[values[0]] = values[1]


rps_game = RockPaperScissorsGame(User(input("Enter your name: ").strip()), input().strip())

print("Okay, let's start.")

while True:
    user_input = input()

    if user_input == "!exit":
        break
    elif user_input == "!rating":
        print(f"Your rating: {rps_game.user.score}")
    else:
        try:
            rps_game.play_round(user_input.strip())
        except Exception as e:
            print(e)

print("Bye!")
