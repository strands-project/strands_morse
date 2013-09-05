from morse.builder import *
from math import cos, sin,pi
from random import *

class AddTable():
  _name = "AddTable"
  _short_desc = "Add table with stools"

  def __init__(self, x, y, yaw, s, r, amin, amax, rar, raa):
    #x coordinate of table
    #y coordinate of table
    #yaw of table (rotation along z axis)
    #s - number of stools
    #r - perimeter for placing stools with center in the center of table (in m)
    #amin - minimal angle to place stools (in degrees)
    #amax - maximal angle to place stools (in degrees)
    #rar - set how big is interval (in m) for random placing of stools along circle
    #raa - set how big is interval for random angle (in degrees)

    z=0.1

    self.table= PassiveObject('bham/data/objects/lg/bar_table.blend','Bartable')
    self.table.properties(Object = True)
    self.table.translate(x,y,z)
    self.table.rotate(0,0,yaw)

    if (amin==0)&(amax == 360):
      inter = (amax-amin)/(s)
    else:
      inter = (amax-amin)/(s-1)
    for i in range(s):
      ran = (random()-0.5)*2*raa;
      an = (amin+i*inter+ran)*pi/180;
      rr = r+(random()-0.5)*2*rar; 
      xn = x+cos(an)*rr;
      yn = y+sin(an)*rr;
      self.stool= PassiveObject('bham/data/objects/lg/bar_stool.blend','barstool')
      self.stool.properties(Object = True)
      self.stool.translate(xn,yn,z)
      self.stool.rotate(0,0,yaw)      
