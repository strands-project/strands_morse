from morse.builder import *
from math import cos, sin,pi
from random import *

class AddLeftTable():
  _name = "AddLeftTable"
  _short_desc = "Add left table"

  def __init__(self, x, y, yaw):
    #x coordinate of table
    #y coordinate of table
    #yaw of table (rotation along z axis)
    
    z=0.0

    self.tableL= PassiveObject('g4s/data/objects/desk_left.blend','desk_left')
    self.tableL.properties(Object = True)
    self.tableL.translate(x,y,z)
    self.tableL.rotate(0,0,yaw)

     
