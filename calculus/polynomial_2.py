
import re

## goal here is finite products 

class finiteproduct(finitesum):

	__string=None

	def __init__(self,string):
		self.__string=string

	def setString(self,string):
		self.__string=string
		if self.__string=='':
			self.__string=='0'
		return self.__string

	def getString(self):		
		return self.__string
	


	def simplify(self):	
		return self.__string		
