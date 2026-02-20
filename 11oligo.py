def tm(A, C, G, T):
	if (A+C+G+T) <= 13: return (A+T)*2 + (G+T)*4
	if (A+C+G+T) > 13: return 64.9 + 41*(G+C-16.4) / (A+T+G+C)
print (tm(2, 2, 2, 2))