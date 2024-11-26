from flask import Flask, render_template, request, redirect, url_for
from teams import teams, matchups_week_13, matchups_week_14  # Import teams and matchups

app = Flask(__name__)

# Tie-breaking function
def compare_teams(team1, team2):
    # First tie-breaker: head-to-head result
    if team2['name'] in team1['head_to_head'] and team1['name'] in team2['head_to_head']:
        if team1['head_to_head'][team2['name']] > team2['head_to_head'][team1['name']]:
            return -1  # team1 wins head-to-head, so it should come first
        elif team1['head_to_head'][team2['name']] < team2['head_to_head'][team1['name']]:
            return 1  # team2 wins head-to-head, so it should come first
    
    # Second tie-breaker: points-for (PF)
    if team1['points_for'] > team2['points_for']:
        return -1
    elif team1['points_for'] < team2['points_for']:
        return 1
    
    # If both tie-breakers are the same, rank them as equal
    return 0

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