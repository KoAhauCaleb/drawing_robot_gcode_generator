# Overview

This currently will take a cartoon image and convert it into g-code that will draw the image in it's own style when ran on a CNC controled drawing robot, or as I like to call it, a 2D printer. 

The main purpose of this project was to gain experience with controls engineering while doing something I would enjoy the final product of. I started this for the 2022 HackUSU competion, and enjoyed it enough that I will work on it in the future.

[Demo Video](https://youtu.be/UN0pHOz7dvg)

# Development Environment

The CNC contolor was using GRBL to proccess movement comands. GRBL has been designed for aurduino based control boards.

I wrote this in python, and implemented pillow for image prossesing. 

# Useful Websites

* [Grbl](https://github.com/grbl/grbl)
* [Pillow Docs](https://pillow.readthedocs.io/en/stable/)

# Future Work

* Fix algorithim to draw longer lines in the direction of the edge.
* Implement a TensorFlow model that will convert realistic images into cartoons.
* Design an algorithm that will create shading for more realistic drawings.