#!/usr/bin/env python3
"""
"""
import pymorse
import sys
import random
from operator import itemgetter


Z_DIST = 0.005
XY_DIST = 0.05

def on(obj1_name, obj2_name):
    bbox1 = eval(morse.rpc('simulation','get_object_bbox',obj1_name))
    bbox2 = eval(morse.rpc('simulation','get_object_bbox',obj2_name))

    # OBJ1

    # Calc x_min and x_max for obj1
    obj1_x_sorted = sorted(bbox1, key=itemgetter(0))
    obj1_x_min = obj1_x_sorted[0][0]
    obj1_x_max = obj1_x_sorted[7][0]

    # Calc y_min and y_max for obj1
    obj1_y_sorted = sorted(bbox1, key=itemgetter(1))
    obj1_y_min = obj1_y_sorted[0][1]
    obj1_y_max = obj1_y_sorted[7][1]

    # Calc z_min and z_max for obj1
    obj1_z_sorted = sorted(bbox1, key=itemgetter(2))
    obj1_z_min = obj1_z_sorted[0][2]
    obj1_z_max = obj1_z_sorted[7][2]

    # OBJ2

    # Calc x_min and x_max for obj2
    obj2_x_sorted = sorted(bbox2, key=itemgetter(0))
    obj2_x_min = obj2_x_sorted[0][0]
    obj2_x_max = obj2_x_sorted[7][0]

    # Calc y_min and y_max for obj2
    obj2_y_sorted = sorted(bbox2, key=itemgetter(1))
    obj2_y_min = obj2_y_sorted[0][1]
    obj2_y_max = obj2_y_sorted[7][1]

    # Calc z_max for obj2
    obj2_z_sorted_rev = sorted(bbox2, key=itemgetter(2))
    obj2_z_max = obj2_z_sorted_rev[7][2]

    obj1_xy_min_diff = min((obj1_x_max - obj1_x_min), (obj1_y_max - obj1_y_min)) / 2
        
    x = random.uniform(obj2_x_min + obj1_xy_min_diff + XY_DIST,
                       obj2_x_max - obj1_xy_min_diff - XY_DIST)

    y = random.uniform(obj2_y_min + obj1_xy_min_diff + XY_DIST,
                       obj2_y_max - obj1_xy_min_diff - XY_DIST)
    
    # place obj1 meters on top of obj2 
    z = obj2_z_max + (obj1_z_max - obj1_z_min) / 2 + Z_DIST

    pos =  eval(morse.rpc('simulation','transform_to_obj_frame', obj2_name, str([x,y,z])))
        
    # print("obj: ", obj1_name, " pos: " , pos)
    # print(" ", obj2_x_min + obj1_xy_min_diff + XY_DIST, "<= X <= ",  obj2_x_max - obj1_xy_min_diff - XY_DIST)
    # print(" ", obj2_y_min + obj1_xy_min_diff + XY_DIST, "<= Y <= ",  obj2_y_max - obj1_xy_min_diff - XY_DIST)
    
    return morse.rpc('simulation','set_object_pose',obj1_name,
                     str(pos),'[0.0, 0.0, 0.0, 1.0]')


def tum_kitchen_scene_1():
    on('cup1','Desk.002')
    on('cup2','Desk.004')
    on('cup3','Desk.005')              


if __name__ == '__main__':
    
    with pymorse.Morse() as morse:

        tum_kitchen_scene_1()


