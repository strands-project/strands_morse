from morse.builder.creator import ActuatorCreator

class Platform(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "bham_cs_sim.actuators.platform.Platform",\
                                 "platform")

