#!/usr/bin/env python3

import click
from elegooMarsUtility import emUtility
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
    emUtility.xyCompensate(input.name, compensation, firstcompensation, output.name,
        lambda x, y: print("Processing layer: {}/{}".format(x, y)), debugshow)

@click.command()
@click.argument("input")
def dump(input):
    photon = Photon(input)
    photon.export_images('tempdir')

cli.add_command(xyCompensate)
cli.add_command(dump)

if __name__ == '__main__':
    cli()