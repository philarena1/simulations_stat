from random import randint


def roll_dice():
	die = randint(1,6)
	return die 

def simulate_rolls(simnum):
	die_results = []
	for i in range(simnum):
		die = randint(1,6)
		die_results.append(die)	
	return die_results

# get distribution
def get_dist(results):
	die_dist = {}
	for num in results:
		die_dist[num] = results.count(num)
	return die_dist

def get_odds(simnum,distribution):
	prob = {}
	for die in distribution:
		result = distribution[die]
		prob[die] = result/float(simnum)
	return prob



sim_num = 10000
results = simulate_rolls(sim_num)
die_dist = get_dist(results)
print(die_dist)
probability = get_odds(sim_num,die_dist)
print(probability)