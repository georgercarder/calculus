#tests

from calculus import finitesum

def test2_1():
  exp=finitesum('2x^3y^4z^7')
  assert(exp.derive('y')=='8x^3y^3z^7')

def test2_2():
  exp2=finitesum('2x^2yz^3')
  assert(exp2.derive('y')=='2x^2z^3')

def test2_3():
  exp3=finitesum('y^3+2y')
  assert(exp3.derive('y')=='2+3y^2')

def test2_4():
  exp4=finitesum('0+x')
  assert(exp4.simplify()=='x')

def test2_5():
  exp5=finitesum('-y^6x^7')
  assert(exp5.derive('y')=='-6y^5x^7')

def test2_6():
  exp6=finitesum('y^-4')
  assert(exp6.derive('y')=='-4y^-5')

def test2_7():
  exp7=finitesum('y^-4')
  assert(exp7.simplify()=='y^-4')

def test2_8():
  exp8=finitesum('2x^-7-2y^-5')
  assert(exp8.derive('y')=='10y^-6')

def test2_9():
  exp9=finitesum('0')
  assert(exp9.simplify()=='0')

