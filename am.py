import cv2
filepath ="daniel.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("my baby",image)
cv2.waitKey(0)
cv2.destroyAllWindows()