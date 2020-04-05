import cv2
import imutils

#cropping the board
img_loc="test_images/imc1.png"
img_loc2="test_images/imc2.png"

#load the positions
img=cv2.imread(img_loc) # just gives the 3-layered r,g,b matrix
nx_img=cv2.imread(img_loc2)
print(img.shape)
#crop the board
img_crpd=img[133:945,534:1342]
img2_crpd=nx_img[133:945,534:1342]
cv2.imwrite("cropped_board.png",img_crpd)
#simplify the image
	#---->first convert to grayscale
gray_img1=cv2.cvtColor(img_crpd,cv2.COLOR_BGR2GRAY)
gray_img2=cv2.cvtColor(img2_crpd,cv2.COLOR_BGR2GRAY)

diff_img_gray=abs(gray_img1-gray_img2)  #----- difference of grayscale images
#cv2.waitKey(0)

#----- it seems difference of grayscales is the best for my usage.
	#-----> so converting 'diff_gray' to binaries
easy_threshold=1
ret3,bin_from_gray=cv2.threshold(diff_img_gray,easy_threshold,255,cv2.THRESH_BINARY)
blr_bin=cv2.blur(bin_from_gray,(2,2))
ret4,clear_img=cv2.threshold(blr_bin,130,255,cv2.THRESH_BINARY)

#print(bin_from_gray)
edges=cv2.Canny(clear_img,0,255) #-----> gives just the edges of the closed area
print(clear_img)
#finding the centroid (could be done by writing definition.... but naah I am fine)
binary=clear_img
binary=binary[:-3,:]
cv2.imshow("binary",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
cnts=cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
print("the shape of cropped image is : ", binary.shape)
print(cnts[0])
for c in cnts:
	M=cv2.moments(c) # M is just a dictionary
	cX=int(M["m10"]/M["m00"])
	cY=int(M["m01"]/M["m00"])
	print(cX,cY)
	cv2.drawContours(img_crpd,[c],-1,(0,255,0),2)
	cv2.circle(img_crpd, (cX, cY), 7, (0, 0, 255), -1)
	cv2.putText(img_crpd, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

cv2.imshow("image",img_crpd)
cv2.waitKey(0)

