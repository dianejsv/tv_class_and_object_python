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
    def setChannel(self, channel):
        if self.on and (1 <= channel <= 120):  # Sets channel if TV is turned on
            self.channel = channel

# Method to sets the current volume
    def getVolume(self):
        return self.volumelevel

# Method that will set new volume
    def setVolume(self, volume):
        if self.on and (1 <= volume <= 7):
            self.volumelevel = volume

# Method that increments channel number by 1