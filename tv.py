# Class representing the Television
class TV:
    # Constructor
    def __init__(self):
        self.channel = 1
        self.volumelevel = 1
        self.on = False

# Method to turn on the TV
    def turnOn(self):
        self.on = True

# Method to turn off the TV
    def turnOff(self):
        self.on = False

# Method that sets the current channel
    def getChannel(self):
        return self.channel

# Method that will set new channel
# Method to sets the current volume
# Method that will set new volume