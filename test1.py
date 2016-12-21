KEY = 14

def compvalido1():
	b = (1 <= 10 and 2 >= 1)
	if b:
		b = ('b' == 'b')
		if KEY == 14 or KEY == 12:
			b = ('a' == 'a')


for row in range(1,20000000):
	compvalido1()
print("fin")