import sys

sys.path.append('/home/tutordelphia/www/')
from baseball.libs.player import Player

from rocket.libs.query import Query as q

import rocket.libs.fileManager as fileMan
class Team(object):
	def __init__(self, name):
		self.players = []
		self.name = name
		self.load_players_from_files(name)
		self.batting_order = []
		self.set_starting_line_up()
		

	def load_players_from_files(self, prefix):
		file_name = "data/"+prefix+ "_stat_lines.txt"
		file_name_2 = "data/" + prefix+ "_stat_lines2.txt"
		with open(file_name, 'r') as stat_lines, open(file_name_2) as stat_lines_2:
			for part_a, part_b in zip(stat_lines, stat_lines_2):
				part_a = self.clean_str(part_a)
				part_b = self.clean_str(part_b)

				player = Player.player_from_stat_lines(part_a, part_b)
				if player.stats["PA"] > 0:
					self.players.append(player)
					player.set_sample_space()

	def clean_str(self, dirty):
		''' sanatize baseball stat files from MLB.com '''
		dirty = dirty.replace('.---', '0.0')
		dirty = dirty.replace('-.--', '0.0')
		clean = dirty.replace('*.**', '0.0')

		return clean

	def set_starting_line_up(self):
		file_name = "data/"+self.name+"_"+"starting"
		try:
			lineup = fileMan.load_json(file_name+".json")
			if len(lineup) != 9:
				raise ValueError("Starting lineup must be 9 players")
			self.batting_order = [player for player in self.players if player.name in lineup]
		except OSError:
			q.change_input_func(input)
			lineup = []
			while len(lineup) < 9:
				lineup.append(q.query_from_list("player", "Select the starting line-up in order: ", [player.name for player in self.players], False))
			self.batting_order = [player for player in self.players if player.name in lineup]
			fileMan.save_json([player.name for player in self.batting_order], file_name)


