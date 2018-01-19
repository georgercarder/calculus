#tests

from calculus import expression

def test2_1():
	exp=expression('2x^3y^4z^7')
	assert(exp.derive('y')=='8x^3y^3z^7')
