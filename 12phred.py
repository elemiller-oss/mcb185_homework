import math

def char_to_prob(x):
	x = ord(x)
	return pow(10, -x / 10)
	
def prob_to_char(y):
	y = -10 * math.log10(y)
	return chr(y)
	
print(char_to_prob('A'))
print(prob_to_char(10))