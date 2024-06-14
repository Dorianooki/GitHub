# 開啟檔案
file_name = "nba_standings.csv"
file = open(file_name, "r")
text = file.readlines()

# 問題一
print("Which teams from the Eastern Conference had the win-loss percentage of Home lower than the win-loss percentage of Away?")
for line in text[1:]:  # Skip header
    words = line.strip().split(",")
    if len(words) < 9:  # Ensure there are enough columns
        continue
    # 先確認該組是在Eastern
    if words[0] == "Eastern":
        # 將在主場與客場的勝敗場分開
        home = words[7].split("-")
        away = words[8].split("-")
        if len(home) < 2 or len(away) < 2:  # Ensure there are both wins and losses
            continue
        # 進行計算 若主場勝率 < 客場勝率 則 print 出該組
        home_wins = int(home[0])
        home_losses = int(home[1])
        away_wins = int(away[0])
        away_losses = int(away[1])
        home_pct = home_wins / (home_wins + home_losses)
        away_pct = away_wins / (away_wins + away_losses)
        if home_pct < away_pct:
            print(words[1])
print()

# 問題二
print("Which conference had a higher average difference about 'PF minus PA'?")
eastern_pf_pa_diff = []
western_pf_pa_diff = []

for line in text[1:]:  # Skip header
    words = line.strip().split(",")
    if len(words) < 9:  # Ensure there are enough columns
        continue
    pf = float(words[5])
    pa = float(words[6])
    diff = pf - pa
    if words[0] == "Eastern":
        eastern_pf_pa_diff.append(diff)
    elif words[0] == "Western":
        western_pf_pa_diff.append(diff)

average_pf_pa_diff_eastern = sum(eastern_pf_pa_diff) / len(eastern_pf_pa_diff) if eastern_pf_pa_diff else 0
average_pf_pa_diff_western = sum(western_pf_pa_diff) / len(western_pf_pa_diff) if western_pf_pa_diff else 0

higher_avg_pf_pa_diff_conference = "Eastern" if average_pf_pa_diff_eastern > average_pf_pa_diff_western else "Western"
print(f"The conference with a higher average PF minus PA is: {higher_avg_pf_pa_diff_conference}")
print()

# 問題三
print("Generate a ranking list of all teams based on wins against the other conference's teams.")
conference_wins = {}

for line in text[1:]:  # Skip header
    words = line.strip().split(",")
    if len(words) < 9:  # Ensure there are enough columns
        continue
    team = words[1]
    conference = words[0]
    win_loss = words[2].split("-")
    
    # Ensure there are wins and losses data
    if len(win_loss) < 2:
        continue
    
    total_wins = int(win_loss[0])
    total_losses = int(win_loss[1])
    
    # Cross-conference wins calculation
    if conference == "Eastern":
        home_record = words[7].split("-")
        home_wins = int(home_record[0])
        away_record = words[8].split("-")
        away_wins = int(away_record[0])
        cross_conference_wins = total_wins - home_wins  # Subtracting home wins (same conference)
    elif conference == "Western":
        home_record = words[7].split("-")
        home_wins = int(home_record[0])
        away_record = words[8].split("-")
        away_wins = int(away_record[0])
        cross_conference_wins = total_wins - away_wins  # Subtracting away wins (same conference)
    
    conference_wins[team] = cross_conference_wins

# Sort teams based on cross-conference wins
ranked_teams = sorted(conference_wins.items(), key=lambda x: x[1], reverse=True)

print("Ranking list of all teams based on cross-conference wins:")
for rank, (team, wins) in enumerate(ranked_teams, 1):
    print(f"{rank}. {team}: {wins} wins against the other conference")

file.close()
