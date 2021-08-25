#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil   # shell utilities will be used to move files
import os       # provies access to low level os operations (agnostic to flavor of OS)

"""called at runtime"""
os.chdir('/home/student/mycode/')   # move into this working directory
shutil.move('raynor.obj', 'ceph_storage/')  # try moving the file raynor.obj into ceph_storage/ dir
