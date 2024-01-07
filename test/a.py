import cv2

img = cv2.imread('capturepics/2024-01-05-16-02.jpg',1)
cv2.imshow('Image',img)
k = cv2.waitKey(0)
if k==99:
	cv2.destroyAllwindows()
else:
	cv2.imwrite('latest.png',img)
	cv2.destroyAllwindows()
