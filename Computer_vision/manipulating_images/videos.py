import cv2
import time

frames = 0
video = cv2.VideoCapture(0)
start = time.time()

while True:
    frames += 1

    check, frame = video.read()
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing Webcam", gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

end = time.time()
difference = int(end - start)
frames_per_second = frames // difference
print(start)
print(end)
print(difference)
print(frames)
print("{} frames per second".format(frames_per_second))
video.release()
cv2.destroyAllWindows()
