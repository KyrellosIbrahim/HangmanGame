"""
Hangman Game
Author: Kyrellos Ibrahim,
Date: 07/17/23
Description: A classic game of Hangman where one player inputs a word
and the second player tries to guess it. The guessing player has a limited
number of attempts. The game ends when the word is correctly guessed or the
guessing player has no more attempts.
"""
class Hangman:
    def __init__(self, attempts=6):
        """
        Initialize the game parameters.
        :param attempts: number of guesses allowed for player 2.
        """
        self.theWord = ""
        self.wordArr = []
        self.attempts = attempts
        self.guessedLetters = []
        self.hiddenWord = []
        self.wordLength = 0

    def getWord(self):
        """
        Get the word that player 2 has to guess from player 1.
        """
        while True:
            self.theWord = input("Player 1: please enter a word: ").lower() #lower cases the word to guess.
            if self.theWord.isalpha():
                break
            else:
                print("Please enter a valid word without numbers or special characters.")

        self.wordArr = list(self.theWord)
        self.hiddenWord = ['_'] * len(self.theWord) #empty spots for the amount of letters in the word.

    def displayState(self):
        """
        Display the current state of the word and the incorrect guesses.
        """
        print(" ".join(self.hiddenWord))
        print("Guessed Letters: ", " ".join(self.guessedLetters))
        print("Attempts left:", self.attempts)

    def guessLetter(self):
        """
        Allow player 2 to guess a letter in the word.
        """
        while True:
            guess = input("Player 2: please guess a letter: ").lower() #takes the letter and lowercases it.
            if len(guess) == 1 and guess.isalpha() and guess not in self.guessedLetters: #nothing wrong with the guess.
                break
            elif guess in self.guessedLetters: #this letter was already guessed.
                print("You've already guessed that letter. Please enter a new letter.")
            else: #a special character was entered.
                print("Please enter a valid letter.")
        if guess in self.wordArr: #checks if the guess is a part of the word
            n = [i for i, letter in enumerate(self.wordArr) if letter == guess] #checks every occurrence of the letter.
            for i in n:
                self.hiddenWord[i] = guess
        else: #handles incorrect guesses.
            self.guessedLetters.append(guess)
            self.attempts -= 1
    def gameOver(self):
        """
        Check if the game is over due to player 2 guessing the word or running out of guesses.
        :return: True if the game is over, false otherwise.
        """
        return self.attempts == 0 or self.hiddenWord == self.wordArr
    def displayResult(self):
        """
        Display the final result of the game and reveal the word.
        """
        if self.attempts == 0:
            print("Player 1 Won!\n The word was: " + self.theWord + ".")
        if self.hiddenWord == self.wordArr:
            print("Player 2 Won!\n The word was: " + self.theWord + ".")
    def play(self):
        """
        lays out the structure of the game.
        """
        self.getWord()
        while not self.gameOver():
            self.displayState()
            self.guessLetter()
        self.displayResult()


if __name__ == "__main__": #incase I ever want to import this script
    while True:
        game = Hangman()
        game.play()

        replay = input("Do you want to play again? y/n : ").lower()
        while replay not in ['y', 'n']:
            print("Invalid response. Please enter y or n.")
            replay = input("Do you want to play again? y/n: ").lower()

        if replay == 'n':
            print("Goodbye!")
            break
