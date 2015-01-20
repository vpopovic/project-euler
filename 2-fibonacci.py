"""
Each new term in the Fibonacci sequence is generated by adding the 
previous two terms. By starting with 1 and 2, 
the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do
not exceed four million, find the sum of the even-valued terms.
"""

fibseq = 4000000
evensum = 0

a,b = 0,1

for d in range(fibseq - 2):
	c = a + b
	a, b = b, c
	if (c % 2 == 0):
		evensum += c
		if (c >= fibseq):
			print c
			break
