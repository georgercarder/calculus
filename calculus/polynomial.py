
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
		__terms=self.getString().split('+')

		self.func('hey')
		for i in range(len(__terms)):
			if re.findall(self.__wrt,__terms[i])==[]:
				pass
			else:
				__terms[i]=self.deriveterm(__terms[i],wrt) 
		__derived=""
		for i in range(len(__terms)):
			__derived=__derived+__terms[i]+'+'	
		__derived=__derived.rstrip('+')
		return __derived

	def func(self,x):
		print(x)
	
	def deriveterm(self,__term,__wrt):
		__term=__term
		__wrt=__wrt
		if len(re.findall(__wrt, __term))==0:
			return "" 
		else:
			if len(re.findall('^\d*',__term))==0:
				__c=1
			else:
				__c=re.findall('^\d*',__term)

			__wrtex=__wrt+'\^*\d*'
			__wrtexp=re.findall(__wrtex,__term)
			if len(re.findall('\^',__wrtexp[0]))==0:
				__exp=1
			else:
				__exp=re.findall('\d+$',__wrtexp[0])
			print(__c, __exp)
			__c=int(__c[0])*int(__exp[0])
			print(__c,__wrt,__exp)
			if int(__exp[0])!=2:
				self.__derivedterm=str(__c)+str(__wrt)+"^"+str(int(__exp[0])-1)
			else:
				self.__derivedterm=str(__c)+str(__wrt)
	
			return self.__derivedterm
###

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
