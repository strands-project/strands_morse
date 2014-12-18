#!/usr/bin/env python3
"""
Simple API for placing objects on tables according to directional spatial
relations.
"""
import pymorse
import sys
import random
import json
import math
import numpy
import errno 
import getopt
from operator import itemgetter
import qsr
import os


from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


            
def remove_objects(objs):
    for o in objs:
        morse.rpc('simulation','set_object_pose', o, str([0,0,0]),str([1,0,0,0]))

def quaternion_multiply(q1, q2):
    return [q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
            q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
            q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
            q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]] 

        
def load_scene(scn, target, offset=0):

    target_pose = json.loads(morse.rpc('simulation','get_object_pose',
                                       target))
    target_pos = target_pose[0]
    target_ori =  target_pose[1]

    
    table_pos = scn['position']['table']
    #table_ori = scn['orientation']['table'] 

    for o in scn['objects']:

        obj_pos = scn['position'][o]

        x = float(obj_pos[0]) - float(table_pos[0])
        y = float(obj_pos[1]) - float(table_pos[1])
        z = float(obj_pos[2]) - float(table_pos[2])

        pos =  morse.rpc('simulation','transform_to_obj_frame', target, str([x,y,z]))

        orientation = scn['orientation'][o]

        new_orientation = quaternion_multiply(target_ori,orientation)

        if (o == 'monitor'):
            cmd = 'rosparam set /qsr_landmark/id%i/pose "[%f, %f, %f, %f, %f, %f, %f]"' % (offset+1, float(pos[0] + 1.35), float(pos[1]) - 0.65, float(pos[2]), float(new_orientation[0]), float(new_orientation[1]), float(new_orientation[2]), float(new_orientation[3]))
            print('Run:', cmd)
            os.system(cmd)

        
        # set pose
        morse.rpc('simulation','set_object_pose',obj_name(o,offset), str(pos), str(new_orientation))


    return scn['objects']

def delete_scene(scn,offset):

    objs = list()
    for o in scn['objects']:
        objs.append(obj_name(o,offset))


    remove_objects(objs)

    

def obj_name(obj, offset):

    SET_SIZE = 7
    
    part = obj.split('.')

    if len(part)==1:
        postfix = SET_SIZE * offset
        if postfix == 0:
            return part[0]
        
    else:
        postfix = SET_SIZE * offset + int(part[1])

    if (postfix < 10):
        return part[0] + '.00' + str(postfix) 
    else:
        return part[0] + '.0' + str(postfix)
    
            
    
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def help_msg():
    return """
  Usage: scene_loader.py [-h] add|del <scences_file> <scene_number> <set_of_obj_models> <target_plane>

    add|del            add or delete a scene
    scenes_file        file that contains all scenes
    scene_number       scene that is added or deleted
    sef_of_obj_models  set of blender object models
    target_plane       object on which the scene is generated

    -h, --help for seeing this msg
"""

morse = None

if __name__ == "__main__":
    argv = None
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)

        if ('-h','') in opts or ('--help', '') in opts:
            raise Usage(help_msg())

        with open(args[1]) as scn_file:    
            scenes = json.load(scn_file)

            with ignored(IOError):
                    
                with pymorse.Morse() as morse:

                    if args[0] == 'add':
                        
                        
                        load_scene(scenes[int(args[2])][1], args[3], int(0))
                        #load_scene(scenes[int(args[4])][1], args[5], int(1))
                        #load_scene(scenes[int(args[6])][1], args[7], int(2))

                        input('Please press any key to continue.')

                        #delete from parameter server
                        for i in range(1,4):
                            cmd = 'rosparam delete /qsr_landmark/id%i/pose' % (i)
                            print('Run:', cmd)
                            os.system(cmd)
                        
                        delete_scene(scenes[int(args[2])][1],int(0))
                        #delete_scene(scenes[int(args[4])][1],int(1))
                        #delete_scene(scenes[int(args[6])][1],int(2))
                        
                    elif args[0] == 'del':
                        delete_scene(scenes[int(args[2])][1],int(args[3]))
                    else:
                        raise Usage('use either add or del')
                    #remove_objects(objs)
                            
    except Usage as err:
        print(err.msg)
        print("for help use --help")
        #return 2

# AAAI
        
# SCENES
# [143,242, 30,
#  470, 378, 273,
#  231, 174, 191,
#  19, 184, 156,
#  25, 275, 111,
#  213,464, 351,
#  316, 188, 7,
#  4, 271, 292,
#  89, 235, 339,
#  287, 86,330]


# TABLES
# [1, 5, 7]
# [4, 6, 3]
# [2, 5, 7]
# [3, 1, 6]
# [5, 2, 6]
# [5, 4, 1]
# [4, 3, 1]
# [4, 7, 5]
# [6, 3, 2]
# [7, 2, 3]

