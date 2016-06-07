#! /usr/bin/env morseexec

"""
Simple environemnt with ScitosA5.
"""

import sys
import subprocess
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
import threading

class SimSetup():
    #from bham.builder.robots import Elevator

    def __init__(self):
        self.trigger()


    def trigger(self):
        # Set the environment
        model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/aloof.blend')
        env = Environment(model_file,fastmode=False)
        env.place_camera([10, -6.0, 15.0])
        env.aim_camera([0, 0, 0.00])

        monitor_table_top = 1.15 #higher value: higher off the table, default: 2
        object_table_top = 0.95 #higher value: higher off the table, default: 2

        #robot = Scitosa5()
        robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)
        robot.translate(x=3.3,y=-9,z=0.0)
        robot.rotate(z=3.14)

        docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
        docking_station.properties(Object = True)
        docking_station.properties(ChargingZone = True)
        docking_station.translate(8,-4.12,0.335)
        docking_station.rotate(0,0,1.57)

        docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
        docking_station_label.properties(Object = True)
        docking_station_label.translate(8,-4.02,1.75)
        docking_station_label.rotate(1.57,0,0)

        ## WEST ROOM
        table1 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table1.properties(Object = True, Type = 'Table')
        table1.translate(x=0.7, y=-3, z=0.0)
        table1.rotate(0,0,math.pi)

        table2 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table2.properties(Object = True, Type = 'Table')
        table2.translate(x=0.7,y=-9.0,z=0.0)
        table2.rotate(0,0,math.pi)

        ##### NORTH ROOM

        north_monitor_a = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
        north_monitor_a.properties(Object = True, Type = 'north_monitor_a')
        north_monitor_a.translate(x=10.4194,y=-0.63546,z=monitor_table_top)
        north_monitor_a.rotate(0,0,-1.9)

        north_monitor_b = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
        north_monitor_b.properties(Object = True, Type = 'north_monitor_b')
        north_monitor_b.translate(x=9.69054,y=-0.6213,z=monitor_table_top)
        north_monitor_b.rotate(0,0,-1.4)

        north_keyboard = PassiveObject('strands_sim/robots/strands_objects.blend','keyboard')
        north_keyboard.properties(Object = True, Type = 'north_keyboard')
        north_keyboard.translate(x=9.99569,y=-1.14737,z=object_table_top)
        north_keyboard.rotate(0,0,4.7)

        north_mouse = PassiveObject('strands_sim/robots/strands_objects.blend','mouse')
        north_mouse.properties(Object = True, Type = 'north_mouse')
        north_mouse.translate(x=10.49005,y=-1.09195,z=object_table_top)
        north_mouse.rotate(1.0,0,-1.053)


        ###### NORTHWEST ROOM (kitchen)

        north_west_monitor = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
        north_west_monitor.properties(Object = True, Type = 'north_west_monitor')
        north_west_monitor.translate(x=0.7,y=-2.96697,z=monitor_table_top)
        north_west_monitor.rotate(0,0,0)


        north_west_keyboard = PassiveObject('strands_sim/robots/strands_objects.blend','keyboard')
        north_west_keyboard.properties(Object = True, Type = 'north_west_keyboard')
        north_west_keyboard.translate(x=1.0,y=-2.99466,z=object_table_top)
        north_west_keyboard.rotate(0,0,0)


        ## KITCHEN SINK ##
        counter_top = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node73.visual')
        counter_top.properties(Object = True, Type = 'counter_top')
        counter_top.translate(x=17.06734,y=-0.31524,z=0.82641)
        counter_top.rotate(0,0,1.570)

        l_edge = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node72.visual')
        l_edge.properties(Object = True, Type = 'counter_top_left')
        l_edge.translate(x=18.08227,y=-0.30976,z=0.42349)
        l_edge.rotate(0,0,1.570)

        r_edge = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node72.visual')
        r_edge.properties(Object = True, Type = 'counter_top_right')
        r_edge.translate(x=16.03759,y=-0.30976,z=0.42349)
        r_edge.rotate(0,0,1.570)

        divider = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node72.visual')
        divider.properties(Object = True, Type = 'counter_top_right')
        divider.translate(x=16.44818,y=-0.53812,z=0.32808)
        divider.rotate(0,1.56,3.15)

        bottom = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node93.visual')
        bottom.properties(Object = True, Type = 'counter_bottom')
        bottom.translate(x=17.06734,y=-0.06524,z=0.0)
        bottom.rotate(0,0,1.57)

        sink = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node92.visual')
        sink.properties(Object = True, Type = 'sink')
        sink.translate(x=16.60285,y=-0.29638,z=0.84087)
        sink.rotate(0,0,1.57)

        tap = PassiveObject('environments/tum_kitchen/tum_kitchen','tap')
        tap.properties(Object = True, Type = 'tap')
        tap.translate(x=16.59032,y=-0.11176,z=0.8245)
        tap.rotate(0,0,3.7)

        fridge = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node3.visual')
        fridge.properties(Object = True, Type = 'fridge')
        fridge.translate(x=18.91756,y=-0.35535,z=0.67172)
        fridge.rotate(0,0,1.57)

        fridge_door = PassiveObject('environments/tum_kitchen/tum_kitchen','Cabinet_Door')
        fridge_door.properties(Object = True, Type = 'fridge_door')
        fridge_door.rotate(0,0,-1.57)
        fridge_door.translate(x=19.23001,y=-0.74,z=0.53)



        shelf_a = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node78.visual')
        shelf_a.properties(Object = True, Type = 'topshelf')
        shelf_a.translate(x=16.43681,y=-0.59,z=0.664)
        shelf_a.rotate(0,0,-1.57)

        shelf_b = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node78.visual')
        shelf_b.properties(Object = True, Type = 'middleshelf')
        shelf_b.translate(x=16.43681,y=-0.59,z=0.36574)
        shelf_b.rotate(0,0,-1.57)


        # big cupboard - near sink
        shelf_c = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node84.visual')
        shelf_c.properties(Object = True, Type = 'shelf_c')
        shelf_c.translate(x=17.13672,y=-0.59,z=0.45)
        shelf_c.rotate(0,0,-1.57)

        # big cupboard 2
        shelf_d = PassiveObject('environments/tum_kitchen/tum_kitchen','v1.node84.visual')
        shelf_d.properties(Object = True, Type = 'shelf_d')
        shelf_d.translate(x=17.75673,y=-0.59,z=0.45)
        shelf_d.rotate(0,0,-1.57)


        ###### WEST ROOM

        west_monitor = PassiveObject('strands_sim/robots/strands_objects.blend','monitor')
        west_monitor.properties(Object = True, Type = 'west_monitor')
        west_monitor.translate(x=0.7,y=-9,z=monitor_table_top)
        west_monitor.rotate(0,0,0)

        west_keyboard = PassiveObject('strands_sim/robots/strands_objects.blend','keyboard')
        west_keyboard.properties(Object = True, Type = 'west_keyboard')
        west_keyboard.translate(x=1.0,y=-9,z=object_table_top)
        west_keyboard.rotate(0,0,0)

        west_mouse = PassiveObject('strands_sim/robots/strands_objects.blend','mouse')
        west_mouse.properties(Object = True, Type = 'west_mouse')
        west_mouse.translate(x=1.2,y=-9.5,z=object_table_top)
        west_mouse.rotate(0,0,0)

        west_mug = PassiveObject('strands_sim/robots/strands_objects.blend','mug')
        west_mug.properties(Object = True, Type = 'west_cup')
        west_mug.translate(x=1.2,y=-8.5,z=object_table_top)
        west_mug.rotate(0,0,0)
        #west_mug.name = 'mug_1'


        ## SOUTH ROOM
        table3 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table3.properties(Object = True, Type = 'Table')
        table3.translate(x=10.14212, y=-10.12913,z=0.0)
        table3.rotate(0,0,math.pi*3/2)

        south_calculator = PassiveObject('strands_sim/robots/strands_objects.blend','calculator')
        south_calculator.properties(Object = True, Type = 'south_calculator')
        south_calculator.translate(x=9.80302,y=-9.66637,z=object_table_top)
        south_calculator.rotate(0,0,0)

        south_telephone = PassiveObject('strands_sim/robots/strands_objects.blend','telephone')
        south_telephone.properties(Object = True, Type = 'south_telephone')
        south_telephone.translate(x=10.68164,y=-10.45363,z=object_table_top)
        south_telephone.rotate(0,0,0)

        south_chair = PassiveObject('environments/indoors-1/indoor-1','red_heat')
        south_chair.properties(Object = True, Type = 'south_chair')
        south_chair.translate(x=8.82655,y=-10.09386,z=0.3)
        south_chair.rotate(0,0,-4.442)

    #    south_cabinet = PassiveObject('environments/tum_kitchen/tum_kitchen','Cabinet')
    #    south_cabinet.properties(Object = True, Type = 'south_cabinet')
    #    south_cabinet.translate(x=6.43451,y=-8.48305,z=0.00493)
        #south_cabinet.rotate(0,0,0)

        south_whiteboard = PassiveObject('environments/indoors-1/indoor-1','whiteboard')
        south_whiteboard.properties(Object = True, Type = 'south_whiteboard')
        south_whiteboard.translate(x=13.02505,y=-10.64416,z=0.3)
        south_whiteboard.rotate(0,0,0)


        ## NORTH ROOM
        table4 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table4.properties(Object = True, Type = 'Table')
        table4.translate(x=10.0,y=-0.7,z=0.0)
        table4.rotate(0,0,math.pi/2)

        # EAST WALL
        table5 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table5.properties(Object = True, Type = 'Table')
        table5.translate(x=19.3,y=-3.0,z=0.0)

        table6 = PassiveObject('environments/human_tut/tutorial_scene','Table')
        table6.properties(Object = True, Type = 'Table')
        table6.translate(x=19.3,y=-9.0,z=0.0)



if __name__ == "__main__":
    s = SimSetup()

