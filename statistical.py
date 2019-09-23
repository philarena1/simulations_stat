# get distribution
def get_dist(results):
	"""
	function gets the frequency of occurance for each item in a list
	"""
	dist = {}
	
	for num in results:
		dist[num] = results.count(num)
	
	return dist

def get_odds(simnum,distribution):
	"""
	function gets the probability of each item appearing in a list
	accepts num of simulations and the distribution
	"""
	prob = {}
	
	for record in distribution:
		result = distribution[record]
		prob[record] = result/float(simnum)
	
	return prob