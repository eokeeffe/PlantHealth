import numpy as np #arrays and math
import cv2 #opencv library
from DVI import *
from NDVI import *
import sys
#-------------------------------------------
#----------------Main Function--------------
#-------------------------------------------

cv2.namedWindow("preview NDVI")
vc = None
if len(sys.argv) < 1:
    vc = cv2.VideoCapture(0)
else:
    vc = cv2.VideoCapture(int(sys.argv[1]))

height = 0
width = 0

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

# Define the codec and create VideoWriter object
#fourcc = cv2.FOURCC(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
height = int(height)
width = int(width)
#print fourcc,fps,height,width

ndvi = cv2.VideoWriter('ndvi.avi',fourcc, fps, (height,width))
dvi = cv2.VideoWriter('dvi.avi',fourcc, fps, (height,width))
normal = cv2.VideoWriter('normal.avi',fourcc, fps, (height,width))


while rval:
    ndviImage = NDVICalc(frame)
    dviImage = DVICalc(frame)

    cv2.putText(frame, "Raw Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)
    cv2.putText(ndviImage, "NDVI Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)
    cv2.putText(dviImage, "DVI Image", (x,y), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)

    ndvi.write(ndviImage)
    dvi.write(dviImage)
    normal.write(frame)

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
ndvi.release()
dvi.release()
normal.release()
cv2.destroyAllWindows()
