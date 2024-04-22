import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# camera feed
cap = cv2.VideoCapture(0)
# adds PoseDetector to the feed
detector = PoseDetector()

#import shirts
shirts = "assets/img"
listShirts = os.listdir(shirts)

#live camera feed
while True:
    #reads the feed 
    success, img = cap.read()
    # and applies landmark points
    img = detector.findPose(img)
    #gets landmark list and bounding box info
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    
    #if anything in bounding box or landmark list detected
    if lmList:
        #extracting torso points
        lm12 = lmList[12][1:3]
        
        #join and use imported shirts path in feed
        shirtImg = cv2.imread(os.path.join(shirts, listShirts[0]), cv2.IMREAD_UNCHANGED)
        
        #debug
        # cv2.imshow("Image", shirtImg)
      
# defective
        #Overlay the shirts over the user in the feed
        try:
            img = cvzone.overlayPNG(img, shirtImg, lm12)
            # img = cv2.resize(shirtImg, (0,0), None, 0.5, 0.5)
            # img = cv2.resize(shirtImg, (0,0), fx=0.4, fy=0.4) 
            print("Try")
        except:
            print("except")
            pass
        else:
            print("Working perfectly")
            
    # feed name
    cv2.imshow("Live", img)
    
    #exit statement
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
