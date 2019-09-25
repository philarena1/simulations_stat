import itertools

games = [[{'team1':'Mets','team2':'Marlins','date':'2019-09-23'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-24'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-25'},
{'team1':'Mets','team2':'Marlins','date':'2019-09-26'},
{'team1':'Mets','team2':'Braves','date':'2019-09-27'},
{'team1':'Mets','team2':'Braves','date':'2019-09-28'},
{'team1':'Mets','team2':'Braves','date':'2019-09-29'}],

[{'team1':'Cubs','team2':'Pirates','date':'2019-09-24'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-25'},
{'team1':'Cubs','team2':'Pirates','date':'2019-09-26'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-27'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-28'},
{'team1':'Cubs','team2':'Cardinals','date':'2019-09-29'}],

# [{'team1':'Brewers','team2':'Reds','date':'2019-09-24'},
# {'team1':'Brewers','team2':'Reds','date':'2019-09-25'},
# {'team1':'Brewers','team2':'Reds','date':'2019-09-26'},
# {'team1':'Brewers','team2':'Rockies','date':'2019-09-27'},
# {'team1':'Brewers','team2':'Rockies','date':'2019-09-28'},
# {'team1':'Brewers','team2':'Rockies','date':'2019-09-29'}],


# [{'team1':'Nationals','team2':'Phillies','date':'2019-09-24-0'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-24-1'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-25'},
# {'team1':'Nationals','team2':'Phillies','date':'2019-09-26'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-27'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-28'},
# {'team1':'Nationals','team2':'Indians','date':'2019-09-29'}]

]

for series in games:
	print(series[0])
	#game_list = [series['team1'] + ' - '+ series['team2'] + ' - '+ series['date'] for series in games ]



