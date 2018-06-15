# This example uses a MovieWriter directly to grab individual frames and
# write them to a file. This avoids any event loop integration, but has
# the advantage of working with even the Agg backend. This is not recommended
# for use in an interactive setting.
# -*- noplot -*-

import matplotlib
#matplotlib.use('TkAgg')
from matplotlib import pyplot
#import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from tqdm import tqdm

import numpy as np
import matplotlib.animation as animation
import numpy as np
import cv2
from PIL import Image
from math import sqrt
import sys, os, time
from multiprocessing import Process

from subprocess import Popen, PIPE

#plt.ion()

def process_image(img,ptype="ndvi"):
    '''
        See https://maxmax.com/endvi.htm for explanation of the ndvi, endvi
        algorithms
    '''
    if ptype=="ndvi":
        red=img[:,:,0]
        green=img[:,:,1]
        blue=img[:,:,2]

        arrR=np.asarray(red).astype('float64')
        arrG=np.asarray(green).astype('float64')
        arrB=np.asarray(blue).astype('float64')
        #red channel  = NIR
        #blue channel = visible
        num=(arrR - arrB)
        denom=(arrR + arrB)
        arr_ndvi = num/(denom+0.0000001)
        return arr_ndvi
    if ptype=="endvi":
        red=img[:,:,0]
        green=img[:,:,1]
        blue=img[:,:,2]

        arrR=np.asarray(red).astype('float64')
        arrG=np.asarray(green).astype('float64')
        arrB=np.asarray(blue).astype('float64')
        #red channel  = NIR
        #blue channel = visible
        num=((arrR+arrG) - (2*arrB))
        denom=((arrR+arrG) + (2*arrB))
        arr_ndvi = num/(denom+0.0000001)
        return arr_ndvi

def parallel_ndvi():
    a = 0

def getNumberOfFrames(videoFile):
    print "Processing:",videoFile
    process = Popen(["ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 "+videoFile], shell=True, stdout=PIPE)
    process.wait()
    (output, err) = process.communicate()
    return int(output)

def main(videoFile,ptype="ndvi"):
    filename = "ndvi"
    if ptype=="endvi":
        filename = "endvi"
    
    cap = cv2.VideoCapture(videoFile)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    #if video_length < 0: video_length = getNumberOfFrames(videoFile)
    
    print "#Frames:",video_length
    Writer=animation.writers['ffmpeg']
    writer = Writer(fps=30,
		metadata=dict(title='Movie Test',
		artist='EvanOKeeffe',
		comment='NDVI of invasive species for Lough Corrib Test'),
		bitrate=1800)

    frame = None
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret:
            break

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    # TkAgg backend
    #manager = plt.get_current_fig_manager()
    #manager.full_screen_toggle()


    arr_ndvi = process_image(frame,ptype)
    ndvi_plot = ax.imshow(arr_ndvi,
		cmap=plt.cm.spectral,
		interpolation="nearest")
    fig.colorbar(ndvi_plot,orientation='horizontal')

    counter = 0.0
    progress = 0.0
    print video_length
    with writer.saving(fig, filename+".mp4", 100):
        with tqdm(total=video_length,unit="frames") as pbar:
            while(cap.isOpened()):
                ret,frame = cap.read()
                if ret:
                    arr_ndvi = process_image(frame,ptype)
                    ndvi_plot.set_data(arr_ndvi)
                    writer.grab_frame()
                    counter+=1
                    pbar.update(counter)
                    #progress_bar(counter,video_length)

    cap.release()
    print "Conversion complete"

if __name__=='__main__':
    main(sys.argv[1],sys.argv[2])
