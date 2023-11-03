import cv2
import numpy as np
from imutils import paths
import os
from typing import List
# print(cv2.INTER_AREA)

class PreProcessor:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inter = cv2.INTER_AREA
    def preprocess(self, image):
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)


class ImageLoader:
    
    def __init__(self, preprocessors: List[PreProcessor] = []):
        self.preprocessors = []

    def load(self, imPaths):
        # labels = np.empty((len(imPath)), dtype=np.string_)
        # data = np.empty((len(imPath)))
        lables = []
        data = []

        for (i, imPath) in enumerate(imPaths):
            label = os.path.split(imPath)[-1].split('.')[1]
            image = cv2.imread(imPath)
            for p in self.preprocessors:
                image = p.preprocess(image)
            data.append(image)
            lables.append(label)
            print(f"\r[INFO] Images processed {i+1}/{len(imPaths)}")
        print(f"Images processed")
        return la



myImg = '/home/rohith/Pictures/Screenshots/Screenshot from 2023-11-03 11-47-33.png'





