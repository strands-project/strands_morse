from morse.builder.creator import ActuatorCreator

class Platform(ActuatorCreator):
    _classpath = "bham.actuators.platform.Platform"

    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)

