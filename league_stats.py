import sys

sys.path.append('/home/tutordelphia/www/')

from libs.team import Team

all_players = Team("all")

H = 0
H2B = 0
H3B = 0
HR = 0
sac_bunt = 0
sac_fly = 0
GO = 0
AO = 0
GDP = 0
for player in all_players.players:
	H += player.stats["H"]
	H2B += player.stats["H2B"]
	H3B += player.stats["H3B"]
	HR += player.stats["HR"]
	sac_bunt += player.stats["SAC"]
	sac_fly += player.stats["SF"]
	GO += player.stats["GO"]
	AO += player.stats["AO"]
	GDP += player.stats["GDP"]

print("H: {} H2B: {} H3B: {}, HR: {} sac_bunt; {} sac_fly: {} GO: {} AO: {} GDP; {}".format(H, H2B, H3B, HR, sac_bunt, sac_fly, GO, AO, GDP))
