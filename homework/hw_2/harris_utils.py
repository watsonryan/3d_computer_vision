#!/usr/bin/env python2.7

import numpy as np
from PIL import Image

class harris_utils():
    '''
    This is a simple class to implement the harris corner detector
    '''

    def __init__(self):
        '''
        Init variables
        '''

        self.window_size = 5
        self.trace_scale = 4e-2
        self.threshold = 1e-4
        self.img_width = 100
        self.img_height = 100
        self.sigma = 1
        self.img_path = ''
        self.corners_arr = []
        self.response_arr = []

    def gauss_ker(self):
        '''
        creates gaussian kernel
        '''

        ax = np.arange(-self.window_size // 2 + 1., self.window_size // 2 + 1.)
        xx, yy = np.meshgrid(ax, ax)
        self.kernel = np.array(np.exp(-(xx**2 + yy**2) / (2. * self.sigma**2)))

    def img_grad(self):
        '''
        find the gradient of the gray scale image
        '''

        self.dx = np.zeros((self.img_height, self.img_height))
        self.dy = np.zeros((self.img_height, self.img_width))

        for x in range(1, self.img_height - 1):
            for y in range(1, self.img_width - 1):
              self.dx[x,y] = float(int(self.gray_scale[x-1,y]) - int(self.gray_scale[x+1,y])) / 255
              self.dy[x,y] = float(int(self.gray_scale[x,y-1]) - int(self.gray_scale[x,y+1])) / 255

    def getStructureTensor(self, x, y):
        mA = 0
        mB = 0
        mC = 0
        mD = 0

        for i in range(0, self.window_size):
            for j in range(0, self.window_size):
                dxi = self.dx[x + i - self.window_size / 2, y + j - self.window_size / 2]
                dyi = self.dy[x + i - self.window_size / 2, y + j - self.window_size / 2]
                mA += self.kernel[i][j] * dxi * dxi
                mB += self.kernel[i][j] * dxi * dyi
                mC += self.kernel[i][j] * dxi * dyi
                mD += self.kernel[i][j] * dyi * dyi
        return [[mA, mB], [mC, mD]]

    def corner_response(self, x, y):
        '''
        Calculate the response of image segment where, R = Det(M) - k(Tr(M)*Tr(M))
        '''

        [[a, b], [c, d]] = self.getStructureTensor(x, y)
        det = a * d - b * c
        trace = a + d
        response = det - ( self.trace_scale * (trace ** 2));
        return response

    def find_corners(self):
        '''
        Harris corner detector
        '''

        self.window_size = int( self.window_size )
        for x in range(self.window_size/2, self.img_height - self.window_size/2):
            for y in range(self.window_size/2, self.img_width - self.window_size/2):
                if (self.corner_response(x,y) > self.threshold):
                    self.corners_arr.append((x, y))
                    self.response_arr.append( self.corner_response(x,y) )

    def display_corners(self):
        '''
        Display the corners found by the Harris detector on a new image
        '''

        for (h,w) in self.corners_arr:
            self.img_arr[h,w] = 127

        # Save an image with the corner locations
        Image.fromarray(self.img_arr).save(self.out_path)

    def write_corners(self):
        '''
        This is a helper method to print the top corners based on the response value
        '''

        out_arr = np.column_stack((np.asarray(self.corners_arr), np.asarray(self.response_arr)))
        sorted_arr = out_arr[np.argsort(-out_arr[:, 2])]
        np.savetxt('top_corners.txt', sorted_arr[0:100,:], delimiter=' ', fmt='%i %i %.3e')


    def harris(self):
        '''
        This is the main method.

        It will import the specified image, run the harris corner detector, saves a new image with the corners marked.
        '''

        try:
            self.image = Image.open(self.img_path)
        except:
            print '\n\n Oops! You need to provide an input image.  Try again... \n\n'
            exit()
        self.img_width, self.img_height = self.image.size
        self.img_arr = np.array(self.image)
        self.gray_scale = np.array(self.image.convert('L'))

        # Generate Gaussian kernel
        self.gauss_ker()
        # Take the grad. of the image
        self.img_grad()
        # Find corners using Harris detector
        self.find_corners()
        # Display corners
        self.display_corners()
        # Write most likely corners to text file
        self.write_corners()
