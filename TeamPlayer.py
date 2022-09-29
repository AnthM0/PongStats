from CupArray import CupArray


class Team:
    # Player player1
    # Player player2 (pointer to player1 if single player)
    # int nplayers
    # CupArray rack
    # Array ballsback (contains players ("p1" or "p2") that have made their shots this turn)
    # int nturn

    def __init__(self, player1, player2):
        self.player1 = Player(player1, player2, 1)
        if player1 == player2:
            self.player2 = self.player1
            self.nplayers = 1
        else:
            self.player2 = Player(player2, player1, 1)
            self.nplayers = 2
        self.rack = CupArray()
        self.ballsback = []
        self.nturn = 0

    def turn(self):
        self.rack.show()
        if (self.rack.ncups < 10) and (True):
            rerackrequest = input("Do you want a rerack?")
            while not self.rack.rerack(rerackrequest):
                rerackrequest = input("Do you want a rerack?")

        self.nturn += 1
        self.player1.shots += 1
        self.player2.shots += 1
        self.ballsback = []

        while (self.player1.shots > 0) or (self.player2.shots > 0):
            if self.nplayers == 1:
                result = self.player1.shot(self.rack, False, False, False, False, self.nturn)
                if self.player1.streak > 0:
                    if "p1" in self.ballsback:
                        self.ballsback.append("p2")
                    else:
                        self.ballsback.append("p1")
            elif self.player2.shots < 1:
                result = self.player1.shot(self.rack, False, False, False, self.nturn)
                if self.player1.streak > 0:
                    self.ballsback.append("p1")
            elif self.player1.shots < 1:
                result = self.player2.shot(self.rack, False, False, False, self.nturn)
                if self.player2.streak > 0:
                    self.ballsback.append("p2")
            else:
                firstPlayer = input("Who is up first? ").upper()
                while (firstPlayer != self.player1.name) and (firstPlayer != self.player2.name):
                    firstPlayer = input("Who is up first? ").upper()
                if firstPlayer == self.player1.name:
                    result = self.player1.shot(self.rack, False, False, False, self.nturn)
                    if self.player2.streak > 0:
                        self.ballsback.append("p1")
                else:
                    result = self.player2.shot(self.rack, False, False, False, self.nturn)
                    if self.player2.streak > 0:
                        self.ballsback.append("p2")

            # if result == "Rack Empty":
            #     if ("p1" in self.ballsback) and ("p2" in self.ballsback):
            #         return "Game Over"
            # if (result == "Rack Empty") and ((self.player1.shots > 0) or (self.player2.shots > 0)):
            #     print("Entering Ice")
            #     ice = True
            #     self.ballsback = []
            #     self.rack.ncups = 1
            #     self.rack.rerack("back cup")

            if ("p1" in self.ballsback) and ("p2" in self.ballsback):
                print("Balls Back!")
                self.player1.shots += 1
                self.player2.shots += 1
                self.ballsback.remove("p1")
                self.ballsback.remove("p2")

        print("Turn Over")
        if self.rack.ncups > 0:
            return "Continue"
        return "Redemption"


class Player:
    def __init__(self, name, teammate, gamenumber):
        self.name = name
        self.teammate = teammate
        self.streak = 0
        self.shots = 0
        self.gamenumber = gamenumber

    def shot(self, cup_array, forballsback, ice, redemption, overtime, turn):
        self.shots -= 1
        shot_hash = cup_array.hash() + "," + str(forballsback) + "," + str(ice) + "," + str(redemption) + "," +\
                    str(overtime) + "," + self.teammate + "," + str(turn) + "," + str(self.gamenumber)
        result = "Error"
        while result == "Error":
            cup = input("Input cup " + self.name + " made (input 0 for a miss): ").upper()
            if cup == "0":
                result = "Miss"
                new_streak = 0
            else:
                result = cup_array.makecup(cup)
                new_streak = self.streak + 1
        if result == "Island":
            island = True
        else:
            island = False
        if (new_streak > 2) and (self.name != self.teammate):
            print(self.name, "is on FIRE!")
            self.shots += 1
        print(">>> ", self.name, cup, self.streak, island, shot_hash, sep=",")
        self.streak = new_streak
        if cup_array.ncups == 0:
            return "Rack Empty"
        return "Make"



