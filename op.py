#This code is used to work on with the evaluation of the given arithmetic expression



#!/usr/bin/python
import stacalc as st
class stack:
	def __init__(self):
		self.items=[]
	def push(self,a):
		self.items.append(a)
	def pop(self):
		return self.items.pop()
	def isempty(self):
		return len(self.items)==0
	def top(self):
		return self.items[-1]
numeric=stack()
operator=stack()
precedence={'*':1,'/':1,'+':2,'-':2,'^':0}
oper=['*','/','+','-','^']

def find():
	a=numeric.pop()
	b=numeric.pop()
	c=operator.pop()
	if c=='*':
		numeric.push(a*b)
	elif c=='/':
		numeric.push(b/a)
	elif c=='+':
		numeric.push(a+b)
	elif c=='-':
		numeric.push(b-a)
	elif c=='^':
		numeric.push(b**a)

def calc(expr):
	num=""
	i=0
	count=0
	for i in expr:
		if i=='(':
			count+=1
		if count:
			num+=i
			if i==')':
				count-=1
			if count==0:
				x=st.calc(num)
				numeric.push(x)
				num=""
		else:
			if i.isdigit() or i=='.':
				num+=i	
			elif i in oper:
				if num=='':
					numeric.push(0)
				else:
					numeric.push(eval(num))
				if i=='-':
				
					num='-'
					i='+'
				else:
					num=""
				if operator.isempty() or precedence[i]<precedence[operator.top()]:
					operator.push(i)
				elif precedence[i]>=precedence[operator.top()]:
					find()
					operator.push(i)
	
				elif i==" ":
					pass
			
	if num:
		numeric.push(eval(num))
	while not operator.isempty():
		find()
	return numeric.pop()

				
			

		
			
