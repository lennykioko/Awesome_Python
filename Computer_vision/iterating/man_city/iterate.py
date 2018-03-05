import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 1)
    resized = cv2.resize(img, (400, 300))
    cv2.imshow("Resizing Images", resized)
    cv2.waitKey(5 * 1000)
    cv2.destroyAllWindows()
    # cv2.imwrite("resized_" + image, resized)
