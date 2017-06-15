import sys

sys.path.append('/home/tutordelphia/www/')

from baseball.libs.game import Game
from baseball.libs.team import Team
from baseball.libs.league import League
import rocket.generalEquations as ge

def main():
	home_scores = []
	home_wins = 0
	away_wins = 0
	away_scores = []
	league = League()
	home = Team("phi") # Phillies
	away = Team("mia") # Marlins

	for each_team in [home, away]:
		each_team.set_sample_space(league)
		each_team.set_starting_line_up()
		each_team.set_starting_pitcher()
	for _ in range(100):
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

	print("{}: {} AVG Runs, {} wins ".format(home.name, ge.average_list(home_scores), home_wins))
	print("{}: {} AVG Runs, {} wins ".format(away.name, ge.average_list(away_scores), away_wins))



if __name__ == "__main__":
	main()
