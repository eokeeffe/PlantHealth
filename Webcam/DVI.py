import numpy as np #arrays and math
import cv2 #opencv library

#-------------------------------------------
#----------------DVI Function---------------
#-------------------------------------------

#DVI Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an RGB frame with equivalent DVI of the input frame
def DVICalc(original):
    "This function performs the DVI calculation and returns an RGB frame)"

    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape; 
    dviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    dvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing DVI value
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue

    #Now get the specific channels. Remember: (B , G , R)
    red = (original[:,:,2]).astype('float')
    blue = (original[:,:,0]).astype('float')

    #Perform DVI calculation
    dvi = (((red-blue)+255)/2).astype('uint8')  #the index

    redSat = (dvi-128)*2  #red channel
    bluSat = ((255-dvi)-128)*2 #blue channel
    redSat[dvi<128] = 0; #if the NDVI is negative, no red info
    bluSat[dvi>=128] = 0; #if the NDVI is positive, no blue info


    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    dviImage[:,:,2] = redSat

    #Blue Channel
    dviImage[:,:,0] = bluSat

    #Green Channel
    dviImage[:,:,1] = 255-(bluSat+redSat)

    return dviImage;
