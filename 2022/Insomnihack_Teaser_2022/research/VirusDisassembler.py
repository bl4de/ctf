import numpy as np
from PIL import Image
import sys
# Very important

SECRET=133

def Dissasemble(img_path):

    img = Image.open(img_path, 'r')
    data = np.array(list(img.getdata()))
    data = data[::SECRET,:]
    tot_pixels = data.shape[0]

    tmp_bits = ""
    for p in range(tot_pixels):
        tmp_bits += (bin(data[p][2])[-1])
    tmp_bits = [tmp_bits[i:i+8] for i in range(0, len(tmp_bits), 8)]

    message = ""
    for i in range(len(tmp_bits)):
        newchar = chr(int(tmp_bits[i], 2))
        message += newchar
    return message


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Example: python3 VirusDissasembler.py <image_path>")
    else:
        print(Dissasemble(sys.argv[1]))
