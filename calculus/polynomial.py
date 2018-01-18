
import re

## goal here is polynomials
## need to build binomial formula and other mult simplifiers
## need to build derivative wrt each variable

class expression:

	__string=None

	def __init__(self,string):
		self.__string=string

	def setString(self,string):
		self.__string=string

	def getString(self):
		return self.__string

	def derive(self, wrt):
		self.__wrt=wrt
		self.simplify()
		__terms=self.string.split('+')
		for i in range(len(__terms)):
			if re.findall(self.__wrt,__terms[i])==[]:
				pass
			else:
				__terms[i]=deriveterm(__terms[i],wrt) #need to define deriveterm
		__derived=""
		for i in range(len(__terms)):
			__derived=__derived+__terms[i]+'+'	
		__derived=__derived.rstrip('+')
		return __derived

	def deriveterm(__term, wrt):
		if len(re.findall( wrt, __term))==0:
			return 0
		else:
			if len(re.findall('^\d*',__term))==0:
				__c=1
			else:
				__c=re.findall('^\d*',__term)

			__wrtex=wrt+'\^*\d*'
### here grep ^ to see if exponent is 1:

	#simplifies '2x^2+5x^3y^5+2y+2x^3y^5' to '2x^2+7x^3y^5+2y'


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
