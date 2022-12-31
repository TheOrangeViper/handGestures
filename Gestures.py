#libraries
import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import uuid
import os
import time
import inspect
import matplotlib.pyplot as plt
import math
from AppOpener import run

triangleFile = open("triangle.txt","a")
lineFile = open("line.txt","a")

start = 0
measurements = []

command = False

#creating a function

def isInList(s,l):
    len_s = len(s) #so we don't recompute length of s on every iteration
    return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))


def leftHandGestures(lst):
    global command

    
    WRIST = lst.landmark[0]
    THUMB_CMC = lst.landmark[1]
    THUMB_MCP= lst.landmark[2]
    THUMB_IP = lst.landmark[3]
    THUMB_TIP = lst.landmark[4]
    INDEX_FINGER_MCP = lst.landmark[5]
    INDEX_FINGER_PIP = lst.landmark[6]
    INDEX_FINGER_DIP = lst.landmark[7]
    INDEX_FINGER_TIP = lst.landmark[8]
    MIDDLE_FINGER_MCP = lst.landmark[9]
    MIDDLE_FINGER_PIP = lst.landmark[10]
    MIDDLE_FINGER_DIP = lst.landmark[11]
    MIDDLE_FINGER_TIP = lst.landmark[12]
    RING_FINGER_MCP = lst.landmark[13]
    RING_FINGER_PIP = lst.landmark[14]
    RING_FINGER_DIP = lst.landmark[15]
    RING_FINGER_TIP = lst.landmark[16]
    PINKY_MCP = lst.landmark[17]
    PINKY_PIP = lst.landmark[18]
    PINKY_DIP = lst.landmark[19]
    PINKY_TIP = lst.landmark[20]



def rightHandGestures(lst):
    global command
    WRIST = lst.landmark[0]
    THUMB_CMC = lst.landmark[1]
    THUMB_MCP= lst.landmark[2]
    THUMB_IP = lst.landmark[3]
    THUMB_TIP = lst.landmark[4]
    INDEX_FINGER_MCP = lst.landmark[5]
    INDEX_FINGER_PIP = lst.landmark[6]
    INDEX_FINGER_DIP = lst.landmark[7]
    INDEX_FINGER_TIP = lst.landmark[8]
    MIDDLE_FINGER_MCP = lst.landmark[9]
    MIDDLE_FINGER_PIP = lst.landmark[10]
    MIDDLE_FINGER_DIP = lst.landmark[11]
    MIDDLE_FINGER_TIP = lst.landmark[12]
    RING_FINGER_MCP = lst.landmark[13]
    RING_FINGER_PIP = lst.landmark[14]
    RING_FINGER_DIP = lst.landmark[15]
    RING_FINGER_TIP = lst.landmark[16]
    PINKY_MCP = lst.landmark[17]
    PINKY_PIP = lst.landmark[18]
    PINKY_DIP = lst.landmark[19]
    PINKY_TIP = lst.landmark[20]

    # #distance between two points
    d = math.sqrt((INDEX_FINGER_MCP.x-PINKY_MCP.x)**2+(INDEX_FINGER_MCP.y-PINKY_MCP.y)**2)
    base = 1
    ratio = base/d
    
    thumb2index = math.sqrt((INDEX_FINGER_TIP.x-THUMB_TIP.x)**2+(INDEX_FINGER_TIP.y-THUMB_TIP.y)**2)
    thumb2pinky = math.sqrt((PINKY_TIP.x-THUMB_TIP.x)**2+(PINKY_TIP.y-THUMB_TIP.y)**2)

    measurement = thumb2index*ratio
    starterMeasurement = thumb2pinky*ratio

    if 0 < starterMeasurement < 0.50:
        command = True
        measurements.clear()
    
    if command == True:
        #adding measurements
        if 0.00 < measurement < 0.50:
            if len(measurements) == 0:
                measurements.append(0)
            elif measurements[-1] != 0:
                measurements.append(0)
        if 0.50 < measurement < 1.15:
            if len(measurements) == 0:
                measurements.append(1)
            elif measurements[-1] != 1:
                measurements.append(1)
        if 1.15 < measurement < 1.90:
            if len(measurements) == 0:
                measurements.append(2)
            elif measurements[-1] != 2:
                measurements.append(2)
        if 1.90 < measurement < 2.65:
            if len(measurements) == 0:
                measurements.append(3)
            elif measurements[-1] != 3:
                measurements.append(3)
        if 2.90 < measurement < 3.10: #18 cm this will clear the measurements list
            measurements.clear()


    print("\n")
    print(measurements)

    #checking gesture
    a = [0,1,2,3]
    b = [0,1,2,1]
    c = [3,2,1,0]

    if isInList(a,measurements):
        print("Opening Discord")
        run("Discord")
        measurements.clear()
        command = False
    elif isInList(b,measurements):
        print("Opening Spotify")
        run("Spotify")
        measurements.clear()
        command = False
    elif isInList(c,measurements):
        print("Opening Google Chrome")
        run("Google Chrome")
        measurements.clear()
        command = False
    # elif isInList(d,measurements):
    #     print("Opening Stremio")
    #     run("Stremio")
    #     measurements.clear()
    #     command = False
    # elif isInList(e,measurements):
    #     print("Opening To Do Microsoft")
    #     run("Microsoft To Do")
    #     measurements.clear()
    #     command = False
    # elif isInList(f,measurements):
    #     print("Opening Parsec")
    #     run("Parsec")
    #     measurements.clear()
    #     command = False

    if len(measurements) == 10:
        measurements.clear()
        command = False

#drawing hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# help(mp.solutions.hands.Hands)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 15)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.4) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        # BGR2RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #image flip
        image = cv2.flip(image,1)

        # Set flag doesn't allow us to write on image
        image.flags.writeable=False
        
        #making the detection
        results = hands.process(image)
        
        # Set flag allows us to write on image
        image.flags.writeable = True
        
        # RGB2BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if start == 0:
            start = time.time()
        if results.multi_handedness:
            end = time.time()
            if (end-start) > 1.5:
                measurements.clear()
            start = 0
            for idx, hand_handedness in enumerate(results.multi_handedness):
                if hand_handedness.classification[0].label == "Left":
                    leftHandGestures(results.multi_hand_landmarks[0])
                if hand_handedness.classification[0].label == "Right":
                    rightHandGestures(results.multi_hand_landmarks[0])
        # #displaying hand mesh
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        
        cv2.imshow("Hand Traking", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

lineFile.close()
triangleFile.close()
cap.release()
# cv2.destroyAllWindows()

#