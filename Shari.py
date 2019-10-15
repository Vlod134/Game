from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x800')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
colors = ['red','orange','yellow','green','blue']
a = [[0,0,0] for i in range (0,5)]
p=0
vsego=0
velocity = [[0,0] for i in range (0,5)]
clicked = [0,0,0,0,0]

def new_ball():
   clicked = [0,0,0,0,0]
   global now,vsego,velocity,clicked
   canv.delete(ALL)
   now=rnd(1,5)
   vsego=vsego+now
   for i in range (0,5):
	   velocity[i][0]=rnd(-5,5)
	   velocity[i][1]=rnd(-5,5)
	   if (i<now):
		   x = rnd(100,700)
		   y = rnd(100,500)
		   r = rnd(30,50)
		   a[i]=[x,y,r]
	   else:
		   a[i]=[0,0,0]
   root.after(2000,new_ball) 
   
def balls_movement():
	for i in range (0,5):
		x=a[i][0]
		y=a[i][1]
		r=a[i][2]
		canv.create_oval(x-r,y-r,x+r,y+r,fill = 'white', width=0)
		if ((x-r)<0 or (x+r)>800):
			velocity[i][0]*=-1
		if ((y-r)<0 or (y+r)>800):
			velocity[i][1]*=-1
			
		a[i][0]=a[i][0]+velocity[i][0]
		a[i][1]=a[i][1]+velocity[i][1]
		x=a[i][0]
		y=a[i][1]
		r=a[i][2]
		canv.create_oval(x-r,y-r,x+r,y+r,fill = colors[i], width=0)
	root.after(1,balls_movement) 
		 		
def click(event):
	global p
	for i in range (0,5):
		r_nov = (event.x - a[i][0])*(event.x - a[i][0]) + (event.y - a[i][1])*(event.y - a[i][1])
		if ((r_nov < a[i][2] * a[i][2]) and (clicked[i]==0)):
			clicked[i]=1
			p = p+1
	print('score: ',p,'  percent: {:.3}'.format(p*100/vsego))
	l['text'] = 'score: '+str(p)+'  percent: {:.3}'.format(p*100/vsego)
	
	
l = Label(bg='black', fg='white', width=20)
l['text'] = 'score: '+str(p)
l.pack()
new_ball()
balls_movement()
canv.bind('<Button-1>', click)
mainloop()
