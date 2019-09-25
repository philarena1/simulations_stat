import itertools

games = [
#{'team1':'Mets','team2':'Marlins','date':'2019-09-24'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-25'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-26'},
{'team1':'Mets','team2':'Braves','date':'2019-09-27'},
{'team1':'Mets','team2':'Braves','date':'2019-09-28'},
{'team1':'Mets','team2':'Braves','date':'2019-09-29'},

#{'team1':'Cubs','team2':'Pirates','date':'2019-09-24'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-25'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-26'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-27'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-28'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-29'},

#{'team1':'Brewers','team2':'Reds','date':'2019-09-24'},
{'team1':'Brewers','team2':'Reds','date':'2019-09-25'},
{'team1':'Brewers','team2':'Reds','date':'2019-09-26'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-27'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-28'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-29'},


#{'team1':'Nationals','team2':'Phillies','date':'2019-09-24-0'},
#{'team1':'Nationals','team2':'Phillies','date':'2019-09-24-1'},
{'team1':'Nationals','team2':'Phillies','date':'2019-09-25'},
{'team1':'Nationals','team2':'Phillies','date':'2019-09-26'},
{'team1':'Nationals','team2':'Indians','date':'2019-09-27'},
{'team1':'Nationals','team2':'Indians','date':'2019-09-28'},
{'team1':'Nationals','team2':'Indians','date':'2019-09-29'}

]



#https://stackoverflow.com/questions/54962794/generating-possible-combinations-of-a-given-list-of-games-in-python



current_wins = {'Mets': 81, 
'Cubs': 74, 
'Brewers':86 , 
'Nationals':87}


import itertools



def simulate_season(games):
	game_list = [game['team1'] + ' - '+ game['team2'] + ' - '+ game['date'] for game in games ]

	games = game_list
	case = ["W","L"]

	results = []
	for i in itertools.product(case, repeat = len(games)):
	    results.append({k:v for k, v in zip(games, i)})


	print(len(results))

	print('\n')
	print(results[-1])

	return results

def wins_per_team(universe,contending_teams):
    wins = []
    for game in universe:
        team = (game.split('-')[0]).strip()
        outcome = universe[game]

        for t in contending_teams:
            if t == team and outcome == 'W':
                wins.append(t)

    wins_per = {}
    for win in wins:
        wins_per[win] = wins.count(win)

    return wins_per

results = simulate_season(games)

contending_teams = ['Mets','Cubs','Brewers','Nationals']
winnng_universe = 0
losing_universe = 0
season_winning = []

for game in results:
    win_per = (wins_per_team(game,contending_teams))
    season = {}
    for team in win_per:
        season[team] = (current_wins[team] + win_per[team])
    season_winning.append(season)
    top_2 = sorted(season, key=season.get, reverse=True)[:2]
    if 'Mets' in top_2:
        print('win')
        winnng_universe += 1

    else:
        print('lose')
        losing_universe += 1

total_uni = winnng_universe + losing_universe
print('Out of %s total universes \n' % str(total_uni))
print('The Mets will lose in %s \n' % str(losing_universe))
print('And the Mets will win in %s \n' % str(winnng_universe))



