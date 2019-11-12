import numpy as np
import skimage
from skimage.morphology import square, disk
from matplotlib import pyplot as plt
from pyphotonfile import Photon
from pyphotonfile.photonfile import rle_to_imgarray, imgarr_to_rle

def xyCompensate(infilename, compensation, firstcompensation, outfilename, report, debugshow=False):
    infile = Photon(infilename)
    for i in range(len(infile.layers)):
        report(i + 1, len(infile.layers))
        for sublayer in infile.layers[i].sublayers:
            layer = rle_to_imgarray(sublayer._data)
            if i < infile.bottom_layers:
                comp = firstcompensation
            else:
                comp = compensation
            if not comp or comp == 0:
                continue
            newLayer = skimage.morphology.binary_erosion(
                layer, square(comp))
            sublayer._data = imgarr_to_rle(skimage.img_as_ubyte(newLayer))
            if debugshow:
                f, a = plt.subplots(1, 2)
                a[0].imshow(layer, cmap=plt.cm.gray)
                a[1].imshow(newLayer, cmap=plt.cm.gray)
                plt.show()
    infile.write(outfilename)