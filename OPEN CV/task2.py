import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def empty(a):
	pass
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,420)
cv2.createTrackbar("Huemin","trackbars",70,179,empty)
cv2.createTrackbar("Huemax","trackbars",89,179,empty)
cv2.createTrackbar("Satmin","trackbars",9,255,empty)
cv2.createTrackbar("Satmax","trackbars",184,255,empty)
cv2.createTrackbar("Valmin","trackbars",0,255,empty)
cv2.createTrackbar("Valmax","trackbars",181,255,empty)
prevx=None
prevy=None
while True:
	success,img=cap.read()
	imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	huemin=cv2.getTrackbarPos("Huemin","trackbars")
	huemax=cv2.getTrackbarPos("Huemax","trackbars")
	satmin=cv2.getTrackbarPos("Satmin","trackbars")
	satmax=cv2.getTrackbarPos("Satmax","trackbars")
	valmin=cv2.getTrackbarPos("Valmin","trackbars")
	valmax=cv2.getTrackbarPos("Valmax","trackbars")
	lower=np.array([huemin,satmin,valmin])
	upper=np.array([huemax,satmax,valmax])
	mask=cv2.inRange(imghsv,lower,upper)
	imgresult=cv2.bitwise_and(img,img,mask=mask)
	contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		area=cv2.contourArea(cnt)
		if area>500:
			x,y,w,h=cv2.boundingRect(cnt)
			cx=x+w//2
			cy=y+h//2
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.circle(img,(cx,cy),5,(0,0,255),-1)
			direction="Still"
			if prevx is not None:
				dx=cx-prevx
				dy=cy-prevy
				if abs(dx)>abs(dy):
					if dx>10:
						direction="Right"
					elif dx<-10:
						direction="Left"
				else:
					if dy>10:
						direction="Down"
					elif dy<-10:
						direction="Up"
			print(f"Coordinates: ({cx},{cy}) | Direction: {direction}")
			cv2.putText(img,f"({cx},{cy})",(cx,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
			cv2.putText(img,direction,(x,y+h+25),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
			prevx=cx
			prevy=cy
	cv2.imshow("Masked",mask)
	cv2.imshow("Result",imgresult)
	cv2.imshow("Real",img)
	cv2.imshow("Output",imghsv)
	if cv2.waitKey(1)&0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
