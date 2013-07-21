#This code is to evaluate the expression if it containd brackets"()"

#!/usr/bin/python
class stack:
	def __init__(self):
		self.items=[]
	def push(self,a):
		self.items.append(a)
	def pop(self):
		return self.items.pop()

def evalu(a,s):
	b=['0','1','2','3','4','5','6','7','8','9','.']
	if a in b:
		s=s+a
		return s
	elif a==')':
		if s!="":
			x.push(eval(s))
		m=find()
		x.push(m)
		return ""
	elif a=='-':
		if s!="":
			x.push(eval(s))
			x.push('-')
			return ""
		else:
			s=s+"-"
			return s
	else:
		if s!="":
                	x.push(eval(s))
		x.push(a)
		return ""	
def calc(expr):
	
	i=0
	s=""
	while i<len(expr):
		s=evalu(expr[i],s)
		i+=1
	if len(x.items):
		return x.pop()
	
def find():
	a=x.pop()
	b=x.pop()
	c=x.pop()
	d=x.pop()
	if b=="+":
		f=a+c
	if b=="-":
		f=c-a
	if b=="*":
		f=a*c
	if b=="/":
		f=c/a
	if b=='^':
		f=c**a
	return f
x=stack()
	
