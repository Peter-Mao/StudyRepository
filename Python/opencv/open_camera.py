import cv2
cap = cv2.VideoCapture(0)
while True:
	ret,frame = cap.read()
	cv2.imshow('frame',frame)
	c = cv2.waitKey(1)
	if c == ord('q'):
		break
cap.realease()
cv2.destroyAllWindows()
