from TeamPlayer import Team, Player
import csv


class PongGame:
    def __init__(self, on_record=True):
        self.on_record = on_record
        self.playerA1 = input("Enter first player's name on Team A: ").upper()
        self.playerA2 = input("Enter second player's name on Team A (input same name for singles): ").upper()
        self.teamA_wins = 0
        self.playerB1 = input("Enter first player's name on Team B: ").upper()
        self.playerB2 = input("Enter second player's name on Team B (input same name for singles): ").upper()
        self.overtimeCount = 0
        self.teamB_wins = 0
        with open('ShotLog.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            last_game = 0
            for row in reader:
                comma_index = -1
                while row[0][comma_index] != ",":
                    comma_index -= 1
                last_game = int(row[0][(comma_index + 1):])
        self.game_number = last_game
        self.teamA = Team(self.playerA1, self.playerA2, self.game_number, self.on_record)
        self.teamB = Team(self.playerB1, self.playerB2, self.game_number, self.on_record)

    def playSeries(self, first_turn="IDK"):
        result = 1
        while (result == 1) or (result == -1):
            self.game_number += 1
            print("\n\n\nEntering Game", self.teamA_wins+self.teamB_wins+1, "(Number", self.game_number, "on record)")
            print(self.playerA1, end=" ")
            if self.playerA1 != self.playerA2:
                print("and", self.playerA2, end=" ")
            if (self.teamA_wins == 0) or (self.teamA_wins > 1):
                print("with", self.teamA_wins, "wins")
            else:
                print("with", self.teamA_wins, "win")
            print(self.playerB1, end=" ")
            if self.playerB1 != self.playerB2:
                print("and", self.playerB2, end=" ")
            if (self.teamB_wins == 0) or (self.teamB_wins > 1):
                print("with", self.teamB_wins, "wins")
            else:
                print("with", self.teamB_wins, "win")

            result = self.playGame(first_turn)
            if result == 1:
                self.teamA_wins += 1
                first_turn = "Team A"
            elif result == -1:
                self.teamB_wins += 1
                first_turn = "Team B"

            game_hash = [result, self.playerA1, self.playerA2, self.teamA.rack.hash(), self.playerB1, self.playerB2,
                         self.teamB.rack.hash(), self.overtimeCount, self.teamA_wins+self.teamB_wins, self.teamA_wins,
                         self.teamB_wins, self.game_number]
            if self.on_record:
                with open('GameLog.csv', 'a', newline='') as csvfile:
                    reader = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    reader.writerow(game_hash)
                print("Logged:", game_hash)
            else:
                print("Did NOT log:", game_hash)

            another_game = input("Another Game? ").lower()
            if (another_game == "n") or (another_game == "no"):
                if (self.teamA_wins + self.teamB_wins) > 1:
                    print("\n\n\nSeries over in", self.teamA_wins + self.teamB_wins, "games")
                else:
                    print("\n\n\nSeries over in", self.teamA_wins + self.teamB_wins, "game")
                print(self.playerA1, end=" ")
                if self.playerA1 != self.playerA2:
                    print("and", self.playerA2, end=" ")
                if (self.teamA_wins == 0) or (self.teamA_wins > 1):
                    print("with", self.teamA_wins, "wins")
                else:
                    print("with", self.teamA_wins, "win")
                print(self.playerB1, end=" ")
                if self.playerB1 != self.playerB2:
                    print("and", self.playerB2, end=" ")
                if (self.teamB_wins == 0) or (self.teamB_wins > 1):
                    print("with", self.teamB_wins, "wins", end="\n\n")
                else:
                    print("with", self.teamB_wins, "win", end="\n\n")
                result = 0

    def playGame(self, first_turn="IDK"):
        self.teamA = Team(self.playerA1, self.playerA2, self.game_number, self.on_record)
        self.teamB = Team(self.playerB1, self.playerB2, self.game_number, self.on_record)
        self.overtimeCount = 0
        teamAturn = "Continue"
        teamBturn = "Continue"
        turn = first_turn
        while (turn != "Team A") and (turn != "Team B"):
            if (self.playerA1 in turn.upper()) or (self.playerA2 in turn.upper()):
                turn = "Team A"
            elif (self.playerB1 in turn.upper()) or (self.playerB2 in turn.upper()):
                turn = "Team B"
            else:
                if (self.playerA1[0] == turn[0].upper()) or (self.playerA2[0] == turn[0].upper()) and not (self.playerB1[0] == turn[0].upper()) or (self.playerB2[0] == turn[0].upper()):
                    turn = "Team A"
                elif (self.playerB1[0] == turn[0].upper()) or (self.playerB2[0] == turn[0].upper()):
                    turn = "Team B"
                else:
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
                print("\n", self.playerA1, sep="", end="")
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
                print("\n", self.playerB1, sep="", end="")
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






