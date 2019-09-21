from random import randint
from statistical import get_dist, get_odds

def roll_dice():
	die = randint(1,6)
	
	return die 

def simulate_rolls(simnum):
	die_results = []
	
	for i in range(simnum):
		die = randint(1,6)
		die_results.append(die)	
	
	return die_results


sim_num = 10000
results = simulate_rolls(sim_num)
die_dist = get_dist(results)
print(die_dist)
probability = get_odds(sim_num,die_dist)
print(probability)