import cv2
import mediapipe as mp

def hands():
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands 
    hands = mpHands.Hands()   
    mpDraw = mp.solutions.drawing_utils  
    while True:
        success, img = cap.read() 
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        lmList = []
        if results.multi_hand_landmarks: 
            for handlandmark in results.multi_hand_landmarks:
                for id,lm in enumerate(handlandmark.landmark):
                    h,w,_ = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
                mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
        cv2.imshow('Image',img)
        if cv2.waitKey(1) & 0xff==ord(' '):
            break      
    return lmList