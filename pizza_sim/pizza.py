from random import randint
from numpy.random import triangular
# pizza simulation
# note, using a triangular dist becuase currently need an approx of unknown dist

def action(actionName, minTime, modeTime, maxTime):
	
	min_time = minTime
	mode_time = modeTime
	max_time = maxTime
	#1 heat water to 110 degrees
	time = triangular(left = min_time, mode =mode_time , right = max_time )
	print('%s: %s seconds' % (actionName,str(time)))

	return time


# make dough
def make_dough():
	""" 
	function 'makes dough' and returns time needed for the entire process
	"""

	dough_steps = {
	# Step 1: heat water to 110 degree
	1 :{'action': 'Heat Water', 
		'min_time': 5, 
		'mode_time': 10, 
		'max_time': 20 },
	# Step 2: mix yeast and wait
	2 :{'action': 'Mix Yeast', 
		'min_time': 10, 
		'mode_time': 12, 
		'max_time': 15},
	# Step 3: mix yeast and wait
	3 :{'action': 'Combine and Knead Dough', 
		'min_time': 15, 
		'mode_time': 20, 
		'max_time': 30},
		# Step 3: mix yeast and wait
	4 :{'action': 'let rest', 
		'min_time': 120, 
		'mode_time': 1440, 
		'max_time': 2880},

	}

	running_time = 0

	for step in dough_steps:
		step_action = dough_steps[step]['action']
		step_min = dough_steps[step]['min_time']
		step_mode = dough_steps[step]['mode_time']
		step_max = dough_steps[step]['max_time']

		time = action(step_action,step_min,step_mode,step_max)
		running_time += time



	print(running_time)



make_dough()