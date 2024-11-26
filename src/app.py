from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for standings using team names as strings
teams = [
    {"name": "Lakeside Lions", "wins": 10, "losses": 2, "points_for": 1594.96, "points_against": 1243.8, "head_to_head": {}},
    {"name": "Seattle Sickos", "wins": 7, "losses": 5, "points_for": 1383.9, "points_against": 1328.8, "head_to_head": {}},
    {"name": "GoHoos", "wins": 8, "losses": 4, "points_for": 1537.52, "points_against": 1412.12, "head_to_head": {}},
    {"name": "Raven Lunatics", "wins": 7, "losses": 5, "points_for": 1450.52, "points_against": 1308.98, "head_to_head": {}},
    {"name": "Deal Makers", "wins": 6, "losses": 6, "points_for": 1363.46, "points_against": 1191.94, "head_to_head": {}},
    {"name": "Henry", "wins": 6, "losses": 6, "points_for": 1252.72, "points_against": 1442.72, "head_to_head": {}},
    {"name": "Trojan Army", "wins": 7, "losses": 5, "points_for": 1246.62, "points_against": 1315.44, "head_to_head": {}},
    {"name": "Who here isn't eskimo bros", "wins": 6, "losses": 6, "points_for": 1406.6, "points_against": 1331.58, "head_to_head": {}},
    {"name": "Who's Your Daddy", "wins": 6, "losses": 6, "points_for": 1326.5, "points_against": 1308.6, "head_to_head": {}},
    {"name": "Diabeto Domination", "wins": 5, "losses": 7, "points_for": 1302.38, "points_against": 1402.12, "head_to_head": {}},
    {"name": "Jack the Gripper", "wins": 6, "losses": 6, "points_for": 1373.84, "points_against": 1278.66, "head_to_head": {}},
    {"name": "PEPE CARTEL", "wins": 3, "losses": 9, "points_for": 1281.86, "points_against": 1463.9, "head_to_head": {}},
    {"name": "Dawg Pound", "wins": 4, "losses": 8, "points_for": 1134.44, "points_against": 1332.72, "head_to_head": {}},
    {"name": "Tomlin's Troops", "wins": 3, "losses": 9, "points_for": 1255.84, "points_against": 1425.56, "head_to_head": {}}
]

# Hardcoded matchups for the next two weeks
matchups_week_13 = [
    ("Dawg Pound", "Seattle Sickos"),
    ("Trojan Army", "Raven Lunatics"),
    ("Deal Makers", "Diabeto Domination"),
    ("Henry", "Who here isn't eskimo bros"),
    ("Who's Your Daddy", "Lakeside Lions"),
    ("Jack the Gripper", "GoHoos"),
    ("PEPE CARTEL", "Tomlin's Troops")
]

matchups_week_14 = [
    ("Henry", "GoHoos"),
    ("Seattle Sickos", "Dawg Pound"),
    ("Raven Lunatics", "Who here isn't eskimo bros"),
    ("PEPE CARTEL", "Who's Your Daddy"),
    ("Lakeside Lions", "Diabeto Domination"),
    ("Jack the Gripper", "Deal Makers"),
    ("Tomlin's Troops", "Trojan Army")
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the matchups for both weeks
        for week, matchups in [('week_1', matchups_week_13), ('week_2', matchups_week_14)]:
            for idx, (team1, team2) in enumerate(matchups):
                winner_name = request.form[f'winner_{week}_{idx}']
                winner = next(team for team in teams if team['name'] == winner_name)
                loser = next(team for team in teams if team['name'] == (team1 if winner['name'] == team2 else team2))

                # Update the teams' wins and losses
                winner['wins'] += 1
                loser['losses'] += 1

                # Update head-to-head record
                if loser['name'] not in winner['head_to_head']:
                    winner['head_to_head'][loser['name']] = 0
                if winner['name'] not in loser['head_to_head']:
                    loser['head_to_head'][winner['name']] = 0

                winner['head_to_head'][loser['name']] += 1

        return redirect(url_for('index'))  # Refresh page with updated standings

    # Sort the teams based on wins, losses, and points_for
    sorted_teams = sorted(teams, key=lambda x: (-x['wins'], x['losses'], -x['points_for']))
    return render_template('index.html', teams=sorted_teams, matchups_week_13=matchups_week_13, matchups_week_14=matchups_week_14)

if __name__ == '__main__':
    app.run(debug=True)