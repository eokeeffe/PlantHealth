import numpy as np #arrays and math
import cv2 #opencv library

#-------------------------------------------
#----------------NDVI Function--------------
#-------------------------------------------

#NDVI Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an RGB frame with equivalent NDVI of the input frame
def NDVICalc(original):
    "This function performs the NDVI calculation and returns an RGB frame)"
    lowerLimit = 5 #this is to avoid divide by zero and other weird stuff when color is near black

    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape; 
    ndviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    ndvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing NDVI value
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue

    #Now get the specific channels. Remember: (B , G , R)
    red = (original[:,:,2]).astype('float')
    blue = (original[:,:,0]).astype('float')

    #Perform NDVI calculation
    summ = red+blue
    summ[summ<lowerLimit] = lowerLimit #do some saturation to prevent low intensity noise

    ndvi = (((red-blue)/(summ)+1)*127).astype('uint8')  #the index

    redSat = (ndvi-128)*2  #red channel
    bluSat = ((255-ndvi)-128)*2 #blue channel
    redSat[ndvi<128] = 0; #if the NDVI is negative, no red info
    bluSat[ndvi>=128] = 0; #if the NDVI is positive, no blue info


    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    ndviImage[:,:,2] = redSat

    #Blue Channel
    ndviImage[:,:,0] = bluSat

    #Green Channel
    ndviImage[:,:,1] = 255-(bluSat+redSat)

    return ndviImage;
