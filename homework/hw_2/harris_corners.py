#!/usr/bin/env python2.7

import os, sys, argparse

# Import harris_utils
sys.path.insert(0, os.getcwd())
import harris_utils

def main():
    '''
    Implement the Harris corner detector. For a list of input parameters, just
    run

        ./harris_corner.py -h
    '''

    help_text = "Implementation of the Harris corder detector"
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument('-w', type=int, action='store', dest="window",
                      help="Size of window")
    parser.add_argument('-i', action='store', dest='img_path',
                      help="Provide the image file name")
    parser.add_argument('-o', action='store', dest='out_path',
                      help="Provide the output file name")
    parser.add_argument('-k', type=float, action='store', dest='trace_scale',
                      help= "Provide the trace scaling parameter k in the constraints det(M)-kTr(M)")
    parser.add_argument('-t', type=float, action='store', dest='threshold',
                      help="Provide the corner response threshold")
    args = parser.parse_args()

    corner_detector = harris_utils.harris_utils()

    corner_detector.window_size = args.window
    corner_detector.img_path = args.img_path
    corner_detector.out_path = args.out_path
    corner_detector.trace_scale = args.trace_scale
    corner_detector.threshold = args.threshold

    corner_detector.harris()

if __name__=="__main__":
    main()
