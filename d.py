import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)
#img = cv2.imread('capturepics/2024-01-05-16-02.jpg',1)
img = cv2.line(img,(0,0),(255,255),(0,255,0),15)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
img = cv2.circle(img,(345,32),50, (255,0,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"Azam",(500,500),font,4,(255,255,0),10,cv2.LINE_AA)
cv2.imshow('Image',img)
k = cv2.waitKey(0)
if k==99:
	cv2.destroyAllWindows()
