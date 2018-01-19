#tests

from calculus import expression

def test1():
	exp=expression('1')
	assert(exp.derive('x')=='0')
	assert(exp.getString()=='1')


def test2():
	exp2=expression('2x^7')
	assert(exp2.derive('x')=='14x^6')


def test3():
	exp3=expression('2x+5y^7')
	exp3.setString('3y^2+82z')
	assert(exp3.getString()=='3y^2+82z')

def test4():
	exp4=expression('2x^3+4y^2+5x^3')
	assert(exp4.simplify()=='4y^2+7x^3')

def test5():
	exp5=expression('2x^3-4y^2-5x^3')
	assert(exp5.simplify()=='-4y^2-3x^3')

def test6():
	exp6=expression('2x^3+1y')
	assert(exp6.simplify()=='2x^3+y')
