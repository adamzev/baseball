from libs.game import Game
from libs.team import Team
from libs.league import League
import libs.generalEquations as ge

def run_sim(team1, team2, num_games):
    home_scores = []
    home_wins = 0
    away_wins = 0
    away_scores = []
    league = League()
    home = Team(team1)  # Phillies #phi
    away = Team(team2)  # Marlins #mia

    for each_team in [home, away]:
        each_team.set_sample_space(league)
        each_team.set_starting_line_up()
        each_team.set_starting_pitcher()
    for _ in range(num_games):
        bb_game = Game()
        home_score, away_score = bb_game.sim(home, away, league, True)
        home_scores.append(home_score)
        away_scores.append(away_score)

        if home_score == away_score:
            raise ValueError("No ties allowed")
        elif home_score > away_score:
            home_wins += 1
        else:
            away_wins += 1

    print(home_scores)

    return {
        "home":"{}: {} AVG Runs, {} wins ".format(home.name, "{0:.4f}".format(ge.average_list(home_scores)), home_wins),
        "away":"{}: {} AVG Runs, {} wins ".format(away.name, "{0:.4f}".format(ge.average_list(away_scores)), away_wins)
    }
