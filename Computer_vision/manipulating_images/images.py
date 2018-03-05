import cv2

img = cv2.imread("galaxy.jpg", 1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img, (img.shape[0]//3, img.shape[1]//3))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Resized_image.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
