import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
#import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cv2
from PIL import Image
from math import sqrt
import sys, os

def savi(img,imageOutPath):
    '''
        SAVI Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    L = 0.5

    num=((arrR-arrB)*(1+L))
    denom=(arrR+arrB+L)
    arr_savi=num/denom

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    savi_plot = ax.imshow(arr_savi, cmap=plt.cm.spectral, interpolation="nearest")
    #rdvi_plot = ax.imshow(arr_rdvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(savi_plot)
    fig.savefig(imageOutPath)

def savi2(img,imageOutPath):
    '''
        SAVI Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    arr_savi2=arrR+0.5-np.sqrt(np.power((arrR+0.5),2)-2*(arrR-arrB))

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    savi2_plot = ax.imshow(arr_savi2, cmap=plt.cm.spectral, interpolation="nearest")
    #rdvi_plot = ax.imshow(arr_rdvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(savi2_plot)
    fig.savefig(imageOutPath)

def rdvi(img,imageOutPath):
    '''
        renormalized Difference Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    num=(arrR - arrB)
    denom=(np.sqrt(arrR+arrB))
    arr_rdvi=num/denom

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    rdvi_plot = ax.imshow(arr_rdvi, cmap=plt.cm.spectral, interpolation="nearest")
    #rdvi_plot = ax.imshow(arr_rdvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(rdvi_plot)
    fig.savefig(imageOutPath)

def msr(img,imageOutPath):
    '''
        MSR Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    num=(arrR - arrB)
    denom=(arrR + arrB)
    arr_ndvi=num/denom

    sr = (1+arr_ndvi)/(1-arr_ndvi)
    msr = (sr-1)/np.sqrt(sr+1)

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    msr_plot = ax.imshow(msr, cmap=plt.cm.spectral, interpolation="nearest")
    #ndvi_plot = ax.imshow(arr_ndvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(msr_plot)
    fig.savefig(imageOutPath)

def sr(img,imageOutPath):
    '''
        SR Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    arr_sr=(arrR/arrB)

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    sr_plot = ax.imshow(arr_sr, cmap=plt.cm.spectral, interpolation="nearest")
    #ndvi_plot = ax.imshow(arr_ndvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(sr_plot)
    fig.savefig(imageOutPath)

def endvi(img,imageOutPath):
    '''
        Enhanced Normalized Difference Vegtation Index
    '''
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')

    num = ((arrR+arrG)-(2*arrB))
    denom = ((arrR+arrG)+(2*arrB))
    arr_endvi=num/denom

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    endvi_plot = ax.imshow(arr_endvi, cmap=plt.cm.spectral, interpolation="nearest")
    #ndvi_plot = ax.imshow(arr_ndvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(endvi_plot)
    fig.savefig(imageOutPath)

def bvdrvi(img,imageOutPath):
    '''
        Normalized difference vegetation index
    '''
    #img1 = Image.open(imageInPath)

    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    arrR=np.asarray(red).astype('float64')
    arrG=np.asarray(green).astype('float64')
    arrB=np.asarray(blue).astype('float64')
    #red channel  = NIR
    #blue channel = visible
    num=0.1*(arrR - arrB)
    denom=0.1*(arrR + arrB)
    arr_bvdrvi=num/denom

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    bvdrvi_plot = ax.imshow(arr_bvdrvi, cmap=plt.cm.spectral, interpolation="nearest")
    #bvdrvi_plot = ax.imshow(arr_bvdrvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(bvdrvi_plot)
    fig.savefig(imageOutPath)

def ndvi(img,imageOutPath):
    '''
        Normalized difference vegetation index
    '''
    #img1 = Image.open(imageInPath)

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
    arr_ndvi=num/denom

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    #custom_cmap=make_cmap_gaussianHSV(bandwidth=0.01,num_segs=1024)
    ndvi_plot = ax.imshow(arr_ndvi, cmap=plt.cm.spectral, interpolation="nearest")
    #ndvi_plot = ax.imshow(arr_ndvi, cmap=custom_cmap, interpolation="nearest")

    fig.colorbar(ndvi_plot)
    #fig.savefig(imageOutPath)
    return fig

def nir(img,imageOutPath):
    '''
        Near InfraRed
    '''
    red=img[:,:,0]
    arrR=np.asarray(red).astype('float64')

    arr_nir=arrR

    fig=plt.figure()
    fig.set_frameon(False)
    ax=fig.add_subplot(111)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    nir_plot = ax.imshow(arr_nir, cmap=plt.cm.gist_gray, interpolation="nearest")

    #fig.colorbar(nir_plot)
    fig.savefig(imageOutPath)

def processVideo(videoFile):
    cap = cv2.VideoCapture(videoFile)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=30, metadata=dict(title='Movie Test', artist='EvanOKeeffe',comment='NDVI of invasive species lough corrib'), bitrate=1800)
    
    count=0
    while(cap.isOpened()):
        ret,frame = cap.read()
        fig = nir(frame,"ndvi"+str(count)+".jpg")
	    
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    print "Processing complete"

if __name__=='__main__':
    processVideo(sys.argv[1])
    #img = mpimg.imread("imagefile.jpg")
    #img = cv2.imread("imagefile.jpg")
    #ndvi(img,"ndvi.jpg")
    #nir(img,"nir.jpg")
