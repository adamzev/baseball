import random
import sys
import json
import copy

from .bases import Bases
import libs.baseball_func as b_func

HIT_TYPES = ['Single', 'Double', 'Triple', 'HR']

class Game(object):
    def __init__(self):
        self.bases = Bases()
        self.inning = 1
        self.top = True # false means bottom of the inning
        self.outs = 0
        self.score = {"home": 0, "away": 0}
        self.home_team = None
        self.away_team = None
        self.batting_team = "away"
        self.pitching_team = "home"

    def get_result_type(self, at_bat_result):
        return at_bat_result.split(":")[0].lower()

    def advance_runners(self, at_bat_result, new_runner):
        result_type = self.get_result_type(at_bat_result)
        runs_scored = 0
        ''' advance the runners '''
        if result_type == "walk":
            runs_scored += self.bases.forced_advance(new_runner)

        if at_bat_result == "ground_rule_double":
            runs_scored += self.bases.forced_advance(new_runner)
            runs_scored += self.bases.forced_advance(None)

        if at_bat_result == "Single":
            runs_scored += self.bases.advance_runners_keep_spacing(1, new_runner)

        if at_bat_result == "Double":
            runs_scored += self.bases.advance_runners_keep_spacing(2, new_runner)

        if at_bat_result == "Triple":
            runs_scored += self.bases.advance_runners_keep_spacing(3, new_runner)

        if at_bat_result == "HR":
            runs_scored += self.bases.advance_runners_keep_spacing(4, new_runner)
        
        return runs_scored

    def display_inning(self):
        if self.top:
            part = "Top"
        else:
            part = "Bottom"
        print("{} of the {} inning".format(part, self.inning))


    def reset_field(self):
        self.bases.clear_bases()
        self.outs = 0

    def is_tie(self):
        return self.score["home"] == self.score["away"]

    def log5_sample_space(self, batter_s, pitcher_s, league_s):
        ''' applied log5 to combine batter and pitcher sample spaces '''
        sample_space = {}
        for key, value in batter_s.items():
            sample_space[key] = b_func.log5(batter_s[key], pitcher_s[key], league_s[key])
        #should we need to normalize after applying log5?
        sample_space = self.normalize_sample_space(sample_space)
        total_prob = sum(sample_space.values())

        if round(total_prob, 3) != 1.0:
            raise ValueError("Sample space must total 1 not {}".format(total_prob))
        return sample_space

    @staticmethod
    def normalize_sample_space(sample_space_raw):
        total_prob = sum(sample_space_raw.values())
        sample_space_norm = {}
        for key, value in sample_space_raw.items():
            sample_space_norm[key] = value/total_prob
        return sample_space_norm

    def at_bat(self, batter, pitcher, league):
        ''' given the state of the bases, sims an at bat and returns the outcome '''

        sample_space = self.log5_sample_space(
            batter.sample_space, pitcher.sample_space, league.sample_space
        )
        bases = self.bases
        while True:
            rand_hit = random.random()
            total = 0
            invalid_outcome = False
            # TODO Change this so it modifies the sample space rather than run again
            for outcome, prob in sample_space.items():
                total += prob
                if rand_hit < total:
                    if outcome == "Walk: Intentional Walk" and bases.are_loaded():
                        invalid_outcome = True
                    elif outcome in ("Out: Double Play", "Out: Sac Bunt") and bases.are_empty():
                        invalid_outcome = True
                    elif outcome == "Out: Sac Fly" and bases.third is None:
                        invalid_outcome = True
                    if invalid_outcome:
                        return self.at_bat(batter, pitcher, league)
                    else:
                        return outcome

    def sim(self, home_team, away_team, league, verbose=False):
        game_json = {
            "home_team": home_team.name, 
            "away_team": away_team.name,
            "innings": [],
        }
        self.inning = 1

        # up to bat is the zero-based count of how many batters have been up to bat
        up_to_bat0 = {"home": 0, "away": 0}
        
        teams = {"away": away_team, "home": home_team}
        total_hits = {"home": 0, "away": 0}

        while self.inning <= 9 or self.is_tie():
            self.display_inning()
            inning_score = {"home": 0, "away": 0}
            for batting_team in ["away", "home"]:
                self.batting_team = batting_team
                self.pitching_team = "home" if batting_team == "away" else "away"
                runs_scored_in_inning = 0
                inning_details = []
                while self.outs < 3:
                    line_up_num = up_to_bat0[batting_team] % 9
                    player = teams[batting_team].batting_order[line_up_num]
                    pitcher = teams[self.pitching_team].starting_pitcher
                    result = self.at_bat(player, pitcher, league)
                    if result in HIT_TYPES:
                        total_hits[batting_team] += 1
                    result_type = self.get_result_type(result)
                    inning_detail = {
                        "bases": str(self.bases),
                        "batter": player.player_name,
                        "result": result
                    }
                    inning_details.append(inning_detail)
                    if verbose:
                        print(self.bases)
                        print("Now batting: {}".format(player.player_name))
                        print(result)
                    runs_scored_in_inning += self.advance_runners(result, player)
                    if result_type == "out":
                        self.outs += 1
                    if result == "Out: Double Play":
                        self.outs += 1  # one out has already been added
                    up_to_bat0[batting_team] += 1
                
                inning_score[self.batting_team] = runs_scored_in_inning
                self.score[self.batting_team] += runs_scored_in_inning
                self.reset_field()

            game_json["innings"].append(
                copy.deepcopy({
                    'inning': self.inning,
                    'score': inning_score,
                    'inning_details': inning_details
                })
            )
            self.inning += 1

        #print("Game over:\n Score\n {}".format(self.score))
        game_json["score"] = self.score
        game_json["hits"] = total_hits
        print(game_json)
        return game_json

