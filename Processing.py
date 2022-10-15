import csv

player_results = {}

with open('ShotLog.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    last_game = 0
    for row in reader:
        print(row)
        print(row[1])
        # player_name = row[1]
        # if player_name not in player_results.keys():
        #     player_results[player_name] = [0, 0]
        # player_results[row[player_name]][0] += 1
        # comma = True
        # while comma:
        #
        # if row[2] != 0:
        #     player_results[row[player_name]][1] += 1

print(player_results)