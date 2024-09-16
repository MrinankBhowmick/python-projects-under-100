import cv2
img = cv2.imread("boom.jpg")
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gr)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(gr,invertedblur,scale = 256.0)
cv2.imwrite("sketch.jpg",sketch)
cv2.waitKey(0)