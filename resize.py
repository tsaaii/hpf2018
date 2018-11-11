import cv2
import os

folder = "./coloreds"

def resize(img_path):
    return cv2.resize(cv2.imread(img_path), (256, 256), interpolation = cv2.INTER_AREA)

for directory in os.listdir(folder):
    for f in os.listdir(folder+"/"+directory):
        img_path = folder+"/"+directory+"/"+f
        cv2.imwrite(img_path, resize(img_path))