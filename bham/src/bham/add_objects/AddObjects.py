from morse.builder import *
from bham.add_objects.AddWall import AddWall
from bham.add_objects.AddTable import AddTable
from math import pi

def add_walls():
  
  #half of wall_holder
  whx = 0.02
  why = 0.02
  #half of wall
  wx = 0.02
  wy = 0.8
  #half of small wall
  wsx = 0.02
  wsy = 0.3

  x = [3, 3, 0, -3.7, -3.7-2*why-2*wy, -3.7-4*why-4*wy , -10.0, -12.45, -12.45]
  y = [-3.6, -3.6+why+wy+wsy, -1, -1,-1,-1, -3.6, -3.9, -3.9+why+wsy+wy]
  yaw = [0, 0, -pi/2, -pi/2, -pi/2, -pi/2, 0, 0, 0]
  hl = [1, 1, 0, 1, 1, 1, 1, 1, 1]
  hr = [0, 1, 1, 0, 0, 1, 1, 0, 1]
  b =  [1, 0, 1, 1, 1, 1, 1, 0, 1]
  #number of walls
  n = 9;
 
  for i in range(n):
    wall = AddWall(x[i],y[i],yaw[i],hl[i],hr[i],b[i])

def add_table():
  n = 10
  x=[ 2.6, 0.0, 1.0, -1.5, -3.5, -5.3, -3.7, -6.7, -9.5, -7.3]
  y=[-2.6,-1.3,-3.8, -3.8, -1.3, -1.3, -3.7, -3.8, -3.0, -1.7] 
  yaw =[0, 0, 0, 0, pi/3, 0, pi/4, pi/2, 0, pi/6]
  s = [3, 4, 4, 4, 4, 4,  4, 4, 4, 4]
  r = [0.5, 0.5, 0.3, 0.3, 0.5, 0.4, 0.5, 0.35, 0.5, 0.4]
  amin = [90, 180, 0, 0, 180, 180,  0, 0, -90, 180]
  amax = [270, 360, 360, 360, 360, 360, 180, 180, 90, 360]
  rar = [0.2, 0.1, 0.2, 0.1, 0.1, 0.2, 0.05, 0.1, 0.2, 0.1]
  raa = [15, 15, 5, 0, 20, 5, 10, 20, 5, 15]
  
  for i in range(n):
    table = AddTable(x[i],y[i],yaw[i],s[i],r[i],amin[i],amax[i],rar[i],raa[i])
  
  
  

  


