class Hand:
    def __init__(self, fingers):
        self.WRIST = Finger(fingers[0])
        self.THUMB_CMC = Finger(fingers[1])
        self.THUMB_MCP= Finger(fingers[2])
        self.THUMB_IP = Finger(fingers[3])
        self.THUMB_TIP = Finger(fingers[4])
        self.INDEX_FINGER_MCP = Finger(fingers[5])
        self.INDEX_FINGER_PIP = Finger(fingers[6])
        self.INDEX_FINGER_DIP = Finger(fingers[7])
        self.INDEX_FINGER_TIP = Finger(fingers[8])
        self.MIDDLE_FINGER_MCP = Finger(fingers[9])
        self.MIDDLE_FINGER_PIP = Finger(fingers[10])
        self.MIDDLE_FINGER_DIP = Finger(fingers[11])
        self.MIDDLE_FINGER_TIP = Finger(fingers[12])
        self.RING_FINGER_MCP = Finger(fingers[13])
        self.RING_FINGER_PIP = Finger(fingers[14])
        self.RING_FINGER_DIP = Finger(fingers[15])
        self.RING_FINGER_TIP = Finger(fingers[16])
        self.PINKY_MCP = Finger(fingers[17])
        self.PINKY_PIP = Finger(fingers[18])
        self.PINKY_DIP = Finger(fingers[19])
        self.PINKY_TIP = Finger(fingers[20])

class Finger:
    def __init__(self, finger):
        self.command = []
        self.finger = finger
        self.x = finger.x
        self.y = finger.y
        self.z = finger.z