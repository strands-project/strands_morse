from morse.builder import *
from math import cos, sin,pi
from random import *

class AddRightTable():
  _name = "AddRightTable"
  _short_desc = "Add right table"

  def __init__(self, x, y, yaw):
    #x coordinate of table
    #y coordinate of table
    #yaw of table (rotation along z axis)
    
    z=0.0

    self.tableL= PassiveObject('g4s/data/objects/desk_right.blend','desk_right')
    self.tableL.properties(Object = True)
    self.tableL.translate(x,y,z)
    self.tableL.rotate(0,0,yaw)

     
