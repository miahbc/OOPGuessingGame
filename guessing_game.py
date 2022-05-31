class GuessingGame():

    def __init__(self, answer=10, user_guess):
        self.answer = answer
        self.user_guess = user_guess
        
    def guess(self):
        if self.user_guess == self.answer:
            return "Correct!"
        elif self.user_guess > self.answer:
            return "high!"
        else: return "low!"
        
    
    def solved(self):
        self.answer = self.guess()
        if self.guess() == self.answer:
            return f"Your last guess {self.user_guess} was {self.answer}."
        else:
            return f"Your last guess {self.user_guess} was {self.answer}."

game = GuessingGame(2)
print(game(2))