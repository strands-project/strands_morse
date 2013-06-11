"""
Actuator for two-panel sliding doors. 

Requires the "left_panel" and "right_panel" to be set to the panel names in blender.
"""
import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.middleware.ros_request_manager import ros_action, ros_service,MorseAnyService
from morse.core import status
from morse.helpers.components import add_data, add_property

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
        print (self._properties)

#        self.left_positions=[.33096,.33096+0.5]
        self.left_positions=[.33096, -.16904-0.5]
        self.right_positions=[-.16904,-.16904-0.5]

        self.target_state = 0
        self.left_done=self.right_done=False



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

        left_bge = self.parent.bge_object.children[self.left_panel]
        right_bge = self.parent.bge_object.children[self.right_panel]
            
        # slide the doors....
        pos = left_bge.position[0]
        distance =  (self.left_positions[self.target_state] + self.bge_object.position[0]) - pos 
        direction = -1 if distance < 0 else 1
        
        if distance**2 > 0.00001:
            vx = direction * 0.2 / self.frequency # 0.9m/s
        else:
            vx=0
            self.left_done=True

        left_bge.position[0]+=vx

        pos = right_bge.position[0]
        distance =  (self.right_positions[self.target_state] + self.bge_object.position[0]) - pos 
        direction = -1 if distance < 0 else 1
        
        if distance**2 > 0.00001:
            vx = direction * 0.2 / self.frequency # 0.9m/s
        else:
            vx=0
            self.right_done=True

        right_bge.position[0]+=vx
        
        

        if self.left_done and self.right_done:
            self.local_data['current_state'] = self.target_state

