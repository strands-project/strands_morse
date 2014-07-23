"""
Actuator for two-panel sliding doors. 

Requires the "left_panel" and "right_panel" to be set to the panel names in blender.
"""
import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.middleware.ros_request_manager import ros_action, ros_service
from morse.core import status
from morse.helpers.components import add_data, add_property
from math import sqrt

class SlidingDoor(morse.core.actuator.Actuator):
    _name = "SlidingDoor"
    _short_desc = ""


    add_data("current_state", 0, 'int', 'The current door state: 0=closed, 1=open')
    add_property("left_panel","","left_panel")
    add_property("right_panel","","right_panel")
    
    
    def __init__(self, obj, parent=None):
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)
        self.parent=parent

        self.target_state = 0
        self.left_done=self.right_done=False

        self.left_bge = self.parent.bge_object.children[self.left_panel]
        self.right_bge = self.parent.bge_object.children[self.right_panel]

        self.left_positions=[list(self.left_bge.localPosition),
                             list(self.parent.bge_object.children[self.left_panel+"_open"].localPosition)
                             ] 
        self.right_positions=[list(self.right_bge.localPosition),
                              list(self.parent.bge_object.children[self.right_panel+"_open"].localPosition)
                              ]


    @async_service
    def change_door_state(self, state):
        """ Change the door to open (1) or closed (0).
        """
        self.target_state = state
        self.left_done = False
        self.right_done = False

    def default_action(self):
        """ Main loop of the actuator.
        """
        # check if we have an on-going asynchronous task...
        if self.target_state == self.local_data['current_state']:
            self.completed(status.SUCCESS, self.local_data['current_state'])
#        print(self.left_positions)
            
        # LEFT DOOR
        pos = self.left_bge.localPosition
        direction=[a - b for a,b in zip(self.left_positions[self.target_state], list(pos)) ]
        distance=sqrt(sum( [ a**2 for a in direction ]))
        if distance > 5e-3:
            for i in range(0,3):
                direction[i] /= distance
            vel=[a * (0.2 / self.frequency) for a in direction]
            for i in range(0,3):
                self.left_bge.localPosition[i]+=vel[i]
        else:
            vel=[0,0,0]
            self.left_done=True

        # RIGHT DOOR
        pos = self.right_bge.localPosition
        direction=[a - b for a,b in zip(self.right_positions[self.target_state], list(pos)) ]
        distance=sqrt(sum( [ a**2 for a in direction ]))
        if distance > 5e-3:
            for i in range(0,3):
                direction[i] /= distance
            vel=[a * (0.2 / self.frequency) for a in direction]

            for i in range(0,3):
                self.right_bge.localPosition[i]+=vel[i]
        else:
            vel=[0,0,0]
            self.right_done=True
            

        if self.left_done and self.right_done:
            self.local_data['current_state'] = self.target_state

