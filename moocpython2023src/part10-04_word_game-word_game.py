# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str)->str:
        "winner longest word "
        winner = 0
        if len(player1_word) < len(player2_word):
            winner = 2
        elif len(player1_word) > len(player2_word):
            winner = 1
        return winner

class MostVowels(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowel(self, input_word: str)->int:
        vowels = "aeiou"
        # count vowels 
        total_vowels = 0
        for vowel in vowels:
            total_vowels += input_word.count(vowel)
        
        return total_vowels

    def round_winner(self, player1_word: str, player2_word: str)->str:
        "winner vowels word "
        winner = 0
        if self.count_vowel(player1_word) < self.count_vowel(player2_word):
            winner = 2
        elif self.count_vowel(player1_word) > self.count_vowel(player2_word):
            winner = 1
        return winner


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int)->None:
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str)->str:
        """
        rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
        paper beats rock (the paper can cover the rock)
        scissors beats paper (the scissors can cut the paper)
        """
        winner = 0
        rps = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
        if player1_word not in rps and player2_word not in rps:
            winner = 0 
        elif player1_word in rps and player2_word not in rps:
            winner = 1
        elif player1_word not in rps and player2_word in rps:
            winner = 2
        else:
            if rps[player2_word] == player1_word:
                winner = 2
            elif rps[player1_word] == player2_word:
                winner = 1
            
        return winner

if __name__ == "__main__":
    
    # Part 1 Longest word
    # p = LongestWord(2)
    # p.play()

    # Part 2 Most vowels wins
    # p = MostVowels(2)
    # p.play()

    # Part 3 

    p = RockPaperScissors(1)
    p.play()