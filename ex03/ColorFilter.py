import numpy as np


class ColorFilter:
    def invert(self, array):
        rarray = 1 - array[...,0:3]
        return rarray

    def to_blue(self, array):
        blu_arr = np.zeros(array.shape)
        blu_arr[...,2:] = array[...,2:]
        return blu_arr

    def to_green(self, array):
        gre_arr = np.array(array)
        gre_arr[...,0] *=  0
        gre_arr[...,2] *=  0
        return gre_arr

    def to_red(self, array):
        red_arr = np.array(array)
        red_arr[...,1:3] -= array[...,1:3]
        return red_arr

    def celluloid(self, array):
        blu_arr = self.to_green(array)
        red_arr = self.to_red(array)
        gre_arr = self.to_green(array)
        blu_min = np.amin(blu_arr, (1,2))
        blu_max = np.amax(blu_arr, (1,2))
        blu_intervals = np.linspace(blu_min, blu_max, 4)
        red_min = np.amin(red_arr, (1,0))
        red_max = np.amax(red_arr, (1,0))
        red_intervals = np.linspace(red_min, red_max, 4)
        gre_min = np.amin(gre_arr, (1,2))
        gre_max = np.amax(gre_arr, (1,2))
        gre_intervals = np.linspace(gre_min, gre_max, 4)
        print(blu_min, blu_max, sep=' / ')
        print(blu_intervals)
        print(red_min, red_max, sep=' / ')
        print(red_intervals)
        print(gre_min, gre_max, sep=' / ')
        print(gre_intervals)

