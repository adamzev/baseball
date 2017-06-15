import sys

sys.path.append('/home/tutordelphia/www/')

from baseball.libs.team import Team

class League(object):
	def __init__(self):
		self.players = all_players = Team("all")
		H = 0
		H2B = 0
		H3B = 0
		HR = 0
		sac_bunt = 0
		sac_fly = 0
		GO = 0
		AO = 0
		GDP = 0
		TPA = 0
		BB = 0
		singles = 0
		ground_outs = 0
		fly_out = 0
		base_on_balls = 0
		outcomes = 0
		HBP = 0
		IBB = 0
		GIDP = 0
		SO = 0

		for player in all_players.players:
			TPA += player.stats['tpa']
			H += player.stats["h"]
			H2B += player.stats["d"]
			H3B += player.stats["t"]
			HR += player.stats["hr"]
			sac_bunt += player.stats["sac"]
			sac_fly += player.stats["sf"]
			GO += player.stats["go"]
			AO += player.stats["ao"]
			BB += player.stats["bb"]
			GDP += player.stats["gdp"]
			HBP += player.stats['hbp']
			IBB += player.stats['ibb']
			SO += player.stats['so']
			GIDP += player.stats['gidp']

			stats = player.stats
			singles += stats['h'] - stats['hr'] - stats['t'] - stats['d']
			ground_outs += stats['go'] - stats['gidp'] * 2 - stats['sac']
			fly_out += stats['ao'] - stats['sf']
			base_on_balls += stats['bb'] - stats['ibb']
			outcomes += stats['tpa']

		self.sample_space = {
			'Walk: Base on balls': base_on_balls/outcomes,
			'Walk: Hit by pitch': HBP/outcomes,
			'Walk: Intentional Walk':  IBB/outcomes,
			'Out: SO': SO/outcomes,
			'Out: Sac Bunt': sac_bunt/outcomes,
			'Out: Sac Fly': sac_fly/outcomes,
			'Out: Double Play' : GIDP/outcomes,
			'Out: Ground Out' : ground_outs/outcomes,
			'Out: Fly Out': fly_out/outcomes,
			'Single': singles/outcomes,
			'Double': H2B/outcomes,
			'Triple': H3B/outcomes,
			'HR': HR/outcomes
		}
		print(self.sample_space)
		total_prob = sum(self.sample_space.values())
		if round(total_prob, 3) != 1.0:
			raise ValueError("Sample space must total 1 not {}".format(total_prob))

		print("H: {} H2B: {} H3B: {}, HR: {} sac_bunt: {} sac_fly: {} GO: {} AO: {} GDP: {} BB: {}".format(H, H2B, H3B, HR, sac_bunt, sac_fly, GO, AO, GDP, BB))
		print("H: {} H2B: {} H3B: {}, HR: {} sac_bunt: {} sac_fly: {} GO: {} AO: {} GDP: {}, BB: {}".format(H/TPA, H2B/TPA, H3B/TPA, HR/TPA, sac_bunt/TPA, sac_fly/TPA, GO/TPA, AO/TPA, GDP/TPA, BB/TPA))
