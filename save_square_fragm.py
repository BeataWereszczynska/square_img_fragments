# -*- coding: utf-8 -*-
"""
Saves random unique square fragments of FDF image (located inside or outside defined bounding box) as jpg.

@author: Beata Wereszczyńska
"""

import itk
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import itertools
import random
import numpy as np
import cv2
import os
import shutil

def save_square_fragm(img_path, bb, vv, N, a, inner, out_folder):
    """
    Saves random unique square fragments of FDF image (located inside or outside defined bounding box) as jpg.
    Input: 
        image location: img_path [str],
        bounding box: bb [tuple, ((x1,y2),(x2,y1))],
        visual verification: vv [bool],
        number of square fragments: N [int],
        length of the side of the square fragments: a [int],
        position of the squares in relation to the bonding box: inner [bool],
        output folder: out_folder [str].
    """
    # FDF image import
    imageio = itk.FDFImageIO.New()
    img = itk.imread(img_path, imageio=imageio)
    img = np.array(img)
    del img_path
    
    # Image and bounding box visual veryfication
    if vv:
        plt.rcParams['figure.dpi'] = 200
        figure, image = plt.subplots()
        image.imshow(img, cmap=plt.get_cmap('gray'))
        w = bb[1][0] - bb[0][0]
        h = bb[1][1] - bb[0][1]
        bb_rect = Rectangle(bb[0], w, h, linewidth=0.5, edgecolor='cyan', facecolor='none')
        image.add_patch(bb_rect)
        plt.title("Image and bounding box - visual veryfication")
        plt.show()
    del vv
        
    # length of the side of the square fragments must be smaller than the bounding box 
    if min([bb[1][0] - bb[0][0], bb[0][1] - bb[1][1]]) >= a:
        
        if inner:            
            # N squares have to fit inside the bounding box:
            N_max = (bb[0][1] - bb[1][1] - a + 2) * (bb[1][0] - bb[0][0] - a + 2)
            if N > N_max:
                print(f"{N} unique squares of size {a} will not fit into the bounding box.")
            
            else:
                # list of allowed locations of upper left corners of the squares
                A = range(bb[0][0], bb[1][0] - a + 2)
                B = range(bb[1][1], bb[0][1] - a + 2)
                PickList = list(itertools.product(A, B))
                
                # input image and output folder preparation                
                img = img/(img.max()/255.0)                              # because FDFs are not scalled 0-255
                shutil.rmtree(out_folder, ignore_errors=True)            # removing residual output folder with content
                os.makedirs(out_folder)                                  # creating new output folder
                
                # positions of the squares and saving square fragments of the image
                i = 0
                squares = random.sample(PickList, N)
                for square in squares:
                    roi = img[square[1] : square[1] + a, square[0] : square[0] + a]
                    cv2.imwrite(f"{out_folder}/{i+1}.jpg", roi)            
                    i = i + 1
        
        else:
            # list of allowed locations of upper left corners of the squares for the image size and "a"
            A = range(0, np.shape(img)[0]- a + 1)
            B = range(0, np.shape(img)[1]- a + 1)
            C = list(itertools.product(A, B))
            # list of locations excluded by bounding box
            D = range(bb[0][0] - a + 1, bb[1][0] + 1)
            E = range(bb[1][1] - a + 1, bb[0][1] + 1)
            F = list(itertools.product(D, E))
            # resulting list of allowed locations of upper left corners of the squares
            # operation on sets, because depending on the position of the box, 
            # there may be elements in F that do not appear in C (excluded by "a")
            PickList = list(set(C) - set(F))
            
            # N squares have to fit inside the selected image region:            
            if N > len(PickList):
                print(f"{N} unique squares of size {a} will not fit into the selected image region.")
                
            else:                
                # input image and output folder preparation                
                img = img/(img.max()/255.0)                              # because FDFs are not scalled 0-255
                shutil.rmtree(out_folder, ignore_errors=True)            # removing residual output folder with content
                os.makedirs(out_folder)                                  # creating new output folder
                
                # positions of the squares and saving square fragments of the image
                i = 0
                squares = random.sample(PickList, N)
                for square in squares:
                    roi = img[square[1] : square[1] + a, square[0] : square[0] + a]
                    cv2.imwrite(f"{out_folder}/{i+1}.jpg", roi)            
                    i = i + 1
    else:
        print('"a" is too big for the bounding box.')


def main():
    img_path = "bumblebeeMRI/slice002.fdf"           # Path to the FDF image of choice: img_path [str]
    bb = ((440, 930), (825, 35))                     # Bounding box: bb [tuple, ((x1,y2),(x2,y1))]
    vv = 1                                           # Show the image with the bounding box for visual verification: vv [bool]
    N = 10                                           # Number of square fragments to create: N [int]
    a = 100                                          # Length of the side of the square fragments: a [int]
    inner = 1                                        # Position of the squares in relation to the bonding box: inner [bool]
    out_folder = "square_fragm"                      # Output folder: out_folder [str]

    save_square_fragm(img_path, bb, vv, N, a, inner, out_folder)


if __name__ == "__main__":
    main()
