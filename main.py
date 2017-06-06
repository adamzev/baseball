import sys

sys.path.append('/home/tutordelphia/www/')

from libs.game import Game
from libs.team import Team
import rocket.generalEquations as ge

def main():
	home_scores = []
	home_wins = 0
	away_wins = 0
	away_scores = []
	home = Team("phil")
	away = Team("marlins")
	for _ in range(1):
		bb_game = Game()
		home_score, away_score = bb_game.sim(home, away)
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
