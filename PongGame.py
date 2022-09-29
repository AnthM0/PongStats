from CupArray import CupArray
from TeamPlayer import Team, Player


class PongGame:
    def __init__(self):
        self.playerA1 = input("Enter first player's name on Team A: ").upper()
        self.playerA2 = input("Enter second player's name on Team A (input same name for singles): ").upper()
        self.teamA = Team(self.playerA1, self.playerA2)
        self.playerB1 = input("Enter first player's name on Team B: ").upper()
        self.playerB2 = input("Enter second player's name on Team B (input same name for singles): ").upper()
        self.teamB = Team(self.playerB1, self.playerB2)
        self.overtimeCount = 0

    def playGame(self):
        while True:
            self.teamA.turn()
            self.teamB.turn()



