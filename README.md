# Introduction
This is a sample code to demostrate CUDA NPP APIs. The template is from [Pascale's course](https://github.com/PascaleCourseraCourses/CUDAatScaleForTheEnterpriseCourseProjectTemplate) and code structure from [CUDA Samples](https://github.com/nvidia/cuda-samples)

Go to https://docs.nvidia.com/cuda/npp/group__image__filtering__functions.html for more documentation on NPP APIs.

The code from NVIDIA has its own license, please check the specific license file or the header of each file.

## Project Description

We demostrated a convolution based filter that transform from one image to convoluted images. Here we have a demostration of original image and convoluted image.

Here you can see the different convolution kernels that act on the image:

| Convolution Kernel             |  Image |
:-------------------------:|:-------------------------:
Original |  <img src="./data/Lena.png"  width="40%" height="40%">
1,1,1,1,1<br>1,1,1,1,1<br>1,1,1,1,1<br>1,1,1,1,1<br>1,1,1,1,1 |  <img src="./data/Lena_convFilter_1%2C1.png"  width="40%" height="40%">
2,2,2,2,2<br>2,2,2,2,2<br>2,2,1,2,2<br>2,2,2,2,2<br>2,2,2,2,2 |  <img src="./data/Lena_convFilter_2%2C1.png"  width="40%" height="40%">
3,3,3,3,3<br>3,3,3,3,3<br>3,3,1,3,3<br>3,3,3,3,3<br>3,3,3,3,3 |  <img src="./data/Lena_convFilter_3%2C1.png"  width="40%" height="40%">
4,4,4,4,4<br>4,4,4,4,4<br>4,4,1,4,4<br>4,4,4,4,4<br>4,4,4,4,4 |  <img src="./data/Lena_convFilter_4%2C1.png"  width="40%" height="40%">

## How to compile & run
Before run the code and compile the code, please make sure FreeImage dependency has already installed.

```
./run.sh
```
Just execute the above, it will compile and run the program, even convert final result to PNG files!

The code is tested on [NVIDIA Jetson TX2 platform](https://developer.nvidia.com/embedded/jetson-tx2), which has 6 ARM cores as well as 256-core NVIDIA Pascal(TM) GPU.

## Code Organization

```bin/```
This folder should hold all binary/executable code that is built automatically or manually. Executable code should have use the .exe extension or programming language-specific extension.

Note that I included the binary of ARM, which is supposed to run on NVIDIA Jetson TX2 platform(GPU arch sm_62). If you have other platform, please re-build the program by running `run.sh`

```data/```
This folder contains sample input and sample output. In my experiments, `Lena.pgm` is the input image. But you can see the picture using `Lena.png`.

```lib/```
Contains libraries that copied from original template repo. It contains GL, UtilNPP, and various helper headers.

Notice that you might need FreeImage placed in the folder if you do not have FreeImage installed on the system.

```src/```
One CPP file that handles image input, invokes NPP's API to do convolution of images, compute the image, and write to image file.

```README.md```
This documentation.

```INSTALL```
The installation dependency library description of this repo.

```Makefile or CMAkeLists.txt or build.sh```
Makefile is used for making this project. You can build the binary simply by `make build`.

```run.sh```
This script is for easy hands-on. It also included a python invokation that convert images to PNG format.

```ConvertImageToPng.py```
Python script that convert image to PNG.