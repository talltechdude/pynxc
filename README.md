pynxc
=====

*A Python to NXC Converter for programming LEGO MINDSTORMS Robots*

**pynxc** on GitHub is a continuation of a now stale project to convert Python
programs to NXC so that you can use Python to program your NXT robots.

You can find the official site of the old project here:
https://code.google.com/p/pynxc/

How to use
----------
1. Download and Install the [LEGO NXT Fantom Driver](https://www.lego.com/r/www/r/MINDSTORMS/-/media/franchises/mindstorms%202014/downloads/firmware%20and%20software/nxt%20software/nxt%20fantom%20drivers%20v120.zip) from the [LEGO Website](https://www.lego.com/en-us/mindstorms/downloads)
1. Download a zip or clone this repository to your local computer
1. Run `python setup.py install` from the main directory
1. Connect your NXT brick via USB
1. Create your Python script and use `pynxc -d myscript.py` to compile and upload it to the NXT
* There are some samples scripts in the `samples` directory that you can try or learn new functions from

How is this different
---------------------

This version is trying to provide an API with which one (in these case
especially kids) can program his or her NXT robot easily. The aim of this
project is to make this API as *Pythonic* as possible, so that if programming
robots with Python is someone's first encounter with Python they can then jump
right into the Python world.

[![Build Status](https://travis-ci.org/xlcteam/pynxc.png?branch=master)](https://travis-ci.org/xlcteam/pynxc)
