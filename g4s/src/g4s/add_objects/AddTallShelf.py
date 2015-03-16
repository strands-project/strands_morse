from morse.builder import *
from math import cos, sin,pi
from random import *

class AddTallShelf():
  _name = "AddTallShelf"
  _short_desc = "Add tall shelf"

  def __init__(self, x, y, yaw, b):
    #x coordinate of table
    #y coordinate of table
    #yaw of table (rotation along z axis)
    #b - boolean - 0 closed shelf, 1 opened shelf
    
    z=0.0

    if(b):
      self.tableL= PassiveObject('g4s/data/objects/openShelf.blend','openShelf')
      self.tableL.properties(Object = True)
      self.tableL.translate(x,y,z)
      self.tableL.rotate(0,0,yaw)

      self.tableL= PassiveObject('g4s/data/objects/openShelf.blend','openShelf')
      self.tableL.properties(Object = True)
      self.tableL.translate(x,y,z+0.78)
      self.tableL.rotate(0,0,yaw)
    else:
      self.tableL= PassiveObject('g4s/data/objects/closedShelf.blend','closedShelf')
      self.tableL.properties(Object = True)
      self.tableL.translate(x,y,z)
      self.tableL.rotate(0,0,yaw)

      self.tableL= PassiveObject('g4s/data/objects/closedShelf.blend','closedShelf')
      self.tableL.properties(Object = True)
      self.tableL.translate(x,y,z+0.78)
      self.tableL.rotate(0,0,yaw)

     
