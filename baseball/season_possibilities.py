import itertools

games = [{'team1':'Mets','team2':'Marlins','date':'2019-09-23'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-24'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-25'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-26'},
{'team1':'Mets','team2':'Braves','date':'2019-09-27'},
{'team1':'Mets','team2':'Braves','date':'2019-09-28'},
{'team1':'Mets','team2':'Braves','date':'2019-09-29'},

{'team1':'Cubs','team2':'Pirates','date':'2019-09-24'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-25'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-26'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-27'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-28'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-29'},

{'team1':'Brewers','team2':'Reds','date':'2019-09-24'},
{'team1':'Brewers','team2':'Reds','date':'2019-09-25'},
{'team1':'Brewers','team2':'Reds','date':'2019-09-26'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-27'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-28'},
{'team1':'Brewers','team2':'Rockies','date':'2019-09-29'},


# {'team1':'Nationals','team2':'Phillies','date':'2019-09-24-0'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-24-1'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-25'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-26'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-27'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-28'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-29'}

]


game_list = [game['team1'] + ' - '+ game['team2'] + ' - '+ game['date'] for game in games ]

#https://stackoverflow.com/questions/54962794/generating-possible-combinations-of-a-given-list-of-games-in-python

import itertools
games = game_list
case = ["W","L"]

results = []
for i in itertools.product(case, repeat = len(games)):
    results.append({k:v for k, v in zip(games, i)})

#print(results)
print(len(results))

print('\n')
print(results[-1])


