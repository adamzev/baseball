import sys

sys.path.append('/home/tutordelphia/www/')
from baseball.libs.player import Player
from baseball.libs.pitcher import Pitcher
from rocket.libs.query import Query as q
import rocket.libs.fileManager as fileMan

import rocket.libs.fileManager as fileMan
class Team(object):
	def __init__(self, name):
		self.players = []
		self.batting_order = []
		self.pitchers = []
		self.starting_pitcher = None
		self.name = name
		self.load_players_from_files(name)


	def set_starting_pitcher(self):
		for player in self.batting_order:
			if player.pos == "P":
				self.starting_pitcher = self.find_pitcher(player.stats['player_id'])
				break
		else:
			raise ValueError("Starting pitcher not found")


	def find_pitcher(self, player_id):
		for pitcher in self.pitchers:
			if pitcher.stats['player_id'] == player_id:
				return pitcher

	def set_sample_space(self, league):
		for pitcher in self.pitchers:
			pitcher.set_sample_space(league)
		for batter in self.players:
			batter.set_sample_space()

	def load_batters(self, team_initials):
		file_name = "data/mlb_batter_data.json"

		json_data = fileMan.load_json(file_name)

		rows = json_data["stats_sortable_player"]["queryResults"]["row"]
		for row in rows:
			player = Player.player_from_json(row)
			if player.stats["tpa"] > 0 and (player.team == team_initials or team_initials == "all"):
				self.players.append(player)

	def load_pitchers(self, team_initials):
		''' loads pitchers from files
			"team_initials" is the two or three letter abrev. for the team, "all" for all
		'''
		file_name = "data/mlb_pitcher_data.json"

		json_data = fileMan.load_json(file_name)

		rows = json_data["stats_sortable_player"]["queryResults"]["row"]
		for row in rows:
			pitcher = Pitcher.player_from_json(row)
			self.pitchers.append(pitcher)

	def load_players_from_files(self, team_initials):
		''' loads players from files
			"team_initials" is the two or three letter abrev. for the team, "all" for all
		'''

		self.load_batters(team_initials)
		self.load_pitchers(team_initials)


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
			self.batting_order = [player for player in self.players if player.player_name in lineup]
		except OSError:
			q.change_input_func(input)
			lineup = []
			while len(lineup) < 9:
				lineup.append(q.query_from_list("player", "Select the starting line-up in order: ", [player.name for player in self.players], False))
			self.batting_order = [player for player in self.players if player.player_name in lineup]
			fileMan.save_json([player.player_name for player in self.batting_order], file_name)


