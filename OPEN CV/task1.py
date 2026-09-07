import os
import cv2
import numpy as np
import cv2.aruco as aruco
def findArucoMarkers(img,markersize=6,totalmarkers=250,draw=True):
	imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	getkey=getattr(aruco,f'DICT_{markersize}X{markersize}_{totalmarkers}')
	arucodict=aruco.getPredefinedDictionary(getkey)
	arucoparam=aruco.DetectorParameters()
	detector=aruco.ArucoDetector(arucodict,arucoparam)
	box,ids,rejected=detector.detectMarkers(imggray)
	print(ids)
	if ids is not None:
		if draw:
			aruco.drawDetectedMarkers(img,box,ids)
		for i in range(len(ids)):
			marker_id=int(ids[i])
			pts=box[i][0]
			a=pts[0]
			b=pts[1]
			c=pts[2]
			d=pts[3]
			x=int((a[0]+b[0]+c[0]+d[0])/4)
			y=int((a[1]+b[1]+c[1]+d[1])/4)
			print(f"Marker ID:{marker_id}|Center:({x},{y})")
			cv2.circle(img,(x,y),5,(0,0,255),-1)
			cv2.putText(img,f"ID:{marker_id}",(x-30,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
			cv2.putText(img,f"({x},{y})",(x-30,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
	return img
def main():
	cap=cv2.VideoCapture(0)
	while True:
		success,img=cap.read()
		if not success:
			break
		findArucoMarkers(img)
		cv2.imshow("Output",img)
		if cv2.waitKey(1)&0xFF==ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
if __name__=="__main__":
	main()
