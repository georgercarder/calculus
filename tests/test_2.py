#tests

from calculus import expression

def test2_1():
	exp=expression('2x^3y^4z^7')
	assert(exp.derive('y')=='8x^3y^3z^7')

def test2_2():
	exp2=expression('2x^2yz^3')
	assert(exp2.derive('y')=='2x^2z^3')

def test2_3():
	exp3=expression('y^3+2y')
	assert(exp3.derive('y')=='2+3y^2')

def test2_4():
	exp4=expression('0+x')
	assert(exp4.simplify()=='x')

def test2_5():
	exp5=expression('-y^6x^7')
	assert(exp5.derive('y')=='-6y^5x^7')
