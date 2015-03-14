from morse.builder import *
from g4s.add_objects.AddDeskDivider import AddDeskDivider
from g4s.add_objects.AddLeftTable import AddLeftTable
from g4s.add_objects.AddRightTable import AddRightTable
from g4s.add_objects.AddShelf import AddShelf
from g4s.add_objects.AddTallShelf import AddTallShelf
from math import pi

def add_desk_divider():  

  x = [-9.89, -4.72, 0.03, 5.26]
  y= 3.32
  yaw = pi/2 
  n = 4;
 
  for i in range(n):
    wall = AddDeskDivider(x[i],y,yaw)

def add_right_table():
  n = 9
  x=[ -13.85, -11.46, -8.32, -6.29, -3.15, -1.54, 1.6, 3.69, 6.83]
  y= 3.32 
  yaw =[-pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2] 

  for i in range(n):
    table = AddRightTable(x[i],y,yaw[i])

def add_left_table():
  n = 9
  x=[ -13.85, -11.46, -8.32, -6.29, -3.15, -1.54, 1.6, 3.69, 6.83]
  y= 3.32 
  yaw =[-pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2] 

  for i in range(n):
    table = AddLeftTable(x[i],y,yaw[i])
  
def add_shelf():  

  s = 1.06 # size of the shelf
  x = [-11.68, -7.05, -2.9, 1.72, 6.37 ]
  y= 0.68
  yaw = 0 
  b = [1,0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0] # open or close shelf
  n = 5;
 
  for i in range(n):
    shelf = AddShelf(x[i],y,yaw,b[i*3])
    shelf = AddShelf(x[i]-s,y,yaw,b[i*3+1])
    shelf = AddShelf(x[i]-2*s,y,yaw,b[i*3+2])
  
def add_tall_shelf():
  s = 1.06
  x = [-15.55, 8.80]
  y= [3.5, 4.78]
  yaw = [-pi/2, pi/2]
  b = [0, 0, 1, 1, 0, 1]

  n = 2

  for i in range(n):
    shelf = AddTallShelf(x[i],y[i],yaw[i],b[i*3])
    shelf = AddTallShelf(x[i],y[i]-s,yaw[i],b[i*3+1])
    shelf = AddTallShelf(x[i],y[i]-2*s,yaw[i],b[i*3+2])

  shelf = AddTallShelf(-15.27,5.16,pi,1)

  


