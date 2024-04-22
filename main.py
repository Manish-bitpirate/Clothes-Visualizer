import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# camera feed
cap = cv2.VideoCapture(0)
# adds PoseDetector to the feed
detector = PoseDetector()


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
        pass
    
    #feed name
    cv2.imshow("Live", img)
    
    #exit statement
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
