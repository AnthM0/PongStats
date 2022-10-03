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
        teamAturn = "Continue"
        teamBturn = "Continue"
        turn = "Team A"
        while (turn == "Team A") or (turn == "Team B"):
            # if it is Team A's turn
            if turn == "Team A":
                # run Team A's turn
                teamAturn = self.teamA.turn()

                # if Team A passes
                if teamAturn == "Continue":
                    # if Team A was in redemption, the game is over, Team B wins
                    if teamBturn == "Rack Clear":
                        turn = "Team B Wins!"
                    # otherwise, it is Team B's turn
                    else:
                        turn = "Team B"
                # if Team A clears the rack
                elif teamAturn == "Rack Clear":
                    # if Team A was in redemption, enter overtime
                    if teamBturn == "Rack Clear":
                        print("Entering Overtime...")
                        self.overtimeCount += 1
                        self.teamA.enter_overtime(self.overtimeCount)
                        self.teamB.enter_overtime(self.overtimeCount)
                        turn = "Team B"
                    # otherwise, put Team B in redemption
                    else:
                        print("Team B is entering Redemption")
                        self.teamB.enter_redemption()
                        turn = "Team B"
                # if Team A ices it...
                elif teamAturn == "Iced":
                    # if Team A was in redemption, enter overtime with Team A's turn
                    if teamBturn == "Rack Clear":
                        print("Entering Overtime...")
                        self.overtimeCount += 1
                        self.teamA.enter_overtime(self.overtimeCount)
                        self.teamB.enter_overtime(self.overtimeCount)
                        turn = "Team A"
                    # otherwise, game over, Team A wins
                    else:
                        turn = "Team A Wins!"

            # if it is Team B's turn
            if turn == "Team B":
                # run Team B's turn
                teamBturn = self.teamB.turn()

                # if Team B passes
                if teamBturn == "Continue":
                    # if Team B was in redemption, the game is over, Team A wins
                    if teamAturn == "Rack Clear":
                        turn = "Team A Wins!"
                    # otherwise, it is Team A's turn
                    else:
                        turn = "Team A"
                # if Team B clears the rack
                elif teamBturn == "Rack Clear":
                    # if Team B was in redemption, enter overtime
                    if teamAturn == "Rack Clear":
                        print("Entering Overtime...")
                        self.overtimeCount += 1
                        self.teamA.enter_overtime(self.overtimeCount)
                        self.teamB.enter_overtime(self.overtimeCount)
                        turn = "Team A"
                    # otherwise, put Team A in redemption
                    else:
                        print("Team A is entering Redemption")
                        self.teamA.enter_redemption()
                        turn = "Team A"
                        # if Team A ices it...
                elif teamBturn == "Iced":
                    # if Team B was in redemption, enter overtime with Team B's turn
                    if teamAturn == "Rack Clear":
                        print("Entering Overtime...")
                        self.overtimeCount += 1
                        self.teamA.enter_overtime(self.overtimeCount)
                        self.teamB.enter_overtime(self.overtimeCount)
                        turn = "Team B"
                    # otherwise, game over, Team A wins
                    else:
                        turn = "Team B Wins!"

        print(turn)





