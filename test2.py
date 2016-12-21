KEY = 14

def compvalido1():
	b = False 
	if (1 <= 10 and 2 >= 1):
		b = ('b' == 'b') or ((KEY == 14 or KEY == 12) \
			and ('a' == 'a'))


for row in range(1,20000000):
	compvalido1()
print("fin")