import random

class Player(object):
	# TODO If Player gets too big, change player to have hitter, fielder and baserunner component classes '''
	def __init__(self, name, team, pos, stats):
		''' inits a player from stats where
			"G" is Games
			"AB" is At Bats
			"R" is runs
			"H" is hits
			"b2B" is doubles
			"b3B" is triples
			"HR" is homeruns
			"RBI" is runs batted in
			"BB" is walks
			"SO" is strike outs
			"SB" is stolen bases
			"CS" is caught stealing
			"AVG" is average
			"OBP" is on base perentage
			"SLG" is slugging: TB/At bats
			"OPS" is on base percentage plus slugging
		'''
		self.sample_space = {}
		self.stats = stats
		self.name = name
		self.team = team
		self.pos = pos

	@classmethod 
	def player_from_stat_lines(cls, stat_line1, stat_line2):
		''' create a player from a MLB stat line '''
		# modify this to handle last names with spaces (look for the comma)
		try:
			_, last, first, team, pos, G, AB, R, H, H2B, H3B, HR, RBI, BB, SO, SB, CS, AVG, OBP, SLG, OPS = stat_line1.split()
			_, last2, first2, team2, _, IBB, HBP, SAC, SF, TB, XBH, GDP, GO, AO, GO_AO, NP, PA = stat_line2.split()
		except ValueError:
			print(stat_line1)
			print(stat_line2)
			raise
		scope_locals = locals()
		stats = {i: float(scope_locals[i]) for i in (
				'G', 'AB', 'R', 'H', 'H2B', 'H3B', 'HR', 'RBI',
				'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS',
				'IBB', 'HBP', 'SAC', 'SF', 'TB', 'XBH', 'GDP', 'GO', 'AO', 'GO_AO', 'NP', 'PA'
		)}
		if last != last2 or first != first2 or team != team2:
			raise ValueError("Stats not loading correctly {} vs {}".format(stat_line1, stat_line2))
		return Player(last+" "+first, team, pos, stats)

	def set_sample_space(self):
		''' find the total outcomes and probability of each '''
		stats = self.stats
		singles = stats['H'] - stats['HR'] - stats['H3B'] - stats['H2B']
		ground_outs = stats['GO'] - stats['GDP'] * 2 - stats['SAC']
		fly_out = stats['AO'] - stats['SF']
		base_on_balls = stats['BB'] - stats['IBB']
		outcomes = base_on_balls + stats['HBP'] + stats['SO'] + stats['IBB'] + stats['SAC'] + \
			stats['SF'] + stats['GDP'] + ground_outs + fly_out + \
			stats['HR'] + stats['H3B'] + stats['H2B'] + singles

		self.sample_space = {
				'Walk: Base on balls': base_on_balls/outcomes,
				'Walk: Hit by pitch': stats['HBP']/outcomes,
				'Walk: Intentional Walk':  stats["IBB"]/outcomes,
				'Out: SO': stats["SO"]/outcomes,
				'Out: Sac Bunt': stats['SAC']/outcomes,
				'Out: Sac Fly': stats['SF']/outcomes,
				'Out: Double Play' : stats['GDP']/outcomes,
				'Out: Ground Out' : ground_outs/outcomes,
				'Out: Fly Out': fly_out/outcomes,
				'Single': singles/outcomes,
				'Double': stats["H2B"]/outcomes,
				'Triple': stats["H3B"]/outcomes,
				'HR': stats["HR"]/outcomes
			}
		total_prob = sum(self.sample_space.values())
		if round(total_prob, 3) != 1.0:
			raise ValueError("Sample space must total 1 not {}".format(total_prob))
		message = "{} Outcomes {} should equal plate appearances {}".format(self.name, outcomes, stats['PA'])
		if outcomes != stats['PA']:
			#raise ValueError(message)
			print(message)

	def at_bat(self, bases):
		''' given the state of the bases, sims an at bat and returns the outcome '''
		while True:
			rand_hit = random.random()
			total = 0
			invalid_outcome = False
			# TODO Change this so it modifies the sample space rather than run again
			for outcome, prob in self.sample_space.items():
				total += prob
				if rand_hit < total:
					if outcome == "Walk: Intentional Walk" and bases.are_loaded():
						invalid_outcome = True
					elif outcome in ("Out: Double Play", "Out: Sac Bunt") and bases.are_empty():
						invalid_outcome = True
					elif outcome == "Out: Sac Fly" and bases.third is None:
						invalid_outcome = True
					if invalid_outcome:
						return self.at_bat(bases)
					else:
						return outcome
