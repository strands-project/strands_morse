"""
Actuator that moves the lift platform inside the shaft to a given floor. 

Interface is via service "move_to_floor(floor_number)", floor_number is 0:3
"""
import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

T=0.01**2 # max tollerence 1mm for position of platform

class Platform(morse.core.actuator.Actuator):
    _name = "Platform"
    _short_desc = "Move the elevator platform to given level"

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description
    #add_data('target_floor', 0, 'int', 'The floor to move to')
    add_data('current_floor', 0, 'int', 'The current floor. Read 999 if between floors.')


    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)

        # Do here actuator specific initializations

        self.local_data['current_floor'] = 0
        self.target_floor=0

        self.lift_cage= parent.bge_object.children['LiftCage']
        self.floor_height={-1:1.5, 0:4.5, 1:7.5, 2:10.5}

   


    @service
    def get_floor(self):
        """
        Return the current floor number
        """

        return self.local_data['current_floor']

    
    @interruptible
    @async_service
    def move_to_floor(self, floor):
        """ Move the platform to the given floor then return
        """
        self.target_floor = floor

        
           
    def default_action(self):
        """ Main loop of the actuator.

        Implements the component behaviour
        """

        # check if we have an on-going asynchronous task...
        if self.target_floor == self.local_data['current_floor']:
            self.completed(status.SUCCESS, self.local_data['current_floor'])

        # move the platform at given speed to target level.
        pos = self.lift_cage.localPosition
        distance =  self.floor_height[self.target_floor]  - pos[2]
        direction = -1 if distance < 0 else 1
        
        if distance**2 > T:
            vz = direction * 0.9 / self.frequency # 0.9m/s
        else:
            vz=0
            self.local_data['current_floor'] = self.target_floor

        self.lift_cage.localPosition[2]+=vz
        
        
