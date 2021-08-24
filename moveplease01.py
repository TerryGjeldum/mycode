#!/usr/bin/env python3

"""A simple script to move two files into ceph_storage/
    Terry Gjeldum Research | Terry_Gjeldum.com"""

import shutil
import os

def main():

    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
