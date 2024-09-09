# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

capture = cv2.VideoCapture("C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 10/cars.mp4")

car_cascade = cv2.CascadeClassifier("C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 10/cars.xml")

while True:
    ret, frames = capture.read()
    grayscale = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayscale, 1.1 , 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("OpenCV", frames)

    if cv2.waitKey(33) == 27:
        break
    