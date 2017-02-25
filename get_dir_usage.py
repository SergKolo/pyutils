#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script to obtain total size of all
# items in a given directory
# Written for http://askubuntu.com/q/1224/295286

from __future__ import print_function
import os,sys

def get_filesizes_sum(directory):
    """ traverses given directory's tree
    and obtains sum of all files in the directory
    and its subdirectories"""
    size_total = 0
    treeroot = directory

    largest = (None,0)
    
    size_total += os.path.getsize(treeroot)

    for dir,subdirs,files in os.walk(treeroot):
         for f in files: 
             filepath = os.path.abspath(os.path.join(dir,f))
             if not os.path.islink(filepath):
                 filesize = os.path.getsize(filepath)
                 if filesize > largest[1]: largest = (filepath,filesize)
                 print(str(filesize) + "\t" + filepath) 
                 size_total += filesize
                 #size_total += os.path.getsize(filepath)

         for d in subdirs: 
             subdirpath = os.path.abspath(os.path.join(dir,d))
             if not os.path.islink(subdirpath):
                 subdirsize = os.path.getsize(subdirpath)
                 #if subdirsize > largest: largest = (subdirpath,subdirsize)
                 #print(str(subdirsize) + "\t" + subdirpath) 
                 size_total += subdirsize
                 #size_total += os.path.getsize(subdirpath)
    print('Largest:',largest)
    return size_total

def get_human_readable(size):
    """ converts size in bytes to
    human readable value in powers of 1024.
    Essentially, same as what df -h gives, or
    """
    prefix = ['B', 'KiB', 'MiB', 'GiB',
              'TiB', 'PiB', 'EiB',
              'ZiB', 'YiB'
              ]
    counter = 0
    while size / 1024 > 0.9:
        counter = counter + 1
        size = size / 1024

    return str(round(size, 2)) + "  " + prefix[counter]

def issue_error(string):
    sys.stderr.write("!!! " + string + "\n")
    sys.exit(1)
            
def main():
    if len(sys.argv) != 2:
        issue_error("Single argument required: path to dir")
    if not os.path.isdir(sys.argv[1]):
        issue_error("Invalid argument")
    dirpath = os.path.abspath(sys.argv[1])
    #print(get_human_readable(get_filesizes_sum(dirpath)))
    print(get_filesizes_sum(dirpath))

if __name__ =='__main__': main()
