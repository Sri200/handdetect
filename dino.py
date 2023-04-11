import cv2
import pyautogui as pg
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=2)
video=cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    if hands:
        lmList=hands[0]
        up=detector.fingersUp(lmList)
        print(up)
        if up==[0,0,0,0,0]:
            cv2.putText(frame, "Finger Count : 0",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(455,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, "Accelerate", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,cv2.LINE_AA)
            pg.keyUp('right')
            pg.keyDown('left')
        if up==[0,1,0,0,0]:
            cv2.putText(frame, "Finger Count : 1",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            pg.press('left')
        if up==[0,1,1,0,0]:
            cv2.putText(frame, "Finger Count : 2",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            pg.press('right')
        if up==[0,1,1,1,0]:
            cv2.putText(frame, "Finger Count : 3",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if up==[0,1,1,1,1]:
            cv2.putText(frame, "Finger Count : 4",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if up==[1,1,1,1,1]:
            cv2.putText(frame, "Finger Count : 5",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, "Brake", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            pg.keyUp('left')
            pg.keyDown('right')
    cv2.imshow("Frame",frame)
    k = cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()
