
import re

##goal here is polynomials

class expression:

	__string=None

	def __init__(self,string):
		self.__string=string

	def setString(self,string):
		self.__string=string

	def getString(self):
		return self.__string


	def simplify(self):
		__terms=self.__string.split("+")
		print(__terms)
		__c=[]
		__d=[]
		for i in range(len(__terms)):
			if re.findall(r'^\d',__terms[i])==[]:
				__c.append('1')
			else:
				__c.append(re.sub(r'\D(.*)','',__terms[i])[0])
		print(__c)
		for i in range(len(__terms)):
			__d.append(re.sub("^\d+","",__terms[i]))
		print(__d)	
		simpdict={}
		for i in range(len(__terms)):
			if __d[i] in simpdict:
				simpdict[__d[i]]=int(__c[i])+int(simpdict[__d[i]])
			else:
				simpdict[__d[i]]=__c[i]
		print(simpdict)
		__simplified=""	
		for i in simpdict:
			__simplified=__simplified+str(simpdict[i])+i+'+'

		__simplified=__simplified.rstrip('+')
		print(__simplified)
		self.__string=__simplified
		return self.__string		
