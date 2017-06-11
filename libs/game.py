import random
import sys

sys.path.append('/home/tutordelphia/www/')
from baseball.libs.bases import Bases

class Game(object):
	def __init__(self):
		self.bases = Bases()
		self.inning = 1
		self.top = True # false means bottom of the inning
		self.outs = 0
		self.score = {"home": 0, "away": 0}
		self.home_team = None
		self.away_team = None
		self.at_bat = "away"

	def get_result_type(self, at_bat_result):
		return at_bat_result.split(":")[0].lower()

	def advance_runners(self, at_bat_result, new_runner):
		result_type = self.get_result_type(at_bat_result)
		''' advance the runners '''
		if result_type == "walk":
			self.score[self.at_bat] += self.bases.forced_advance(new_runner)

		if at_bat_result == "ground_rule_double":
			self.score[self.at_bat] += self.bases.forced_advance(new_runner)
			self.score[self.at_bat] += self.bases.forced_advance(None)

		if at_bat_result == "Single":
			self.score[self.at_bat] += self.bases.advance_runners_keep_spacing(1, new_runner)

		if at_bat_result == "Double":
			self.score[self.at_bat] += self.bases.advance_runners_keep_spacing(2, new_runner)

		if at_bat_result == "Triple":
			self.score[self.at_bat] += self.bases.advance_runners_keep_spacing(3, new_runner)

		if at_bat_result == "HR":
			self.score[self.at_bat] += self.bases.advance_runners_keep_spacing(4, new_runner)

	def display_inning(self):
		if self.top:
			part = "Top"
		else:
			part = "Bottom"
		print("{} of the {} inning".format(part, self.inning))


	def reset_field(self):
		self.bases.clear_bases()
		self.outs = 0

	def is_tie(self):
		return self.score["home"] == self.score["away"]

	def sim(self, home_team, away_team):

		self.inning = 1
		batter_numbers = {"home": 0, "away": 0}
		teams = {"away": away_team, "home": home_team}
		while self.inning <= 9 or self.is_tie():
			self.display_inning()
			for at_bat in ["away", "home"]:
				self.at_bat = at_bat
				while self.outs < 3:
					line_up_num = batter_numbers[at_bat] % 9
					player = teams[at_bat].batting_order[line_up_num]
					print(self.bases)
					print("Now batting: {}".format(player.name))
					result = player.at_bat(self.bases)
					result_type = self.get_result_type(result)
					print(result)
					self.advance_runners(result, player)
					if result_type == "out":
						self.outs += 1
					if result == "Out: Double Play":
						self.outs += 1 # one out has already been added
					batter_numbers[at_bat] += 1
				self.reset_field()
			self.inning += 1
		#print("Game over:\n Score\n {}".format(self.score))
		return self.score["home"], self.score["away"]

