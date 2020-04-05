import cv2
import imutils
image=cv2.imread("clear_img.bmp")
binary=cv2.imread("clear_img.bmp",cv2.IMREAD_UNCHANGED)
binary=binary[:-5,:]
cv2.imshow("binary",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
cnts=cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
print(cnts[0])
for c in cnts:
	M=cv2.moments(c) # M is just a dictionary
	cX=int(M["m10"]/M["m00"])
	cY=int(M["m01"]/M["m00"])
	cv2.drawContours(image,[c],-1,(0,255,0),2)
	cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

cv2.imshow("image",image)
cv2.waitKey(0)
