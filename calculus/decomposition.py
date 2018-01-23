#!/usr/bin/python

## MOCK UP .. in development. Depends on finiteproduct (which isn't ready yet)
import re

# strategy: count left paren
# def finitesums simplify
# def finiteprods simplify
# repeat

## re.findall('\([a-z0-9A-Z\+-^]+\)',) #gives (z+4u)...

## re.findall('[0-9]*\([a-z0-9A-Z\+-^]+\)\^*[0-9]*',a) #gives 4(A+B)^3

a='2(x^3+(2y(z+4u+3z)^2-3(x+86v^2-(22x+y+5x)))-72)^3'


n=a.count('(')

while n>0:
X=re.findall('[0-9]*\([a-z0-9A-Z\+-^]+\)\^*[0-9]*',a)
XX=X
	# simplify each of these finite sums
for i in range(len(X)):
	S=re.findall('\([a-z0-9A-Z\+-^]+\)',X[i])
	finsum=finitesum(S[0].strip('(').strip(')'))
	finsum.simplify()
	XX[i]=X[i].replace(S[0].strip('(').strip(')'),finsum.getString())

	# now multipy
	P=finiteproduct(XX[i])
	P.simplify()
	XX[i]=P.getString()

	a.replace(X[i],XX[i])
	n-=1

