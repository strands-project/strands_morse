#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham_cs_sim and uses ScitosA5.
"""

import sys
import subprocess 
import os

# Add the bham_cs_sim to the python path and to MORSE_RESOURCE_PATH
pack=subprocess.Popen(["rospack","find","bham_cs_sim"],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
bham_cs_path=pack.stdout.read().decode("utf-8").strip()
sys.path.append(os.path.join(bham_cs_path,"src"))
resources=os.getenv('MORSE_RESOURCE_PATH',"")
os.environ["MORSE_RESOURCE_PATH"]=resources+":"+os.path.join(bham_cs_path,"data")


from morse.builder import *
from strands_sim.builder.robots import Scitosa5
from bham_cs_sim.builder.robots import Elevator

robot = Scitosa5()
robot.translate(x=-1.35, y=0.56, z=7.5)

lift = Elevator()
lift.translate(3.81419,2.51356,0)

# At lowest level, the lift is controlled through a socket interface
# by lift_controller.py, which in turn provides a ros interface...
lift.add_default_interface('socket')


# Set the environment
model_file=os.path.join(bham_cs_path,'data/CS_Building.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

