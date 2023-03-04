# Introduction
This is a sample code to demostrate CUDA NPP APIs. The template is from [Pascale's course](https://github.com/PascaleCourseraCourses/CUDAatScaleForTheEnterpriseCourseProjectTemplate) and code structure from [CUDA Samples](https://github.com/nvidia/cuda-samples)

Go to https://docs.nvidia.com/cuda/npp/group__image__filtering__functions.html for more documentation on NPP APIs.

## Project Description

We demostrated a convolution based filter that transform from one image to convoluted images. Here we have a demostration of original image and convoluted image.

## Code Organization

```bin/```
This folder should hold all binary/executable code that is built automatically or manually. Executable code should have use the .exe extension or programming language-specific extension.

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
An optional script used to run your executable code, either with or without command-line arguments.