# Calculus Library  
### building module to serve as backend for symbolic mathematics application.

A project that has been attracting my interest is building a calculus module to support the backend of a symbolic mathematics application. Think Wolfram Alpha. No, I'm not trying to reinvent the wheel or do anything innovative, I just think it will be a fun exercise. Sure calculus is pretty easy, but coding it takes some care.

To use:
From the root directory of the download
sudo pip3 install .

within python3

from calculus import expression

exp=expression('2x^2+3x^3y^2z^6+4x^2')

exp.simplify() # will simplify
exp.derive('y') # will derive wrt y
exp.derive('z') # will derive wrt z etc.
