#!/usr/bin/env python3.3
"""
Simple script for converting generated scenes into a slightly different JSON format defined here:
https://github.com/strands-project/strands_qsr/wiki/Data-sets
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


class BBox():
    """ Bounding box of an object with getter functions.
    """
    def __init__(self, bbox):
        # Calc x_min and x_max for obj1
        x_sorted = sorted(bbox, key=itemgetter(0))
        self.x_min = x_sorted[0][0]
        self.x_max = x_sorted[7][0]

        # Calc y_min and y_max for obj
        y_sorted = sorted(bbox, key=itemgetter(1))
        self.y_min = y_sorted[0][1]
        self.y_max = y_sorted[7][1]

        # Calc z_min and z_max for obj
        z_sorted = sorted(bbox, key=itemgetter(2))
        self.z_min = z_sorted[0][2]
        self.z_max = z_sorted[7][2]
        
    def get_x_min(self):
        return self.x_min

    def get_x_max(self):
        return self.x_max

    def get_y_min(self):
        return self.y_min

    def get_y_max(self):
        return self.y_max

    def get_z_min(self):
        return self.z_min

    def get_z_max(self):
        return self.z_max

                        
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def help_msg():
    return """
  Usage: scene_converter.py [-h] <input_file> <output_file>

    input_file         scenes to be converted
    output_file        converted scenes

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

        if ('-h','') in opts or ('--help', '') in opts or len(args) is not 2:
            raise Usage(help_msg())

        with open(args[0]) as in_file:
            with open(args[1],'w') as out_file:    
                scenes = json.load(in_file)
                conv = list() 

                # get table info (only once)
                table_bbox = BBox(scenes[0][1]['bbox']['table'])
                x_dim = table_bbox.get_x_max() - table_bbox.get_x_min()
                y_dim = table_bbox.get_y_max() - table_bbox.get_y_min()
                z_dim = table_bbox.get_z_max() - table_bbox.get_z_min()
                #print("Table dimensions (x,y,z):",x_dim,y_dim,z_dim)

                table_pos = scenes[0][1]['position']['table']
                print("Table position (x,y,z):",table_pos)

                # the origin of the table is at the bottom (ground) 
                table_corner = [table_pos[0] - x_dim/2,
                                table_pos[1] - y_dim/2,
                                table_pos[2] + z_dim]

                print("Table corner (x,y,z) (NEW ORIGIN)", table_corner)
                
                for s in scenes:

                    pos = dict()
                    ori = dict()
                    bbox = dict()
                    objT = dict()
                    for o in s[1]['objects']:
                        pos[o] = [ s[1]['position'][o][0] - table_corner[0],
                                   s[1]['position'][o][1] - table_corner[1],
                                   s[1]['position'][o][2] - table_corner[2]]

                        ori[o] = s[1]['orientation'][o]

                        new_bbox = list()
                        for c in s[1]['bbox'][o]:
                            new_bbox.append([ c[0] - table_corner[0],
                                              c[1] - table_corner[1],
                                              c[2] - table_corner[2]])
                        bbox[o] = new_bbox

                        objT[o] = s[1]['type'][o]

                    conv.append({'scene_id' : s[0],
                                 'objects'  : s[1]['objects'],
                                 'position' : pos,
                                 'orientation' : ori,
                                 'bbox' : bbox,
                                 'type' : objT
                                 })
                    #print("Convert", s[0])

                out_file.write(json.dumps(conv, out_file, indent=2))
                    
                print("Done. Converted", len(conv), "scene(s).")
            
    except Usage as err:
        print(err.msg)
        print("for help use --help")
        #return 2


