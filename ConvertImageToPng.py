#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Mar 04 2023
#
# Copyright (c) 2023 Daochen Shi
#

__author__ = "Daochen Shi"
__copyright__ = "Copyright (c) 2023 Daochen Shi"
__version__ = "0.1"

import os
import argparse
from PIL import Image

def convertImage2Png(imgPath, suffix):
    """Convert single image with specfic suffix, to a PNG file."""
    im = Image.open(imgPath)
    pngPath = imgPath[:-len(suffix)] + ".png"
    if os.path.exists(pngPath):
        print("Target exists, skip convert:", pngPath)
    else:
        print("Converted to ", pngPath)
        im.save(pngPath)

def checkFileFormatAndConvert(imgPath, suffix):
    if imgPath.endswith(suffix) and len(imgPath) > len(suffix):
        convertImage2Png(imgPath, suffix=suffix)
    

def findAndConvertImg2Png(folderpath):
    for dirpath, _, files in os.walk(folderpath):
        for file in files:
            checkFileFormatAndConvert(imgPath=os.path.join(dirpath,file), suffix='.pgm')
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert pgm images to png images')
    parser.add_argument('--folder', default='./data', nargs='?', type=str, help='The folder path to search for .pgm files')
    args = parser.parse_args()

    findAndConvertImg2Png(args.folder)
