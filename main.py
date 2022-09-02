import cv2
import numpy as np
import ults
path='img5.jpeg'
cap=cv2.VideoCapture(0)
address="http://10.39.84.1:8080/video"
cap.open(address)
webcam=False


cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale=3
wP=210*scale
hP=297*scale



while True:
    if webcam:success,img=cap.read()
    else: img=cv2.imread(path)
    imgContours, conts = ults.getContours(img,minArea=50000,filter=4)
    if len(conts)!=0:
        biggest = conts[0][2]
        #print(biggest)
        imgWarp=ults.wraping(img, biggest, wP , hP)

        imgContours2, conts2 = ults.getContours(imgWarp, minArea=2000,
                                                filter=4,cThr=[50,50],draw=False)
        if len(conts)!=0:
            for obj in conts2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
                npoints=ults.reorder(obj[2])
                nW=round((ults.findDis(npoints[0][0]//scale,npoints[1][0]//scale)/10),1)
                nH=round((ults.findDis(npoints[0][0]//scale,npoints[2][0]//scale)/10),1)
                cv2.arrowedLine(imgContours2, (npoints[0][0][0], npoints[0][0][1]),
                                (npoints[1][0][0], npoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (npoints[0][0][0], npoints[0][0][1]),
                                (npoints[2][0][0], npoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
        cv2.imshow('a4', imgContours2)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow('Original',img)
    cv2.waitKey(1)
##############################




































'''img = cv2.imread('smarties.png')
#output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x, y ,r) in detected_circles[0, :]:
    cv2.circle(img, (x, y), r, (0, 0, 0), 3)
    cv2.circle(img, (x, y), 2, (0, 255, 255), 3)


cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
