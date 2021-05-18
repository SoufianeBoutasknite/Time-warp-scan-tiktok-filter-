import cv2
import numpy as np


list_img = []
imgW, imgH = 600, 500
cap = cv2.VideoCapture(0)
y = 1
while y < imgH:
    _, img = cap.read()
    img = cv2.resize(img, (imgW, imgH))
    list_img.append(img[y-1])
    img[:y, :] = np.array(list_img)
    cv2.line(img, (0, y), (imgW, y), (0, 255, 0), 1)
    y += 1
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imshow('img', img)
cv2.waitKey(0)
