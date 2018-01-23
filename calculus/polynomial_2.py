
import re
from .polynomial_1 import finitesum

## goal here is finite products. in development. not ready yet. 
## a*(finitesum1)^e1***(finitesumN)^eN

class finiteproduct(finitesum):

	__string=None

	def __init__(self,string):
		super(finiteproduct, self).__init__(string) 	

