from morse.builder import *
from g4s.add_objects.AddDeskDivider import AddDeskDivider
from g4s.add_objects.AddLeftTable import AddLeftTable
from g4s.add_objects.AddRightTable import AddRightTable
from g4s.add_objects.AddShelf import AddShelf
from g4s.add_objects.AddTallShelf import AddTallShelf
from math import pi

def add_desk_divider():  

  x = [-9.89, -4.72, 0.03, 5.26, 18.08]
  y1 = 3.32
  y2 = 3.01
  yaw = pi/2 
  n = 5;
 
  for i in range(n):
    if i<4:
      wall = AddDeskDivider(x[i],y1,yaw)
    else:
      wall = AddDeskDivider(x[i],y2,yaw)

def add_right_table():
  n = 14
  x=[ -13.85, -11.46, -8.32, -6.29, -3.15, -1.54, 1.6, 3.69, 6.83, 15.55, 16.51, 19.65, 21.06, 18.09]
  y1 = 3.32
  y2 = 3.01 
  y3 = -4.88
  yaw =[-pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2] 

  for i in range(n):
    if i<9:
      table = AddRightTable(x[i],y1,yaw[i])
    elif i<13:
      table = AddRightTable(x[i],y2,yaw[i])
    elif i == 13:
      table = AddRightTable(x[i],y3,yaw[i])


def add_left_table():
  n = 13
  x=[ -13.85, -11.46, -8.32, -6.29, -3.15, -1.54, 1.6, 3.69, 6.83, 15.55, 16.51, 19.65, 21.06]
  y1 = 3.32 
  y2 = 3.01
  yaw =[-pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, -pi/2, pi/2, pi/2, -pi/2, pi/2, -pi/2] 

  for i in range(n):
    if i<9:
      table = AddLeftTable(x[i],y1,yaw[i])
    elif i<13:
      table = AddLeftTable(x[i],y2,yaw[i])

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

  x2 = 16.39
  y2 = -1.06
  shelf = AddShelf(x2,y2,0,1) 
  shelf = AddShelf(x2+s,y2,0,0) 
  shelf = AddShelf(x2,y2-0.5,pi,0) 
  shelf = AddShelf(x2+s,y2-0.5,pi,0) 
  
  


  
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

  shelf = AddTallShelf(-14.75,5.06,pi,1)

  


