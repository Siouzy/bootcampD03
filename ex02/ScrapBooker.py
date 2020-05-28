import numpy as np


class ScrapBooker:
    def crop(self, array, dimensions, position):
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            print('ERROR: dimensions are larger than the current image size')
            return
        new_array = []
        x = position[0]
        y = position[1]
        width = dimensions[0]
        heigth = dimensions[1]
        array = array[x:x + width]
        for vec in array:
            new_vec = vec[y:y + heigth]
            new_array.append(new_vec)
        return np.asarray(new_array)

    def thin(self, array, n, axis):
        return np.delete(array, n, axis)

    def juxtapose(self, array, n, axis):
        array_tpl = []
        for i in range(n):
            array_tpl.append(array)
        print(array_tpl)
        return np.concatenate(tuple(array_tpl), axis)

    def mosaic(self, array, dimensions):
        return self.juxtapose(
            self.juxtapose(
                array, dimensions[1], 1
                ), dimensions[0], 0
                )
