# Cricket Tournament Analytics System
'''Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report. '''

players = {
    "Virat": {"runs": 500, "wickets": 2},
    "Rohit": {"runs": 450, "wickets": 1},
    "Hardik": {"runs": 300, "wickets": 8},
    "Gill": {"runs": 250, "wickets": 0},
    "Jadeja": {"runs": 200, "wickets": 10}
}

while True:

    print("\n1.Display Players")
    print("2.Add Player")
    print("3.Highest Run Scorer")
    print("4.Lowest Run Scorer")
    print("5.Average Runs")
    print("6.Maximum Wickets")
    print("7.All Rounders")
    print("8.Above Average Players")
    print("9.Player Categories")
    print("10.Award Winners")
    print("11.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        for p in players:
            print(p, players[p])

    elif ch == 2:

        name = input("Enter Player Name: ")
        runs = int(input("Enter Runs: "))
        wickets = int(input("Enter Wickets: "))

        players[name] = {
            "runs": runs,
            "wickets": wickets
        }

        print("Player Added")

    elif ch == 3:

        best = ""
        max_runs = -1

        for p in players:

            if players[p]["runs"] > max_runs:

                max_runs = players[p]["runs"]
                best = p

        print("Highest Run Scorer =", best)

    elif ch == 4:

        low = ""
        min_runs = 99999

        for p in players:

            if players[p]["runs"] < min_runs:

                min_runs = players[p]["runs"]
                low = p

        print("Lowest Run Scorer =", low)

    elif ch == 5:

        total = 0

        for p in players:
            total += players[p]["runs"]

        avg = total / len(players)

        print("Average Runs =", avg)

    elif ch == 6:

        bowler = ""
        max_wicket = -1

        for p in players:

            if players[p]["wickets"] > max_wicket:

                max_wicket = players[p]["wickets"]
                bowler = p

        print("Maximum Wickets =", bowler)

    elif ch == 7:

        print("All Rounders:")

        for p in players:

            if players[p]["runs"] > 200 and players[p]["wickets"] > 5:
                print(p)

    elif ch == 8:

        total = 0

        for p in players:
            total += players[p]["runs"]

        avg = total / len(players)

        print("Players Above Average:")

        for p in players:

            if players[p]["runs"] > avg:
                print(p)

    elif ch == 9:

        for p in players:

            runs = players[p]["runs"]

            if runs >= 400:
                print(p, "- Star Performer")

            elif runs >= 250:
                print(p, "- Good Performer")

            elif runs >= 100:
                print(p, "- Average Performer")

            else:
                print(p, "- Poor Performer")

    elif ch == 10:

        awards = {}

        for p in players:

            if players[p]["runs"] > 300:
                awards[p] = players[p]

        print("Award Winners:")
        print(awards)

    elif ch == 11:
        break

    else:
        print("Invalid Choice")