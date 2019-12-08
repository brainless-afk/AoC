from collections import Counter
from PIL import Image
import numpy as np

with open('input') as file:
    array = file.read().rstrip()
    array = list(map(int, array))

img_width, img_height = 25, 6
pixels = img_width * img_height

layers = []
layers = [array[i * pixels: (i + 1) * pixels] for i in range((len(array) + pixels - 1) // pixels)]

dict_count = [Counter(lay) for lay in layers]

min_list = [d.get(0) for d in dict_count]
min_index = min_list.index(min(min_list))
checksum = dict_count[min_index].get(1) * dict_count[min_index].get(2)

print("Part 1: Checksum: ", checksum)

decoded_image = np.zeros(pixels)
for pos in range(pixels):
    transparent = True
    depth = 0
    while transparent:
        if not layers[depth][pos] == 2:
            if layers[depth][pos] == 1:
                decoded_image[pos] = 255
            transparent = False
        else:
            depth += 1

image = Image.fromarray(decoded_image.reshape((img_height, img_width)))
image.show(title="Part 2 Code")
