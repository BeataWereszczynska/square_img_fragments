# square_img_fragments
The save_square_fragm function saves random unique square fragments of an image (located inside or outside defined bounding box) as jpg. It can be useful e.g. in image recognition.

This little project is inspired by a recruitment task of a company that wished to remain anonymous. The task was to:

1. write a code that saves a specified number of random unique square fragments of a given image.
2. The fragments were to be located inside or outside defined bounding box (depending on a value of parameter assigned).
3. The fragments had to be smaller than bounding box to be able to fit in it.
4. The fragments were to be saved as jpg files in newly created output folder.
5. Before saving, the existing output folder was to be deleted with its content and created again.

A starting code provided by the company (requested not to be published here) was providing the input for the function to be created, containing:

1. name of the output folder, as a string,
2. value of parameter deciding if the fragments are to be located inside or outside the bounding box, as a bool,
3. custom definition of a bounding box with negative height, as a tuple (dealt by me as ((x1,y2),(x2,y1))),
4. number of square fragments to be saved, as an int,
5. length of the side of the square fragments, as an int,
6. the image to work on, as an JpegImageFile, Mode:RGB.

Here I present modified version of my solution adapted to process MRI (Magnetic Resonance Imaging) images in FDF format (native for Agilent MRI scanners). The current version:

1. takes as an input the FDF image path instead of preloaded jpg image,
2. can be easily modified to work on any image format,
3. allows for optional visual verification of the image with overlaid bounding box.



### The repository contains:

1. save_square_fragm function code, as .py,
2. save_square_fragm function code with description and results presentation, as jupyter notebook,
3. sample data in bumblebeeMRI folder (MRI images of a bumblebee fixed in glutaraldehyde solution. The imaging was performed on a 9.4 T MRI scanner),
4. sample output in square_fragm folder.
    
