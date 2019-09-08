#!/usr/bin/env python3

import click
import numpy as np
import skimage
from skimage.morphology import square, disk
from matplotlib import pyplot as plt
from pyphotonfile import Photon
from pyphotonfile.photonfile import rle_to_imgarray, imgarr_to_rle
import sys
import shutil
import pkg_resources

if pkg_resources.get_distribution("pyphotonfile").version != "0.2.0":
    print("Only version 0.2.0 of pyphoton file is supported for now")
    sys.exit(1)

@click.group()
def cli():
    pass

@click.command()
@click.argument("input", type=click.File('rb'))
@click.option("--compensation", "-c", type=int, default=0)
@click.option('--firstCompensation', '-f', type=int, default=0)
@click.option('--output', '-o', type=click.File('wb'))
@click.option('--debugShow', type=bool, default=False)
def xyCompensate(input, compensation, firstcompensation, output, debugshow):
    infile = Photon(input.name)
    for i in range(len(infile.layers)):
        print("Processing layer: {}/{}".format(i + 1, len(infile.layers)))
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
    infile.write(output.name)

@click.command()
@click.argument("input")
def dump(input):
    photon = Photon(input)
    photon.export_images('tempdir')

cli.add_command(xyCompensate)
cli.add_command(dump)

if __name__ == '__main__':
    cli()