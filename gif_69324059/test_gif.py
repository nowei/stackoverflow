import numpy as np
import matplotlib.pyplot as plt
import imageio
# Create PNGs
y = np.random.randint(30, 40, size=(40))
for i in range(4):
    plt.plot(y[:i - 3])
    plt.ylim(20,50)
    plt.savefig('1.png')
    plt.close()
    
# Build GIF
png_list = ['1.png', '2.png', '3.png', '4.png'] # Order of images
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in png_list:
        image = imageio.imread(filename)
        writer.append_data(image)