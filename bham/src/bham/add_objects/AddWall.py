from morse.builder import *
from math import cos, sin

class AddWall():
  _name = "AddWall"
  _short_desc = "Add wall with holder"

  def __init__(self, x, y, yaw,hl,hr,b):
    #x coordinate
    #y coordinate
    #yaw angle (rotation about z-axis
    #hl - wall holder on the left, values 0/1
    #hr - wall holder on the right, values 0/1
    #b - values 1/0, big or small wall to import

    #z axis
    z=0.1
    #half of pi
    pih = 1.5707963
    #half of wall_holder
    whx = 0.02
    why = 0.02
    if b==1:
      self.wall= PassiveObject('bham/data/objects/lg/wood_wall.blend','woodwall')
      self.wall.properties(Object = True)
      self.wall.translate(x,y,z)
      self.wall.rotate(0,0,yaw)
      wx = 0.02
      wy = 0.8
    else:
      self.wall= PassiveObject('bham/data/objects/lg/wood_wall_small.blend','wallsmall')
      self.wall.properties(Object = True)
      self.wall.translate(x,y,z)
      self.wall.rotate(0,0,yaw)
      wx = 0.02
      wy = 0.3

    if hl==1:
      yn = y-cos(yaw)*(why+wy)
      xn = x-sin(yaw)*(why+wy)
      self.holderl= PassiveObject('bham/data/objects/lg/wall_holder.blend','wh')
      self.holderl.properties(Object = True)
      self.holderl.translate(xn,yn,z)
      self.holderl.rotate(0,0,yaw)

    if hr==1:
      yn = y+cos(yaw)*(why+wy)
      xn = x+sin(yaw)*(why+wy)
      self.holderr= PassiveObject('bham/data/objects/lg/wall_holder.blend','wh')
      self.holderr.properties(Object = True)
      self.holderr.translate(xn,yn,z)
      self.holderr.rotate(0,0,yaw)
