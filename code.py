
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

plt.ion()
theta2=0
"""defining a function which will draw polygon when vertices of polygon given as input."""
def draw_polygon(x_coord,y_coord):
	

	plt.ion()
	plt.plot(x_coord+[x_coord[0]],y_coord+[y_coord[0]])


shape=input()#taking input of shape disc or polygon whichever user wants to draw
if shape=="polygon":
	x_coord=[int(x) for x in input().split(" ")]
	y_coord=[int(x) for x in input().split(" ")]
	draw_polygon(x_coord,y_coord)
if shape=="disc":
	a,b,r=[int(x) for x in input().split(" ")]
	
	x1=[r]
	y1=[r]
	x_coord=[]
	y_coord=[]

	import math
	for i in range(0,360):
		
		x=float(x1[0])*(math.cos(math.radians(i)))+a
		y=float(y1[0])*(math.sin(math.radians(i)))+b
		x_coord.append(x)
		y_coord.append(y)
inp=[]
w=[]
"""defining a function which will do matrix multiplication."""
def matrix_mult(a,b):
	z=[]
	x1=len(a)
	x2=len(b[0])
	for i in range(x1):
		w=["-"]*x2
		z.append(w)
	for r1 in range(len(a)):
		for c2 in range(len(b[0])):
			r=0
			for c1 in range(len(a[0])):
				if(type(b[c1][c2])==list):
					r=float(r)+(a[r1][c1])*(b[c1][c2][0])
				else:
					r=float(r)+(a[r1][c1])*(b[c1][c2])
			z[r1][c2]=round(r,2)
	return z
"""defining a function which will give 3*3 matrix."""
def matrix3_3():
	b=[]
	a=[0]*3
	for i in range(3):
		b.append(a)
	return b

def new_matrix(z,index,indextobechanged,c):
	changed=[]
	for y in range(0,len(z)):
		if(y==index):
			s=list(z[y])
			s[indextobechanged]+=c
			changed.append(s)
		else:
			changed.append(z[y])
	return changed


def scaling(SX,SY,x_coord,y_coord):
	z=matrix3_3()
	z=new_matrix(z,0,0,SX)
	z=new_matrix(z,1,1,SY)
	z=new_matrix(z,2,2,1)
	for i in range(len(x_coord)):
		b=[]
		x1=x_coord[i]
		y1=y_coord[i]
		b.append([x1])
		b.append([y1])
		b.append([1])
		m=matrix_mult(z,b)
		x_coord[i]=m[0][0]
		y_coord[i]=m[1][0]
	z1=[x_coord,y_coord]
	return z1
"""defining a function which do rotation"""
def rotation(theta,x_coord,y_coord):
	z=matrix3_3()
	import math
	z=new_matrix(z,0,0,math.cos(math.radians(theta)))
	z=new_matrix(z,0,1,-(math.sin(math.radians(theta))))
	z=new_matrix(z,1,0,math.sin(math.radians(theta)))
	z=new_matrix(z,1,1,math.cos(math.radians(theta)))

	z=new_matrix(z,2,2,1)

	for i in range (len(x_coord)):
		b=[]
		x1=x_coord[i]
	
		y1=y_coord[i]
		b.append([x1])
		b.append([y1])
		b.append([1])
	
		m=matrix_mult(z,b)
		x_coord[i]=m[0][0]
		y_coord[i]=m[1][0]
	z1=[x_coord,y_coord]
	return z1

"""defining a function which do translation"""
def translation(dx,dy,x_coord,y_coord):
	z=matrix3_3()
	z=new_matrix(z,0,0,1)
	z=new_matrix(z,1,1,1)
	z=new_matrix(z,2,2,1)
	z=new_matrix(z,0,2,dx)
	z=new_matrix(z,1,2,dy)
	for i in range (len(x_coord)):
		b=[]
		x1=x_coord[i]
		y1=y_coord[i]
		b.append([x1])
		b.append([y1])
		b.append([1])
		m=matrix_mult(z,b)
		x_coord[i]=m[0][0]
		y_coord[i]=m[1][0]
	z1=[x_coord,y_coord]
	return z1
theta2=0
if shape=="disc":
	#draw_ellipse(a,b,x1[0],y1[0],theta2)#to draw the original ellipse
	draw_polygon(x_coord,y_coord)
a1="quit"
while a1 not in w:
	w=[]
	w=[x for x in input().split(" ")]

	if w[0]!="quit":
		inp.append(w)
	else:
		break
	theta1=[]

	k=inp[-1]
	if k[0]=="S":# if scaling to be done
		SX=int(k[1])# scaling to be done along x-axis
		SY=int(k[2])# scaling to be done along y-axis
		scale=scaling(SX,SY,x_coord,y_coord)# calling scaling function


		x_coord=scale[0]
		y_coord=scale[1]

		if shape=="disc":# if shape is disc we will scale semi major-axis and semi minor-axis
			scale1=scaling(SX,SY,x1,y1)
			x1=scale1[0]#as semi major and semi minor length changes  
			y1=scale1[1]
			
			print(a,b,x1[0],y1[0])

		
		else:#if shape is polygon we will scale  each of the vertices 
			print(x_coord,y_coord)
		draw_polygon(x_coord,y_coord)
			
	elif k[0]=="R":# if rotation to be done
		theta=int(k[1])
		theta1.append(theta)
		theta2=theta2+theta
		rotate=rotation(theta,x_coord,y_coord)#calling rotation function
		x_coord=rotate[0]
		y_coord=rotate[1]
		
		if shape=="disc":#if shape is disc we will rotate about origin through that angle and thus call rotation function for centre coordinates
			rotate=rotation(theta,[a],[b])
			a=rotate[0][0]
			b=rotate[1][0]
			print(a,b,x1[0],y1[0])
		

		else:#if shape is polygon we will rotate each of the vertices
			print(x_coord,y_coord)
		draw_polygon(x_coord,y_coord)
	elif k[0]=="T":# if translation to be done
		dx=int(k[1])
		dy=int(k[2])
		translate=translation(dx,dy,x_coord,y_coord)
		x_coord=translate[0]
		y_coord=translate[1]
		if shape=="disc":# if shape is disc we will call translation function to translate the centre coordinates
			translate1=translation(dx,dy,[a],[b])
			a=translate1[0][0]
			b=translate1[1][0]
			print(a,b,x1[0],y1[0])
			
		else:#if shape is polygon we will translate each of the vertices
			print(x_coord,y_coord)
		draw_polygon(x_coord,y_coord)
	
plt.pause(0.1)
plt.show()
