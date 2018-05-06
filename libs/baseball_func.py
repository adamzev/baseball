def log5(bat_avg, pitch_avg, league_avg):
    ''' computs the probability a batter will succeed based on the log5 method '''
    avg_div_league = bat_avg * pitch_avg / league_avg
    return avg_div_league / (avg_div_league + (1 - bat_avg) * (1 - pitch_avg) / (1 - league_avg))
