from CupArray import CupArray
from TeamPlayer import Team, Player


class PongGame:
    def __init__(self):
        self.playerA1 = input("Enter first player's name on Team A: ").upper()
        self.playerA2 = input("Enter second player's name on Team A (input same name for singles): ").upper()
        self.teamA = Team(self.playerA1, self.playerA2)
        self.teamA_wins = 0
        self.playerB1 = input("Enter first player's name on Team B: ").upper()
        self.playerB2 = input("Enter second player's name on Team B (input same name for singles): ").upper()
        self.teamB = Team(self.playerB1, self.playerB2)
        self.overtimeCount = 0
        self.teamB_wins = 0

    def playSeries(self, first_turn="IDK"):
        result = 0
        while True:
            print("\n\n\nEntering Game", self.teamA_wins+self.teamB_wins+1)
            print(self.playerA1, end=" ")
            if self.playerA1 != self.playerA2:
                print("and", self.playerA2, end=" ")
            print("with", self.teamA_wins, "wins", end="\n")
            print(self.playerB1, end=" ")
            if self.playerB1 != self.playerB2:
                print("and", self.playerB2, end=" ")
            print("with", self.teamB_wins, "wins", end="\n\n")

            result = self.playGame(first_turn)

            if result == 1:
                self.teamA_wins += 1
                first_turn = "Team A"
            elif result == -1:
                self.teamB_wins += 1
                first_turn = "Team B"

            another_game = input("Another Game? ").lower()
            if (another_game == "n") or (another_game == "no"):
                print("\n\n\nSeries over in", self.teamA_wins + self.teamB_wins, "games")
                print(self.playerA1, end=" ")
                if self.playerA1 != self.playerA2:
                    print("and", self.playerA2, end=" ")
                print("with", self.teamA_wins, "wins")
                print(self.playerB1, end=" ")
                if self.playerB1 != self.playerB2:
                    print("and", self.playerB2, end=" ")
                print("with", self.teamB_wins, "wins", end="\n\n")
                break

    def playGame(self, first_turn="IDK"):
        self.teamA = Team(self.playerA1, self.playerA2)
        self.teamB = Team(self.playerB1, self.playerB2)
        self.overtimeCount = 0
        teamAturn = "Continue"
        teamBturn = "Continue"
        turn = first_turn
        while (turn != "Team A") and (turn != "Team B"):
            inputstring = "Who starts? Team A (" + self.playerA1
            if self.playerA1 != self.playerA2:
                inputstring += " and" + self.playerA2
            inputstring += ") or Team B (" + self.playerB1
            if self.playerB1 != self.playerB2:
                inputstring += " and " + self.playerB2
            inputstring += ")? "
            turn = input(inputstring)

        while (turn == "Team A") or (turn == "Team B"):
            # if it is Team A's turn
            if turn == "Team A":
                print("\n", self.playerA1, end="")
                if self.playerA1 != self.playerA2:
                    print(" and", self.playerA2, end="")
                print("\'s Turn")

                # run Team A's turn
                teamAturn = self.teamA.turn()

                # if Team A passes
                if teamAturn == "Continue":
                    # if Team A was in redemption, the game is over, Team B wins
                    if teamBturn == "Rack Clear":
                        turn = "Team B Wins!"
                        return -1
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
                        return 1

            # if it is Team B's turn
            if turn == "Team B":
                print("\n", self.playerB1, end="")
                if self.playerB1 != self.playerB2:
                    print(" and", self.playerB2, end="")
                print("\'s Turn")

                # run Team B's turn
                teamBturn = self.teamB.turn()

                # if Team B passes
                if teamBturn == "Continue":
                    # if Team B was in redemption, the game is over, Team A wins
                    if teamAturn == "Rack Clear":
                        turn = "Team A Wins!"
                        return 1
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
                        return -1






