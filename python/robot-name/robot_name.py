import datetime
from string import ascii_uppercase

class Robot(object):
    def __init__(self):
        self.name=NewName()
    
    def reset(self):
        self.name=NewName()


def NewName():
    ALPHABET = zip(ascii_uppercase)
    nm=ALPHABET[datetime.datetime.now().hour][0]+ALPHABET[datetime.datetime.now().minute % 26][0]+str(datetime.datetime.now().microsecond % 1000)
    print nm
    return nm


if __name__ == '__main__':  
    robot = Robot()
    robot.reset()
       