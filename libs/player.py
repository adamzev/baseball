import random
import sys

sys.path.append('/home/tutordelphia/www/')
import rocket.util.func as func

class Player(object):
	# TODO If Player gets too big, change player to have hitter, fielder and baserunner component classes '''
	def __init__(self, first, last, team, pos, stats):
		'''
			"team_name" is full pretty team name
			"team" is lower case two or three digit team abv
			"pos" is position
			"league" is NL for National and AL for American
			"bats" is batting handedness (S for switch, L or R)
			"g" is Games
			"ab" is At Bats
			"r" is runs
			"h" is hits
			"d" is doubles
			"t" is triples
			"hr" is homeruns
			"rbi" is runs batted in
			"bb" is walks
			"ibb" is intential walk
			"hbp" is hit by pitch
			"so" is strike outs
			"sb" is stolen bases
			"cs" is caught stealing
			"ppa" is pitches per plate apearence
			"avg" is average
			"obp" is on base perentage
			"slg" is slugging: TB/At bats
			"ops" is on base percentage plus slugging
			"sbptc" is stolen base percentage
			"ao" is fly out
			"go" is ground out
			"sf" is sac fly
			"sac" is sacrafice bunt
			"tpa" is total plate apearences
			"gidp" is ground into double play
		'''
		self.sample_space = {}
		self.stats = stats
		self.first = first
		self.last = last
		self.team = team
		self.pos = pos

	@property
	def player_name(self):
		return self.last + ', ' + self.first[0]

	@classmethod
	def player_from_json(cls, json_stats):
		stats = {}
		name = json_stats.pop('name_display_first_last', '')
		first = name.split()[0]
		last = json_stats.pop('last_name', '')
		team = json_stats.pop('team', '')
		pos = json_stats.pop('pos', '')

		for key, value in json_stats.items():
			if value in ['.---', '-.--', '*.**']:
				value = 0.0
			if func.is_float(value):
				stats[key] = float(value)
			else:
				stats[key] = value
		return Player(first, last, team, pos, stats)


	def set_sample_space(self):
		''' find the total outcomes and probability of each '''
		stats = self.stats
		singles = stats['h'] - stats['hr'] - stats['t'] - stats['d']
		ground_outs = stats['go'] - stats['gidp'] * 2 - stats['sac']
		fly_out = stats['ao'] - stats['sf']
		base_on_balls = stats['bb'] - stats['ibb']
		outcomes = base_on_balls + stats['hbp'] + stats['so'] + \
			stats['ibb'] + stats['sac'] + stats['sf'] + \
			stats['gidp'] + ground_outs + fly_out + \
			stats['hr'] + stats['t'] + stats['d'] + singles

		self.sample_space = {
				'Walk: Base on balls': base_on_balls/outcomes,
				'Walk: Hit by pitch': stats['hbp']/outcomes,
				'Walk: Intentional Walk':  stats["ibb"]/outcomes,
				'Out: SO': stats["so"]/outcomes,
				'Out: Sac Bunt': stats['sac']/outcomes,
				'Out: Sac Fly': stats['sf']/outcomes,
				'Out: Double Play' : stats['gidp']/outcomes,
				'Out: Ground Out' : ground_outs/outcomes,
				'Out: Fly Out': fly_out/outcomes,
				'Single': singles/outcomes,
				'Double': stats["d"]/outcomes,
				'Triple': stats["t"]/outcomes,
				'HR': stats["hr"]/outcomes
			}
		total_prob = sum(self.sample_space.values())
		if round(total_prob, 3) != 1.0:
			raise ValueError("Sample space must total 1 not {}".format(total_prob))
		message = "{} Outcomes {} should equal plate appearances {}".format(self.player_name, outcomes, stats['tpa'])
		if outcomes != stats['tpa']:
			#raise ValueError(message)
			print(message)

