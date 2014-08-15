#! /usr/bin/env morseexec

"""
Brings in the CS building simulation environment from bham and uses ScitosA5.
"""

import sys
import subprocess 
import os
import random

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

robot = Scitosa5(with_cameras = Scitosa5.WITHOUT_DEPTHCAMS)

env = Environment('indoors-1/indoor-1')
