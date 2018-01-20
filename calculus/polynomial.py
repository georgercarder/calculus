
import re

## --FIXED ///PROBLEM!! ex=expression('2x^3y') ex.derive('x') gives '6x^2'. FIX THIS!! :
## expression simplify() and derive() are ready.
## use: exp=expression('2x^3+4y^7+5x^3'), exp.derive('y') derives wrt y
## goal here is polynomials
## need to build binomial formula and other mult simplifiers
## need to address negative coefficients-- resolved

class expression:

	__string=None

	def __init__(self,string):
		self.__string=string

	def setString(self,string):
		self.__string=string
		if self.__string=='':
			self.__string=='0'
		return self.__string

	def getString(self):		# string of form '2x^3-5y^2+7x^2'
		return self.__string

	def derive(self, wrt):		# self.derive('x') to derive wrt x
		self.__wrt=wrt
		self.simplify()
		__terms=self.getString().split('+')
		__derived=""
		for i in range(len(__terms)):
			if re.findall(self.__wrt,__terms[i])==[]:
				pass	
			else:
				__terms[i]=self.__deriveterm(__terms[i],wrt) 
				__derived=__derived+__terms[i]+'+'
		#print(__terms)
		__derived=__derived.rstrip('+')
		if __derived=="":
			__derived='0'
		__derived=__derived.replace('+-','-')
		return __derived

	def __deriveterm(self,__term,__wrt): 	# derives terms having variable of interest
		__term=__term
		__wrt=__wrt
	#	print(__term,__wrt)
		if len(re.findall(__wrt, __term))==0:
			return "" 
		else:
			print(re.findall('^\d*',__term))	
			if len(re.findall('^\d*',__term)[0])==0:
				__c=['1']
	#			print('here')
			else:
				__c=re.findall('^\d*',__term)
	#			print('there')

			__wrtex=__wrt+'\^*\d*'
			__wrtexp=re.findall(__wrtex,__term)
			__wrtbet='^\d*(.*)'+__wrt
			__wrtbetw=re.findall(__wrtbet,__term)
			__wrtaft=__wrt+'\^*\d*(.*)'
			__wrtafter=re.findall(__wrtaft,__term)

		#	print(__wrtex,__wrtexp,__wrtbet,__wrtbetw,__wrtaft,__wrtafter)

			if len(re.findall('\^',__wrtexp[0]))==0:
				__exp=['1']
			else:
				__exp=re.findall('\d+$',__wrtexp[0])
			if __exp==[]:
				__exp=['1']
	#		print(__c,__exp)	
			__c=int(__c[0])*int(__exp[0])
			if int(__exp[0])!=2:
				if int(__exp[0])!=1:
					self.__derivedterm=str(__c)+str(__wrtbetw[0])+str(__wrt)+"^"+str(int(__exp[0])-1)+str(__wrtafter[0])
				else:
	#				print(__c,__wrtbetw,__wrtafter)
					self.__derivedterm=str(__c)+str(__wrtbetw[0])+str(__wrtafter[0])
			else:
				self.__derivedterm=str(__c)+str(__wrtbetw[0])+str(__wrt)+str(__wrtafter[0])
	
		#	print(self.__derivedterm)	
			return self.__derivedterm
	#simplifies '2x^2+5x^3y^5+2y+2x^3y^5' to '2x^2+7x^3y^5+2y'

	def simplify(self):	
		__terms=self.__string.replace('-','+-').split("+") 	# resolving negative coefficients
		__c=[]
		__d=[]
		for i in range(len(__terms)):
			if re.findall(r'^-*\d',__terms[i])==[]:
				__c.append('1')
			else:
				__c.append(re.sub(r'[a-z]+(.*)','',__terms[i]))
		for i in range(len(__terms)):
			__d.append(re.sub("^-*\d+","",__terms[i]))
		simpdict={}
		for i in range(len(__terms)):
			if __d[i] in simpdict:
				simpdict[__d[i]]=int(__c[i])+int(simpdict[__d[i]])
			else:
				simpdict[__d[i]]=__c[i]
		for i in simpdict:
			if i!="" and simpdict[i]=='1':
				simpdict[i]=""
		__simplified=""	
		for i in sorted(simpdict):
			__simplified=__simplified+str(simpdict[i])+i+'+'

		__simplified=__simplified.replace('+-','-').rstrip('+')
		self.__string=__simplified
		return self.__string		
