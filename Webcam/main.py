import numpy as np #arrays and math
import cv2 #opencv library
from NDVI import NDVICalc
from DVI import DVICalc
#-------------------------------------------
#----------------Main Function--------------
#-------------------------------------------

cv2.namedWindow("preview NDVI")
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    height = vc.get(3) #get height
    width = vc.get(4) #get width
    #Text Related
    x = int(width/2)
    y = int(2*height/3) 
    text_color = (255,255,255) #color as (B,G,R)
    font = cv2.FONT_HERSHEY_PLAIN
    thickness = 2
    font_size = 2.0
else:
    rval = False

while rval:
    ndviImage = NDVICalc(frame)
    dviImage = DVICalc(frame)

    cv2.putText(frame, "Raw Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)
    cv2.putText(ndviImage, "NDVI Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)
    cv2.putText(dviImage, "DVI Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)

    newFrame = np.concatenate((ndviImage,dviImage,frame),axis=1)
    cv2.imshow("preview NDVI", newFrame)

    rval, frame = vc.read()

    key = cv2.waitKey(1)&0xFF #get a key press
    if key == ord('q'): #q for quitting
        break
    elif key == ord('p'): #p for printscreen
        curtime = datetime.datetime.now()
        formattedTime = curtime.strftime("%Y%m%d-%H-%M-%S.jpg")
        print 'filename:%s'%formattedTime
        cv2.imwrite(formattedTime,newFrame)
        print "Screenshot taken!"

# When everything done, release the capture
vc.release()
cv2.destroyAllWindows()
