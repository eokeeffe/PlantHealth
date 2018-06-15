# This example uses a MovieWriter directly to grab individual frames and
# write them to a file. This avoids any event loop integration, but has
# the advantage of working with even the Agg backend. This is not recommended
# for use in an interactive setting.
# -*- noplot -*-

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
#import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cv2
from PIL import Image
from math import sqrt
import sys, os, time
from multiprocessing import Process

plt.ion()

video_length = 0.0
counter = 0.0
progress = 0.0

def progress_bar(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

def process_image(img):
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
    arr_ndvi=num/(denom+0.0000001)
    return arr_ndvi

def parallel_ndvi(cap,writer,fig,ndvi_plot):
    global video_length
    global counter
    global progress

    a = 0
    if(cap.isOpened()):
        ret,frame = cap.read()
        if ret:
            arr_ndvi = process_image(frame)
            ndvi_plot.set_data(arr_ndvi)
            writer.grab_frame()
            counter+=1
            progress_bar(counter,video_length)

def main(videoFile):
    global video_length
    cap = cv2.VideoCapture(videoFile)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    Writer=animation.writers['ffmpeg']
    writer = Writer(fps=30,
        metadata=dict(title='Movie Test',
        artist='EvanOKeeffe',
        comment='NDVI of LyonsEstate'),
        bitrate=1800)

    frame = None
    while not frame:
        ret,frame = cap.read()
        if ret: break

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)
    arr_ndvi = process_image(frame)
    ndvi_plot = ax.imshow(arr_ndvi,
        cmap=plt.cm.spectral,
        interpolation="nearest")
    fig.colorbar(ndvi_plot)

    with writer.saving(fig, "ndvi.mp4", 400):
        parallel_ndvi(cap,writer,fig,ndvi_plot)

    cap.release()
    print "Conversion complete"

if __name__=='__main__':
    main(sys.argv[1])
