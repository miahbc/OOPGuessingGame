class GuessingGame():

    def __init__(self, answer, user_guess):
        self.answer = answer
        self.user_guess = user_guess
        
    def guess(self):
        if self.user_guess == self.answer:
            return "Correct!"
        elif self.user_guess > self.answer:
            return "high!"
        else: return "low!"
        
    
    def solved(self):
        if self.guess() == self.answer:
            print(f"Your last guess {self.user_guess} was {self.guess()}.")
        else: print(f"Your last guess {self.user_guess} was {self.guess()}.")

game = GuessingGame(10)
print(game.guess(2))