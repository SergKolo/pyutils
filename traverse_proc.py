#!/usr/bin/env python
# Process listing program ,similar to ps
# Traverses proc filesystem
from __future__ import print_function
import os,sys,re

def main():
    top_dir="/proc"
    proc_dirs = [ os.path.join(top_dir,dirent) 
                  for dirent in os.listdir(top_dir) 
                  if dirent.isdigit()]
    for dirent in proc_dirs:
        with open(os.path.join(dirent,"stat")) as fd:
             words = fd.readline().split()
             print(words[0],end=" ")
             binary = str()
             for word in words[1:]:
                 binary = binary + " " + word
                 if ')' in word: break
             print(re.sub(r'[()]','',binary),end=" ")

        with open(os.path.join(dirent,"cmdline")) as fd2:
             cmdline=fd2.read()
             print(cmdline.replace('\x00',' '))

if __name__ == '__main__' : main()
