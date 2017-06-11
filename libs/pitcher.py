class Pitcher(object):
	# TODO If Player gets too big, change player to have hitter, fielder and baserunner component classes '''
	def __init__(self, name, team, stats):
		''' inits pitcher from stats where
			"ERA" is Earned run average. The average number of earned 
			runs allowed multiplied by 9 and divided by innings pitched 
			"G" is games appeared in
			"GS" is games started
			"SV" saves
			"SVO" save oportunities, the number of times the pitcher closed the game
			"IP" Innings pitched: 1/3 inning per out
			"H" Hits allowed
			"R" Runs allowed
			"ER" Earned runs allowed
			"HR" Home runs allowed
			"BB" Walks
			"SO" Strike outs
			"AVG" Hits/opponent-at-bats
			"WHAP" (H+W)/IP
			"CG" complete games
			"SHO" Shut outs
			"HB" Hit batter
			"IBB" Intential walks
			"GF" Games finished/last relief pitcher
			"HLD" Holds, game in save situation but not last pitcher
			"GIDP" ground into double play
			"GO" Ground out
			"AO" Fly out
			"WP" wild pitches
			"BK" balks
			"SB" stolen bases allowed
			"CS" number of runners caught stealing
			"PK" number of pickoffs by the pitcher
			"TBF" total batters faced
			"NP" pitches thrown
		'''

		self.sample_space = {}
		self.stats = stats
		self.name = name
		self.team = team

	@classmethod 
	def pitcher_from_stat_lines(cls, stat_line1, stat_line2):
		''' create a player from a MLB stat line '''
		# modify this to handle last names with spaces (look for the comma)
		_, last, first, team, W, L, ERA, G, GS, SV, SVO, IP, H, R, ER, HR, BB, SO, AVG, WHIP = stat_line1.split()

		_, last2, first2, team2, CG, SHO, HB, IBB, GF, HLD, GIDP, GO, AO, WP, BK, SB, CS, PK, TBF, NP = stat_line2.split()

		if last != last2 or first != first2 or team != team2:
			raise ValueError("Stats not loading correctly {} vs {}".format(stat_line1, stat_line2))
		scope_locals = locals()
		stats = {i: float(scope_locals[i]) for i in (
				'W', 'L', 'ERA', 'G', 'GS', 'SV', 'SVO', 'IP',
				'H', 'R', 'ER', 'HR', 'BB', 'SO', 'AVG', 'WHIP',
				'CG', 'HB', 'IBB', 'GF', 'HLD', 'GIDP', 'GO', 'AO', 'WP', 'BK',
				'SB', 'CS', 'PK', 'TBF', 'NP'
		)}

		return Pitcher(last+" "+first, team, stats)

	def set_sample_space(self, league_triples_percent=0.024, league_doubles_percent=0.174):
		''' Calculates the probability a batter will get each outcome against this pitcher. 
			The data usually just gives us the total hits and HR's a pitcher allowed.
			However, we can use the multipliers to estimate doubles
			and triples from the total number of hits. These multipliers are 
			calculated from the data set's (year, league) rate at which these events occur
			league_triples_percent = total_triples / total_hits
			league_double_percent = league_double_percent / total_hits
		'''

		# probability of HR, triple, double, single and walk:

		H3B = self.stats["H"] * league_triples_percent
		H2B = self.stats["H"] * league_doubles_percent
		H1B = self.stats["H"]  - self.stats["HR"] - H3B - H2B

		stats = self.stats
		sac_bunt = stats['GO'] * leagues_sac_bunt_perc
		ground_outs = stats['GO'] - stats['GIDP'] * 2 - sac_bunt
		sac_fly = league_sac_perc * stats['AO']
		fly_out = stats['AO'] - sac_fly
		base_on_balls = stats['BB'] - stats['IBB']
		outcomes = self.stats["TBF"]


		self.sample_space = {
				'Walk: Base on balls': base_on_balls/outcomes,
				'Walk: Hit by pitch': stats['HB']/outcomes,
				'Walk: Intentional Walk':  stats["IBB"]/outcomes,
				'Out: SO': stats["SO"]/outcomes,
				'Out: Sac Bunt': sac_bunt/outcomes,
				'Out: Sac Fly': sac_fly/outcomes,
				'Out: Double Play' : stats['GIDP']/outcomes,
				'Out: Ground Out' : ground_outs/outcomes,
				'Out: Fly Out': fly_out/outcomes,
				'Single': H1B/outcomes,
				'Double':H2B/outcomes,
				'Triple': H3B/outcomes,
				'HR': stats["HR"]/outcomes
			}
