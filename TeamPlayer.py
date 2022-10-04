from CupArray import CupArray
import csv

class Team:
    # Player player1
    # Player player2 (pointer to player1 if single player)
    # int nplayers
    # CupArray rack
    # int ballsbackP1 (Player 1's makes this turn, decreases by 1 when balls back is awarded)
    # int ballsbackP2 (Player 2's makes this turn, decreases by 1 when balls back is awarded)
    # bool rerack_avalible
    # bool redemption
    # bool overtime
    # int nturn

    def __init__(self, player1, player2, gamenumber, on_record):
        self.player1 = Player(player1, player2, gamenumber, on_record)
        if player1 == player2:
            self.player2 = self.player1
            self.nplayers = 1
        else:
            self.player2 = Player(player2, player1, gamenumber, on_record)
            self.nplayers = 2
        self.rack = CupArray()
        self.ballsbackP1 = 0
        self.ballsbackP2 = 0
        self.rerack_avalible = True
        self.redemption = False
        self.overtime = False
        self.nturn = 0

    def enter_redemption(self):
        self.redemption = True

    def enter_overtime(self, count):
        self.redemption = False
        self.overtime = True
        self.rack.overtime(count)

    def turn(self):
        # display the current rack
        self.rack.show()

        # if you have 2 cups or less, offer rerack (for gentleman's)
        if self.rack.ncups <= 2:
            self.rerack_avalible = True

        # if you have a rerack avalible,
        if (self.rack.ncups < 7) and self.rerack_avalible and (not self.rack.reracked_to_this):
            rerack_result = False
            # ask if the player wants a rerack
            rerackrequest = input("Do you want a rerack (input name): ").lower()
            if not((rerackrequest == "no") or (rerackrequest == "n") or (rerackrequest == "")):
                rerack_result = self.rack.rerack(rerackrequest)
                while not rerack_result:
                    rerackrequest = input("Do you want a rerack (input name): ").lower()
                    if (rerackrequest == "no") or (rerackrequest == "n") or (rerackrequest == ""):
                        break
                    rerack_result = self.rack.rerack(rerackrequest)
            # if the player took a rerack, update their rerack availability
            if rerack_result:
                self.rerack_avalible = False
                self.rack.show()

        self.nturn += 1
        self.player1.shots += 1
        self.player2.shots += 1
        self.ballsbackP1 = 0
        self.ballsbackP2 = 0
        rack_clear = False
        ice = False

        while (self.player1.shots > 0) or (self.player2.shots > 0):
            forballsback = False

            # if it is a single-player team
            if self.nplayers == 1:
                # check if the shot is for balls back
                if self.ballsbackP1 > 0:
                    forballsback = True
                    # if there is only one cup left, the player could ice the game
                    if self.rack.ncups == 1:
                        print("Ice Opportunity...")
                        ice = True
                # shooting result
                result = self.player1.shot(self.rack, forballsback, ice, self.redemption, self.overtime, self.nturn)
                # if Player didn't miss, update the balls back tracker
                if result != "Miss":
                    if self.ballsbackP1 < 1:
                        self.ballsbackP1 += 1
                    else:
                        self.ballsbackP2 += 1

            # if Player 1 is the only player with shots left, they must go
            elif self.player2.shots < 1:
                # check if the shot is for balls back
                if self.ballsbackP2 > 0:
                    forballsback = True
                    # if there is only one cup left, the player could ice the game
                    if self.rack.ncups == 1:
                        print("Ice Opportunity...")
                        ice = True
                # shooting result
                result = self.player1.shot(self.rack, forballsback, ice, self.redemption, self.overtime, self.nturn)
                # if Player 1 didn't miss, update the balls back tracker
                if result != "Miss":
                    self.ballsbackP1 += 1

            # if Player 2 is the only player with shots left, it is their shot
            elif self.player1.shots < 1:
                # check if the shot is for balls back
                if self.ballsbackP1 > 0:
                    forballsback = True
                    # if there is only one cup left, the player could ice the game
                    if self.rack.ncups == 1:
                        print("Ice Opportunity...")
                        ice = True
                # shooting result
                result = self.player2.shot(self.rack, forballsback, ice, self.redemption, self.overtime, self.nturn)
                # if Player 2 didn't miss, update the balls back tracker
                if result != "Miss":
                    self.ballsbackP2 += 1

            # else, ask who is up first
            else:
                firstPlayer = input("Who is up first? ").upper()
                while (firstPlayer != self.player1.name) and (firstPlayer != self.player2.name):
                    firstPlayer = input("Who is up first? ").upper()

                # Player 1 goes
                if firstPlayer == self.player1.name:
                    # check if the shot is for balls back
                    if self.ballsbackP2 > 0:
                        forballsback = True
                        # if there is only one cup left, the player could ice the game
                        if self.rack.ncups == 1:
                            print("Ice Opportunity...")
                            ice = True
                    # shooting result
                    result = self.player1.shot(self.rack, forballsback, ice, self.redemption, self.overtime, self.nturn)
                    # if Player 1 didn't miss, update the balls back tracker
                    if result != "Miss":
                        self.ballsbackP1 += 1

                # Player 2 goes
                elif firstPlayer == self.player2.name:
                    # check if the shot is for balls back
                    if self.ballsbackP1 > 0:
                        forballsback = True
                        # if there is only one cup left, the player could ice the game
                        if self.rack.ncups == 1:
                            print("Ice Opportunity...")
                            ice = True
                    # shooting result
                    result = self.player2.shot(self.rack, forballsback, ice, self.redemption, self.overtime, self.nturn)
                    # if Player 2 didn't miss, update the balls back tracker
                    if result != "Miss":
                        self.ballsbackP2 += 1

            # if the last cup is made...
            if (result[0] == "A") or (result[0] == "B") and (not self.redemption):
                # if the players would get balls back, the game is over
                if (self.ballsbackP1 > 0) and (self.ballsbackP2 > 0):
                    print("Iced! Game Over!")
                    return "Iced"
                # if it was an Ice Opportunity and a player makes a cup, the game is over
                if ice and ((self.ballsbackP1 > 0) or (self.ballsbackP2 > 0)):
                    print("Iced! Game Over!")
                    return "Iced"
                # otherwise, we enter into an Ice Opportunity
                if (self.player1.shots > 0) or (self.player2.shots > 0):
                    print("Ice Opportunity...")
                    ice = True
                    rack_clear = True
                    self.ballsbackP1 = 0
                    self.ballsbackP2 = 0
                    self.rack.addcup(result)

            # if both player have made a shot, give them balls back
            if (self.ballsbackP1 > 0) and (self.ballsbackP2 > 0) and (not self.redemption):
                print("Balls Back!")
                self.player1.shots += 1
                self.ballsbackP1 -= 1
                self.player2.shots += 1
                self.ballsbackP2 -= 1

        print("Turn Over")
        if rack_clear:
            return "Rack Clear"
        return "Continue"


