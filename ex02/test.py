import numpy as np 
from ScrapBooker import ScrapBooker


notrand_array = np.array(range(25)).reshape((5,5))

print(notrand_array)
print(notrand_array.shape)
#print(rand_array)
sb = ScrapBooker()
new_array = sb.crop(notrand_array, (3,3), (1,2))
print(new_array)
print(new_array.shape)
print(sb.juxtapose(notrand_array, 2, 1))
print(sb.mosaic(notrand_array, (2, 3)))