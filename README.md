# square_img_fragments
Saving random unique square fragments of an image (located inside or outside defined bounding box) as jpg.

## The task
This little project is inspired by a recruitment task of a company that wished to remain anonymous. The task was to:

1. write a code that saves a specified number of random unique square fragments of a given image.
2. The fragments were to be located inside or outside defined bounding box (depending on a value of a parameter assigned).
3. The fragments had to be smaller than the bounding box to be able to fit in it.
4. The fragments were to be saved as jpg files in newly created output folder.
5. Before saving, the existing output folder was to be deleted with its content and created again.

A starting code provided by the company (requested not to be published here) was providing the input for the function to be created, containing:

1. name of the output folder, as a string,
2. value of the parameter deciding if the fragments are to be located inside or outside the bounding box, as a boolean value,
3. custom definition of a bounding box with negative height, as a tuple (dealt by me as ((x1,y2),(x2,y1))),
4. number of square fragments to be saved, as an integer,
5. length of the side of the square fragments, as an integer,
6. the image to work on, as an JpegImageFile, Mode:RGB.

Here I present modified version of my solution, adapted to process MRI (Magnetic Resonance Imaging) images in FDF format (native for Agilent MRI scanners). The current version:

1. takes as an input the FDF image path instead of preloaded jpg image,
2. can be easily modified to work on any image format,
3. allows for optional visual verification of the image with overlaid bounding box.

## The repository contains:

1. Python script save_square_fragm.py with the code,
2. The code with description and sample results, as jupyter notebook file notebook_save_square_fragm.ipynb,
3. sample data in bumblebeeMRI folder - FDF images (MRI images of a bumblebee fixed in glutaraldehyde solution. The imaging was performed on a 9.4 T Agilent MRI scanner),
4. sample output in square_fragm folder.
    
## License

The software is licensed under the MIT license. The non-software content of this project is licensed under the Creative Commons Attribution 4.0 International license. See the LICENSE file for license rights and limitations.
