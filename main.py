import cv2

cv2.namedWindow('actual image')
cv2.namedWindow('hsv image')
cv2.namedWindow('thresholded result')
cv2.namedWindow('slider')

image_before = cv2.imread("/home/safiqq/opencv/image.jpg")
image_hsv = cv2.cvtColor(image_before, cv2.COLOR_BGR2HSV)

lh, ls, lv, uh, us, uv = 0, 0, 0, 180, 255, 255

def on_change_lh(val): global lh; lh = val
def on_change_ls(val): global ls; ls = val
def on_change_lv(val): global lv; lv = val

def on_change_uh(val): global uh; uh = val
def on_change_us(val): global us; us = val
def on_change_uv(val): global uv; uv = val
 
cv2.createTrackbar('lower h', 'slider', lh, 180, on_change_lh)
cv2.createTrackbar('lower s', 'slider', ls, 255, on_change_ls)
cv2.createTrackbar('lower v', 'slider', lv, 255, on_change_lv)

cv2.createTrackbar('upper h', 'slider', uh, 180, on_change_uh)
cv2.createTrackbar('upper s', 'slider', us, 255, on_change_us)
cv2.createTrackbar('upper v', 'slider', uv, 255, on_change_uv)
 
while True:
    cv2.imshow('actual image', image_before)
    cv2.imshow('hsv image', image_hsv)
    image_after = cv2.inRange(image_hsv, (lh, ls, lv), (uh, us, uv))
    cv2.imshow('thresholded result', image_after)

    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
       print(lh,ls,lv,uh,us,uv)
       break