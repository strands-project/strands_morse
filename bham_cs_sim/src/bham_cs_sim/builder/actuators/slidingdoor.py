from morse.builder.creator import ActuatorCreator

class SlidingDoor(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "bham_cs_sim.actuators.slidingdoor.SlidingDoor",\
                                 "SlidingDoor")

