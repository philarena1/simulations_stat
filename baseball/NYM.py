from random import randint
import pandas as pd

def get_winner(team1,team2,prob):
	"""gets the winner between two, with 
	probability of team 1 winning/team 2 losing
	"""
	rand_num = float(randint(0,1000)/1000)
	print('prob: %s rand %s' % (str(prob), str(rand_num)) )
	if rand_num <= prob:
		winner = team1
	else:
		winner = team2

	return winner


def get_winner_df(row):
	"""gets the winner between two, with 
	probability of team 1 winning/team 2 losing
	"""
	team1 = row['team1']
	team2 = row['team2']
	prob =  row['prob']
	rand_num = float(randint(0,1000)/1000)
	print('prob: %s rand %s' % (str(prob), str(rand_num)) )
	if rand_num <= prob:
		winner = team1
	else:
		winner = team2

	return winner



data = [{'team1':'Marlins','team2':'Mets','date':'2019-09-23','prob':.25}]
games_df = pd.DataFrame(data)
print(games_df)


games_df['winner'] = games_df.apply(get_winner_df, axis=1)
print(games_df)