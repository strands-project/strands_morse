from morse.builder import *
from math import cos, sin

class AddDeskDivider():
  _name = "AddDeskDivider"
  _short_desc = "Add desk divider"

  def __init__(self, x, y, yaw):
    #x coordinate
    #y coordinate
    #yaw angle (rotation about z-axis
   

    #z axis
    z=0.715

    
    self.wall= PassiveObject('g4s/data/objects/desk_divider.blend','desk_divider')
    self.wall.properties(Object = True)
    self.wall.translate(x,y,z)
    self.wall.rotate(0,0,yaw)

    
