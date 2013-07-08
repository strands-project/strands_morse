from morse.builder.creator import ActuatorCreator

class Platform(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "bham.actuators.platform.Platform",\
                                 "platform")

