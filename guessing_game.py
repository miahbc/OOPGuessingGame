class GuessingGame():

    def __init__(self, answer):
        self.answer = int(answer)
        # print(self.answer)
    
    def guess(self, user_guess):
        self.user_guess = user_guess
        # list = []
        # list.append(self.user_guess)
        if self.user_guess == self.answer:
            return "Correct!"
        elif self.user_guess > self.answer:
            return "high!"
        else: return "low!"

        
    
    def solved(self):
        # self.user_guess = user_guess
        print(list)
        print(self.user_guess, self.answer)
        if self.user_guess == self.answer:
            # return 'True'
            return f"Your last guess {self.user_guess} was {self.guess(self.user_guess)}"
        else:
            # return "False"
            return f"Your last guess {self.user_guess} was {self.guess(self.user_guess)}"



game = GuessingGame(2)
print(game.guess(1))
print(game.solved())