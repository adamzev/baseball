import sys
import requests

import libs.fileManager as fileMan

def create_url(sort_column, sort_dir, season):
	''' Creates a MLB.com API url
	API breakdown
	string fields have single quotes (encoded at %27)

	base_url: 
		http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?
	
	season:
		4 digit year: 1876 to current year
	sort_order:
		'asc' or 'desc'
	sort_column:
		such as 'era' or any json column name
			need further details/restrictions
	stat_type:
		pitching, hitting or fielding(no quotes)
	page_type:
		'SortablePlayer'
	game_type:
		'R' is regular season
	player_pool:
		ALL no quotes for all players
		something like Q or Qualifing for only players who regularly apear in games
	season_type:
		ANY
	sport_code:
		'mlb'
	results:
		1000 number of results
	recPP:
		50 records per page

	'''
	api_url = "http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?"
	api_url += "season="+str(season)

#Avialble players and salaries on draftkings
#https://www.draftkings.com/lineup/getavailableplayers?draftGroupId=13953
# probable starters: need to beautiful soup it:
#https://rotogrinders.com/lineups/mlb?site=draftkings

# pitcher info
#http://mlb.mlb.com/lookup/xml/named.sit_pitcher_date.bam?player_id=453286&sport_code=%27mlb%27&season=2017&game_type=%27F%27&game_type=%27D%27&game_type=%27L%27&game_type=%27W%27&date_num=%272017/06/16%27&vs_team_id=121
#http://mlb.mlb.com/ticketing-client/xml/Game.tiksrv?team_id=108&begin_date=20170616&end_date=20170620&site_section=%27DEFAULT%27
urls = {
	"mlb_pitcher_data":
		"http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2017&sort_order=%27asc%27&sort_column=%27era%27&stat_type=pitching&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=5000&position=%271%27&recSP=1&recPP=5000",
	"mlb_batter_data":
		"http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2017&sort_order=%27desc%27&sort_column=%27avg%27&stat_type=hitting&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=5000&recSP=1&recPP=5000",
	"mlb_fielding_data":
		"http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2017&sort_order=%27desc%27&sort_column=%27fpct%27&stat_type=fielding&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=5000&recSP=1&recPP=5000"
}

for file_name, url in urls.items():
	r = requests.get(url)
	r.raise_for_status()
	fileMan.save_json(r.json(), 'data/'+file_name)
