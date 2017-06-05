class Pitcher(object):
	# TODO If Player gets too big, change player to have hitter, fielder and baserunner component classes '''
	def __init__(self, name, team, pos, stats):
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
		self.pos = pos

	@classmethod 
	def pitcher_from_stat_lines(cls, stat_line1, stat_line2):
		''' create a player from a MLB stat line '''
		# modify this to handle last names with spaces (look for the comma)
		_, last, first, team, pos, G, AB, R, H, H2B, H3B, HR, RBI, BB, SO, SB, CS, AVG, OBP, SLG, OPS = stat_line1.split()

		_, _, _, _, _, IBB, HBP, SAC, SF, TB, XBH, GDP, GO, AO, GO_AO, NP, PA = stat_line2.split()
		scope_locals = locals()
		stats = {i: float(scope_locals[i]) for i in (
				'G', 'AB', 'R', 'H', 'H2B', 'H3B', 'HR', 'RBI',
				'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS',
				'IBB', 'HBP', 'SAC', 'SF', 'TB', 'XBH', 'GDP', 'GO', 'AO', 'GO_AO', 'NP', 'PA'
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
		P4 = self.stats["HR"] / self.stats["TBF"]
		P3 = self.stats["H"] * league_triples_percent / self.stats["TBF"]
		P2 = self.stats["H"] * league_doubles_percent / self.stats["TBF"]
		P1 = self.stats["H"] / self.stats["TBF"] -P4 - P3 - P2
		PBB = self.stats["BB"] / self.stats["TBF"]