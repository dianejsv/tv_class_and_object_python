# Test drive
# Import the TV class
from tv import TV


# Define TestTV
def test_tv():
    # Create two objects
    tv1 = TV()
    tv2 = TV()

# Turn on tv1 and set its channel to 30 and volume to 3
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

# Turn on tv2 and set its channel to 3 and volume to 2
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
    
# ANSI escape codes for purple and bold
# Print the states of tv1 and tv2 in purple and bold
# Run the test