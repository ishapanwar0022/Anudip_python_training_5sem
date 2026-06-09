#4. Cricket Tournament Analytics System 
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
12. Create a separate dictionary for award winners. '''

# Cricket Tournament Analytics System

players = {
    "Virat": {"runs": 500, "wickets": 2},
    "Rohit": {"runs": 450, "wickets": 1},
    "Hardik": {"runs": 300, "wickets": 8}
}

while True:

    print("\n1.Display Players")
    print("2.Add Player")
    print("3.Highest Run Scorer")
    print("4.Maximum Wickets")
    print("5.All Rounders")
    print("6.Exit")

    ch = int(input("Enter Choice: "))

    # Display Players
    if ch == 1:

        for p in players:
            print(p, players[p])

    # Add Player
    elif ch == 2:

        name = input("Enter Player Name: ")
        runs = int(input("Enter Runs: "))
        wickets = int(input("Enter Wickets: "))

        players[name] = {
            "runs": runs,
            "wickets": wickets
        }

        print("Player Added")

    # Highest Run Scorer
    elif ch == 3:

        best = ""
        max_runs = 0

        for p in players:

            if players[p]["runs"] > max_runs:

                max_runs = players[p]["runs"]
                best = p

        print("Highest Run Scorer =", best)

    # Maximum Wickets
    elif ch == 4:

        bowler = ""
        max_wicket = 0

        for p in players:

            if players[p]["wickets"] > max_wicket:

                max_wicket = players[p]["wickets"]
                bowler = p

        print("Maximum Wickets =", bowler)

    # All Rounders
    elif ch == 5:

        print("All Rounders:")

        for p in players:

            if players[p]["runs"] > 200 and players[p]["wickets"] > 5:
                print(p)

    # Exit
    elif ch == 6:
        break

    else:
        print("Invalid Choice")