class Player:
    def __init__(self, name, teammate, gamenumber, on_record):
        self.name = name
        self.on_record = on_record
        self.teammate = teammate
        self.streak = 0
        self.shots = 0
        self.gamenumber = gamenumber

    def shot(self, cup_array, forballsback, ice, redemption, overtime, turn):
        # Models a Player's shot.
        # Returns: "Make" if the player makes the cup (Even if it's an Island)
        #          "Make - Rack Empty" if the player makes the last cup
        #          "Miss" if the player does not make a cup
        self.shots -= 1

        old_shot_hash = [cup_array.hash(), forballsback, ice, redemption, overtime, self.teammate, turn, self.gamenumber]
        result = "Error"
        while result == "Error":
            cup = input("Input cup " + self.name + " made (input 0 for a miss): ").upper()
            if cup == "0":
                result = "Miss"
                new_streak = 0
            else:
                result = cup_array.makecup(cup)
                new_streak = self.streak + 1

        # if the shot was an island, mark that
        if result == "Island":
            island = True
        else:
            island = False

        # if the player has made two or more cups, note they are On Fire and give them another shot
        if (new_streak > 2) and (self.name != self.teammate) and (not redemption):
            print(self.name, "is on FIRE!")
            self.shots += 1

        # if it is in redemption, give the player another shot
        if (new_streak > 0) and redemption:
            print(self.name, "stays alive.")
            self.shots += 1

        # store the log of the shot
        shot_hash = [">>>", self.name, cup, self.streak, island]
        if self.on_record:
            for i in old_shot_hash:
                shot_hash.append(i)
            with open('ShotLog.csv', 'a', newline='') as csvfile:
                reader = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                reader.writerow(shot_hash)
            print("Logged:", shot_hash)
        else:
            print("Did NOT log:", shot_hash)

        # update the player's streak
        self.streak = new_streak

        # return the result of the shot
        if result == "Miss":
            return "Miss"
        if cup_array.ncups == 0:
            return cup
        return "Make"
