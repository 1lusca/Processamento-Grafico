import cv2
import Overlay
  

#define the events for the
# mouse_click.
def mouse_click(event, x, y, 
                flags, param):
      
    # to check if left mouse 
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
          
        sticker = cv2.imread('assets/stickers/dino-rockeiro.png', cv2.IMREAD_UNCHANGED)

        out = Overlay.overlay(img, sticker, x, y) 

        cv2.imshow('sticker', out)



  
# read image
img = cv2.imread('baboon.png')


  
# show image
cv2.imshow('sticker', img)
   

          
        
cv2.setMouseCallback('sticker', mouse_click)
   
cv2.waitKey(0)
  
# close all the opened windows.
cv2.destroyAllWindows()