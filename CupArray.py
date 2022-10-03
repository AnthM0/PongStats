
class CupArray:
    def __init__(self):
        self.situation = {"A1": True, "A2": True, "A3": True, "A4": True, "A5": True,
                          "A6": True, "A7": True, "A8": True, "A9": True, "A10": True,
                          "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                          "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                          "C1": False, "C2": False, "C3": False}
        self.ROF_situation = {"A1": False, "A2": True, "A3": True, "A4": True, "A5": False,
                              "A6": True, "A7": False, "A8": True, "A9": True, "A10": False,
                              "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                              "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                              "C1": False, "C2": False, "C3": False}
        self.RROF_situation = {"A1": True, "A2": False, "A3": False, "A4": False, "A5": True,
                               "A6": False, "A7": True, "A8": False, "A9": False, "A10": True,
                               "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                               "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                               "C1": False, "C2": False, "C3": False}
        self.ncups = 10
        self.reracked_to_this = True

    def hash(self):
        returnString = ""
        for key in self.situation.keys():
            if self.situation[key]:
                returnString += key + "-"
        return returnString

    def show(self):
        if self.situation["C1"]:
            print("    C1")
        if self.situation["C2"] or self.situation["C3"]:
            if self.situation["C2"]:
                print("  C2  ", end="")
            else:
                print("      ", end="")
            if self.situation["C3"]:
                print("C3")
            else:
                print()
        if self.situation["A1"]:
            print("      A1")
        if self.situation["A1"] or self.situation["A2"] or self.situation["A3"]:
            if self.situation["A2"]:
                print("    A2  ", end="")
            else:
                print("        ", end="")
            if self.situation["A3"]:
                print("A3")
            else:
                print()
        if self.situation["A1"] or self.situation["A2"] or self.situation["A3"] or self.situation["A4"] or \
                self.situation["A5"] or self.situation["A6"]:
            if self.situation["A4"]:
                print("  A4  ", end="")
            else:
                print("      ", end="")
            if self.situation["A5"]:
                print("A5  ", end="")
            else:
                print("    ", end="")
            if self.situation["A6"]:
                print("A6")
            else:
                print()
        if self.situation["A1"] or self.situation["A2"] or self.situation["A3"] or self.situation["A4"] or \
                self.situation["A5"] or self.situation["A6"] or self.situation["A7"] or self.situation["A8"] or \
                self.situation["A9"] or self.situation["A10"]:
            if self.situation["A7"]:
                print("A7  ", end="")
            else:
                print("    ", end="")
            if self.situation["A8"]:
                print("A8  ", end="")
            else:
                print("    ", end="")
            if self.situation["A9"]:
                print("A9  ", end="")
            else:
                print("    ", end="")
            if self.situation["A10"]:
                print("A10")
            else:
                print()
        if self.situation["B1"]:
            print("B1")
        if self.situation["B1"] or self.situation["B2"] or self.situation["B3"]:
            if self.situation["B2"]:
                print("B2  ", end="")
            else:
                print("    ", end="")
            if self.situation["B3"]:
                print("B3")
            else:
                print()
        if self.situation["B1"] or self.situation["B2"] or self.situation["B3"] or self.situation["B4"] or \
                self.situation["B5"]:
            if self.situation["B4"]:
                print("B4  ", end="")
            else:
                print("    ", end="")
            if self.situation["B5"]:
                print("B5")
            else:
                print()
        if self.situation["B1"] or self.situation["B2"] or self.situation["B3"] or self.situation["B4"] or \
                self.situation["B5"] or self.situation["B6"] or self.situation["B7"]:
            if self.situation["B6"]:
                print("B6  ", end="")
            else:
                print("    ", end="")
            if self.situation["B7"]:
                print("B7")
            else:
                print()
        if self.situation["B1"] or self.situation["B2"] or self.situation["B3"] or self.situation["B4"] or \
                self.situation["B5"] or self.situation["B6"] or self.situation["B7"] or self.situation["B8"] or \
                self.situation["B9"]:
            if self.situation["B8"]:
                print("B8  ", end="")
            else:
                print("    ", end="")
            if self.situation["B9"]:
                print("B9")
            else:
                print()
        if self.situation["B10"]:
            print("    B10")

    def addcup(self, cup):
        if cup not in self.situation.keys():
            return "Error"
        if not self.situation[cup.upper()]:
            self.ncups += 1
            self.situation[cup.upper()] = True
            self.reracked_to_this = True
            return cup
        return "Error"

    def makecup(self, cup):
        if cup not in self.situation.keys():
            return "Error"
        if self.checkROF(cup):
            self.ncups = 0
            self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                              "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                              "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                              "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                              "C1": False, "C2": False, "C3": False}
            return cup
        if self.situation[cup.upper()]:
            self.situation[cup.upper()] = False
            self.ncups -= 1
            self.reracked_to_this = False
            return self.checkIsland(cup)
        else:
            return "Error"

    def island(self):
        while True:
            islandCup = input("Choose a cup:").upper()
            if self.situation[islandCup]:
                self.situation[islandCup] = False
                self.ncups -= 1
                return "Island"

    def checkIsland(self, cup):
        if self.ncups <= 1:
            return cup
        if cup == "A1" and (self.situation["A2"] or self.situation["A3"]):
            return "Make"
        if cup == "A2" and (self.situation["A1"] or self.situation["A3"] or self.situation["A4"] or self.situation["A5"]):
            return "Make"
        if cup == "A3" and (self.situation["A1"] or self.situation["A2"] or self.situation["A4"] or self.situation["A5"]):
            return "Make"
        if cup == "A4" and (self.situation["A2"] or self.situation["A5"] or self.situation["A7"] or self.situation["A8"]):
            return "Make"
        if cup == "A5" and (self.situation["A2"] or self.situation["A3"] or self.situation["A4"] or self.situation["A6"]
                            or self.situation["A8"] or self.situation["A9"]):
            return "Make"
        if cup == "A6" and (self.situation["A3"] or self.situation["A5"] or self.situation["A9"] or self.situation["A10"]):
            return "Make"
        if cup == "A7" and (self.situation["A4"] or self.situation["A8"]):
            return "Make"
        if cup == "A8" and (self.situation["A7"] or self.situation["A4"] or self.situation["A5"] or self.situation["A9"]):
            return "Make"
        if cup == "A9" and (self.situation["A8"] or self.situation["A5"] or self.situation["A6"] or self.situation["A10"]):
            return "Make"
        if cup == "A10" and (self.situation["A9"] or self.situation["A6"]):
            return "Make"
        if cup == "B1" and (self.situation["B2"] or self.situation["B3"]):
            return "Make"
        if cup == "B2" and (self.situation["B1"] or self.situation["B3"] or self.situation["B4"]):
            return "Make"
        if cup == "B3" and (self.situation["B1"] or self.situation["B2"] or self.situation["B4"] or self.situation["B5"]):
            return "Make"
        if cup == "B4" and (self.situation["B2"] or self.situation["B3"] or self.situation["B5"] or self.situation["B6"]):
            return "Make"
        if cup == "B5" and (self.situation["B3"] or self.situation["B4"] or self.situation["B6"] or self.situation["B7"]):
            return "Make"
        if cup == "B6" and (self.situation["B4"] or self.situation["B5"] or self.situation["B7"] or self.situation["B8"]):
            return "Make"
        if cup == "B7" and (self.situation["B5"] or self.situation["B6"] or self.situation["B8"] or self.situation["B9"]):
            return "Make"
        if cup == "B8" and (self.situation["B6"] or self.situation["B7"] or self.situation["B9"] or self.situation["B10"]):
            return "Make"
        if cup == "B9" and (self.situation["B7"] or self.situation["B8"] or self.situation["B10"]):
            return "Make"
        if cup == "B10" and (self.situation["B8"] or self.situation["B9"]):
            return "Make"
        if cup == "C1" or cup == "C2" or cup == "C3":
            return "Make"
        askIsland = input("Was Cup " + cup.upper() + " an island (y/n)?")
        if askIsland == "y":
            return self.island()
        return "Make"

    def checkROF(self, cup):
        if cup != "A5":
            return False
        else:
            ROF = True
            RROF = True
            for key in self.situation:
                if self.situation[key] != self.ROF_situation[key]:
                    ROF = False
                if self.situation[key] != self.RROF_situation[key]:
                    RROF = False
            if ROF:
                print("Ring of Fire!")
                return True
            if RROF:
                print("Reverse Ring of Fire!")
                return True
        return False

    def overtime(self, count):
        self.reracked_to_this = True
        if count == 1:
            self.ncups = 4
            self.situation = {"A1": False, "A2": False, "A3": False, "A4": True, "A5": False,
                              "A6": False, "A7": True, "A8": True, "A9": False, "A10": False,
                              "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                              "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                              "C1": False, "C2": True, "C3": False}
        if count == 2:
            self.ncups = 7
            self.situation = {"A1": False, "A2": False, "A3": False, "A4": True, "A5": True,
                              "A6": False, "A7": True, "A8": True, "A9": True, "A10": False,
                              "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                              "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                              "C1": False, "C2": True, "C3": True}
        if count >= 3:
            self.ncups = 9
            self.situation = {"A1": False, "A2": True, "A3": False, "A4": True, "A5": True,
                              "A6": False, "A7": True, "A8": True, "A9": True, "A10": False,
                              "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                              "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                              "C1": True, "C2": True, "C3": True}

    def rerack(self, name):
        if name.lower() == "zipper":
            name = "socialism"
        if name.lower() == "stoplight":
            name = "chain gang"
        if name.lower() == "gentlemans":
            name = "gentleman's"
        if name.lower() == "three-two-one":
            if self.ncups == 6:
                self.situation = {"A1": False, "A2": True, "A3": False, "A4": True, "A5": True,
                                  "A6": False, "A7": True, "A8": True, "A9": True, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "socialism":
            if self.ncups == 5:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": True, "B7": True, "B8": True, "B9": True, "B10": True,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "full house":
            if self.ncups == 5:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": True, "A5": True,
                                  "A6": False, "A7": True, "A8": True, "A9": True, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "skis":
            if self.ncups == 4:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": True, "B8": True, "B9": True, "B10": True,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "diamond":
            if self.ncups == 4:
                self.situation = {"A1": False, "A2": True, "A3": False, "A4": True, "A5": True,
                                  "A6": False, "A7": False, "A8": True, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "chain gang":
            if self.ncups == 3:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": True,
                                  "B6": False, "B7": True, "B8": False, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            if self.ncups == 4:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": True, "B4": False, "B5": True,
                                  "B6": False, "B7": True, "B8": False, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            if self.ncups == 5:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": True, "B2": False, "B3": True, "B4": False, "B5": True,
                                  "B6": False, "B7": True, "B8": False, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "triangle":
            if self.ncups == 3:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": True, "A5": False,
                                  "A6": False, "A7": True, "A8": True, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "play button":
            if self.ncups == 3:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": True, "B8": True, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "reverse triangle":
            if self.ncups == 3:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": True, "A5": True,
                                  "A6": False, "A7": False, "A8": True, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": False, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "gentleman's":
            if self.ncups == 2:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": True, "B8": False, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        if name.lower() == "back cup":
            if self.ncups == 1:
                self.situation = {"A1": False, "A2": False, "A3": False, "A4": False, "A5": False,
                                  "A6": False, "A7": False, "A8": False, "A9": False, "A10": False,
                                  "B1": False, "B2": False, "B3": False, "B4": False, "B5": False,
                                  "B6": False, "B7": False, "B8": False, "B9": True, "B10": False,
                                  "C1": False, "C2": False, "C3": False}
                self.reracked_to_this = True
                return True
            else:
                return False
        return False

