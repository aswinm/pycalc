#This code looks after the GUI part

#To evaluate the given expression, it calls the "calc" function in the "op" file

#!usr/bin/python
import op 
from gi.repository import Gtk
w=Gtk.Window()
table=Gtk.Table(5,5,True)
tb=Gtk.Entry()
class Window:
	def __init__(self):
		self.turn=False
	def equalclicked(self,widget):
		m=tb.get_text()
		m=str(op.calc(m))
		tb.set_text(m)
		self.turn=True
	def buttonclicked(self,widget):
		if self.turn==True:
			tb.set_text("")
			self.turn=False
		m=tb.get_text()
		m=m+widget._value
		tb.set_text(m)
	def clear(self,widget):
		tb.set_text("")
		self.turn=False
	def back(self,widget):
		m=tb.get_text()
		m=m[:-1]
		tb.set_text(m)
x=Window()

zero=Gtk.Button(label='0')
one=Gtk.Button(label='1')
two=Gtk.Button(label='2')
three=Gtk.Button(label='3')
four=Gtk.Button(label='4')
five=Gtk.Button(label='5')
six=Gtk.Button(label='6')
seven=Gtk.Button(label='7')
eight=Gtk.Button(label='8')
nine=Gtk.Button(label='9')
add=Gtk.Button(label='+')
sub=Gtk.Button(label='-')
mul=Gtk.Button(label='X')
div=Gtk.Button(label='/')
equ=Gtk.Button(label='=')
clear=Gtk.Button(label='C')
neg=Gtk.Button(label='+/-')
opbr=Gtk.Button(label='(')
exp=Gtk.Button(label='^')
clbr=Gtk.Button(label=')')
point=Gtk.Button(label='.')
back=Gtk.Button(label='<-')
buttons=[zero,one,two,three,four,five,six,seven,eight,nine]
for i in range(len(buttons)):
	buttons[i]._value=str(i)
nine._value='9'
exp._value='^'
add._value='+'
sub._value='-'
mul._value='*'
div._value='/'
equ._value='='
clear._value='c'
neg._value='-'
opbr._value='('
clbr._value=')'
point._value='.'
buttonlist=[zero,one,two,three,four,five,six,seven,eight,nine,point,add,sub,mul,div,opbr,clbr,neg,exp]
for button in buttonlist:
	button.connect("clicked",x.buttonclicked)
equ.connect("clicked",x.equalclicked)
back.connect("clicked",x.back)
clear.connect("clicked",x.clear)
table.attach(tb,0,3,0,1)
table.attach(exp,3,4,0,1)
table.attach(clear,4,5,0,1)
table.attach(seven,0,1,1,2)
table.attach(eight,1,2,1,2)
table.attach(nine,2,3,1,2)
table.attach(four,0,1,2,3)
table.attach(five,1,2,2,3)
table.attach(six,2,3,2,3)
table.attach(one,0,1,3,4)
table.attach(two,1,2,3,4)
table.attach(three,2,3,3,4)
table.attach(zero,0,1,4,5)
table.attach(point,1,2,4,5)
table.attach(add,3,4,1,2)
table.attach(sub,3,4,2,3)
table.attach(mul,3,4,3,4)
table.attach(div,3,4,4,5)
table.attach(equ,2,3,4,5)
table.attach(neg,4,5,2,3)
table.attach(opbr,4,5,3,4)
table.attach(clbr,4,5,4,5)
table.attach(back,4,5,1,2)
w.add(table)
w.show_all()
w.connect("delete-event",Gtk.main_quit)		
Gtk.main()
