#!/usr/bin/env python3
# given a file, repeat the contents of the file
# n amount of times. Originally written for
# http://askubuntu.com/q/521465/295286
from __future__ import print_function
import sys,os

def error_out(string):
    sys.stderr.write(string+"\n")
    sys.exit(1)

def read_bytewise(fp):
    data = fp.read(1024)
    print(data.decode(),end="",flush=True)
    while data:
        data = fp.read(1024)
        print(data.decode(),end="",flush=True)
    #fp.seek(0,1)

def main():
    howmany = int(sys.argv[1]) + 1
    if not os.path.isfile(sys.argv[2]):
       error_out("Needs a valid file") 

    fp = open(sys.argv[2],'rb')
    for i in range(1,howmany):
        #print(i)
        fp.seek(0)
        read_bytewise(fp)
    fp.close()

if __name__ == '__main__': main()
