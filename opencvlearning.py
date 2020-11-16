import cv2

print("package imported {0}".format(cv2.__version__))

img = cv2.imread(r"C:\Users\atlas\Desktop\download(3).jpg")
cv2.imshow("window", img)
cv2.waitKey()