from morse.builder.creator import ActuatorCreator

class SlidingDoor(ActuatorCreator):
    _classpath = "bham.actuators.slidingdoor.SlidingDoor"
    
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)

