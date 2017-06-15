import sys

sys.path.append('/home/tutordelphia/www/')
import rocket.util.func as func

class Pitcher(object):
	def __init__(self, first, last, team, stats):

		''' inits pitcher from stats where
			"era" is Earned run average. The average number of earned
			runs allowed multiplied by 9 and divided by innings pitched
			"g" is games appeared in
			"gs" is games started
			"ir" is inherited runnters
			"irs" is inherited runners scored
			"throws" is throws "R" or "L"
			"sv" saves
			"svo" save oportunities, the number of times the pitcher closed the game
			"ip" Innings pitched: 1/3 inning per out
			"h" Hits allowed
			"r" Runs allowed
			"er" Earned runs allowed
			"hr" Home runs allowed
			"bb" Walks
			"so" Strike outs
			"avg" Hits/opponent-at-bats
			"whip" (H+W)/IP
			"cg" complete games
			"sho" Shut outs
			"hb" Hit batter
			"ibb" Intential walks
			"gf" Games finished/last relief pitcher
			"hld" Holds, game in save situation but not last pitcher
			"gidp" ground into double play
			"go" Ground out
			"ao" Fly out
			"wp" wild pitches
			"bk" balks
			"sb" stolen bases allowed
			"cs" number of runners caught stealing
			"pk" number of pickoffs by the pitcher
			"tbf" total batters faced
			"np" pitches thrown
		'''

		self.sample_space = {}
		self.stats = stats
		self.first = first
		self.last = last
		self.team = team

	@classmethod
	def player_from_json(cls, json_stats):
		stats = {}
		name = json_stats.pop('name_display_first_last', '')
		first = name.split()[0]
		last = json_stats.pop('last_name', '')
		team = json_stats.pop('team', '')

		for key, value in json_stats.items():
			if value in ['.---', '-.--', '*.**']:
				value = 0.0
			if func.is_float(value):
				stats[key] = float(value)
			else:
				stats[key] = value
		return Pitcher(first, last, team, stats)


	@property
	def player_name(self):
		return self.last + ', ' + self.first[0]

	def set_sample_space(self, league):
		''' Calculates the probability a batter will get each outcome against this pitcher. 
			The data usually just gives us the total hits and HR's a pitcher allowed.
			However, we can use the multipliers to estimate doubles
			and triples from the total number of hits. These multipliers are 
			calculated from the data set's (year, league) rate at which these events occur
			league_triples_percent = total_triples / total_hits
			league_double_percent = league_double_percent / total_hits
		'''

		# probability of HR, triple, double, single and walk:

		H3B = self.stats["h"] * league.sample_space["Triple"]
		H2B = self.stats["h"] * league.sample_space["Double"]
		H1B = self.stats["h"]  - self.stats["hr"] - H3B - H2B

		stats = self.stats
		sac_bunt = stats['go'] * league.sample_space["Out: Ground Out"]
		ground_outs = stats['go'] - stats['gidp'] * 2 - sac_bunt
		sac_fly = league.sample_space["Out: Sac Fly"] * stats['ao']
		fly_out = stats['ao'] - sac_fly
		base_on_balls = stats['bb'] - stats['ibb']
		outcomes = self.stats["tbf"]


		self.sample_space = {
				'Walk: Base on balls': base_on_balls/outcomes,
				'Walk: Hit by pitch': stats['hb']/outcomes,
				'Walk: Intentional Walk':  stats["ibb"]/outcomes,
				'Out: SO': stats["so"]/outcomes,
				'Out: Sac Bunt': sac_bunt/outcomes,
				'Out: Sac Fly': sac_fly/outcomes,
				'Out: Double Play' : stats['gidp']/outcomes,
				'Out: Ground Out' : ground_outs/outcomes,
				'Out: Fly Out': fly_out/outcomes,
				'Single': H1B/outcomes,
				'Double':H2B/outcomes,
				'Triple': H3B/outcomes,
				'HR': stats["hr"]/outcomes
			}
