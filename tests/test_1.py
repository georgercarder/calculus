#tests

from calculus import expression

def test1():
	exp=expression('1')
	assert(exp.derive('x')=='0')

