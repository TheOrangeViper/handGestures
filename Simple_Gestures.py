#libraries
import mediapipe as mp
import cv2
import time
import math
from AppOpener import run
from FingerClass import Hand

leftCommand = False
rightCommand = False
startTimer = 0
endTimer = 0
#commands dictionary
leftHandCommands = {
    "index" : "Google Chrome",
    "middle" : "Stremio",
    "ring" : "Spotify"
}

rightHandCommands = {
    "index" : "Steam",
    "middle" : "Microsoft To Do",
    "ring" : "Google Assistant"
}

def leftHandGestures(hand):
    global leftCommand
    global startTimer
    #pre-calculations & ratios
    d = math.sqrt((hand.INDEX_FINGER_MCP.x-hand.PINKY_MCP.x)**2+(hand.INDEX_FINGER_MCP.y-hand.PINKY_MCP.y)**2)
    base = 1
    ratio = base/d
    thumb2index = math.sqrt((hand.INDEX_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.INDEX_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2middle = math.sqrt((hand.MIDDLE_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.MIDDLE_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2ring = math.sqrt((hand.RING_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.RING_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2pinky = math.sqrt((hand.PINKY_TIP.x-hand.THUMB_TIP.x)**2+(hand.PINKY_TIP.y-hand.THUMB_TIP.y)**2) * ratio

    #ThumbtoPinky START
    if 0 < thumb2pinky < 0.50:
        leftCommand = True
        startTimer = time.time()
    #If more than 3 seconds without command reset
    elif leftCommand == True:
        if time.time() - startTimer > 3: #counts 3 seconds
            leftCommand = False
    #ThumbtoRing
        elif 0.00 < thumb2index < 0.50:
            run(leftHandCommands["index"])
            leftCommand = False
    #ThumbtoMiddle
        elif 0.00 < thumb2middle < 0.50:
            run(leftHandCommands["middle"])
            leftCommand = False
    #ThumbtoIndex
        elif 0.00 < thumb2ring < 0.50:
            run(leftHandCommands["ring"])
            leftCommand = False

def rightHandGestures(hand):
    global rightCommand
    global startTimer
    #pre-calculations & ratios
    d = math.sqrt((hand.INDEX_FINGER_MCP.x-hand.PINKY_MCP.x)**2+(hand.INDEX_FINGER_MCP.y-hand.PINKY_MCP.y)**2)
    base = 1
    ratio = base/d
    thumb2index = math.sqrt((hand.INDEX_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.INDEX_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2middle = math.sqrt((hand.MIDDLE_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.MIDDLE_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2ring = math.sqrt((hand.RING_FINGER_TIP.x-hand.THUMB_TIP.x)**2+(hand.RING_FINGER_TIP.y-hand.THUMB_TIP.y)**2) * ratio
    thumb2pinky = math.sqrt((hand.PINKY_TIP.x-hand.THUMB_TIP.x)**2+(hand.PINKY_TIP.y-hand.THUMB_TIP.y)**2) * ratio

    #ThumbtoPinky START
    if 0 < thumb2pinky < 0.50:
        rightCommand = True
        startTimer = time.time()
    #If more than 3 seconds without command reset
    elif rightCommand == True:
        if time.time() - startTimer > 3: #counts 3 seconds
            rightCommand = False
    #ThumbtoRing
        elif 0.00 < thumb2index < 0.50:
            run(rightHandCommands["index"])
            rightCommand = False
    #ThumbtoMiddle
        elif 0.00 < thumb2middle < 0.50:
            run(rightHandCommands["middle"])
            rightCommand = False
    #ThumbtoIndex
        elif 0.00 < thumb2ring < 0.50:
            run(rightHandCommands["ring"])
            rightCommand = False
    



#drawing hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720) # creating a 1:1 ratio 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.4) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # BGR2RGB
        image = cv2.flip(image,1) # Image flip
        image.flags.writeable=False # Set flag doesn't allow us to write on image
       
        results = hands.process(image) # Making the detection
        image.flags.writeable = True # Set flag allows us to write on image

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # RGB2BGR

        if results.multi_handedness:
            for idx, hand_handedness in enumerate(results.multi_handedness):
                fingers = results.multi_hand_landmarks[0].landmark
                if hand_handedness.classification[0].label == "Left":
                    leftHand = Hand(fingers)
                    leftHandGestures(leftHand)
                if hand_handedness.classification[0].label == "Right":
                    rightHand = Hand(fingers)
                    rightHandGestures(rightHand)
                    
        # #displaying hand mesh
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        
        cv2.imshow("Hand Tracking", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
# cv2.destroyAllWindows()

#