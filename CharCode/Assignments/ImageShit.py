from PIL import Image

import cv2
#Read Image
img = cv2.imread("C:\\Users\\ayych\\Pictures\\Peoples_nudes\\bunk.PNG")
#Display Image
cv2.imshow("C:\\Users\\ayych\\Pictures\\Peoples_nudes\\bunk.PNG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('graytest.jpg',gray)
