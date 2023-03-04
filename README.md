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

## How to run
Before run the code and compile the code, please make sure FreeImage dependency has already installed.

Just execute `run.sh`, it will compile and run the program, even convert final result to PNG files!

## Code Organization

```bin/```
This folder should hold all binary/executable code that is built automatically or manually. Executable code should have use the .exe extension or programming language-specific extension.
Note that I included the binary of ARM, which is supposed to run on NVIDIA Jetson TX2 platform. If you have other platform, please re-build the program by running `run.sh`

```data/```
This folder should hold all example data in any format. If the original data is rather large or can be brought in via scripts, this can be left blank in the respository, so that it doesn't require major downloads when all that is desired is the code/structure.

```lib/```
Any libraries that are not installed via the Operating System-specific package manager should be placed here, so that it is easier for inclusion/linking.
Note that in order to reduce the code size, I didn't include the FreeImage library here. You can get the library through the Internet.

```src/```
The source code should be placed here in a hierarchical fashion, as appropriate.

```README.md```
This file should hold the description of the project so that anyone cloning or deciding if they want to clone this repository can understand its purpose to help with their decision.

```INSTALL```
This file should hold the human-readable set of instructions for installing the code so that it can be executed. If possible it should be organized around different operating systems, so that it can be done by as many people as possible with different constraints.

```Makefile or CMAkeLists.txt or build.sh```
There should be some rudimentary scripts for building your project's code in an automatic fashion.

```run.sh```
This script is for easy hands-on. It also included a python invokation that convert images to PNG format.

```ConvertImageToPng.py```
Python script that convert image to PNG.