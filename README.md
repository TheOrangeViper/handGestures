# handGestures

Using mediapipe customizable hand gestures are made.

NEEDED LIBRARIES:

- mediapipe
- cv2 (opencv)
- time
- math
- AppOpener

import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import math
from AppOpener import run
from FingerClass import Finger, Hand

Gestures.py is the original version of the app, it is intended for more than 24 actions. The app is not finished, and is not capable more than 3 actions (limited to the right hand and the index finger to thumb command).

Simple_Gestures.py is the second version of the app, it is intended for more than 8 gestures (this will be upgraded later to 16 or possibly 24 by using the joints of the fingers as an additional gestures). This Simple_Gestures.py requires the FingerClass.py which holds two classes; the Hand Class and the Finger Class.
