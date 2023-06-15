import cv2 as cv

def blurFunction(img):
  return cv.GaussianBlur(img, (13, 13), 5, 0)

def brightnessFunction(img):
  return cv.convertScaleAbs(img, beta=60)