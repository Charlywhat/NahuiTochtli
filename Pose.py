def coward(input_vals):
	w = [-2,1,2,-3,5]
	return neuron(input_vals, w)

def aggressive(input_vals):
	w = [1,1,1,1,1]
	return neuron(input_vals, w)

def crafty(input_vals):
	w = [1,0,-2,-2,3]
	return neuron(input_vals, w)


def neuron(dendrite, weights):
	s = 0
	for n in range(5):
		if dendrite[n] == True:
			dendrite[n] = 1
		else: dendrite[n] = 0
		s += dendrite[n]*weights[n]
	if s >= 0: s = 1
	else: s = -1
	return s

