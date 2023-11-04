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
        self.preprocessors: List[PreProcessor] = preprocessors

    def load(self, imPaths):
        # labels = np.empty((len(imPath)), dtype=np.string_)
        # data = np.empty((len(imPath)))
        lables = []
        data = []

        for (i, imPath) in enumerate(imPaths):
            label = os.path.split(imPath)[-1].split('.')[0]
            image = cv2.imread(imPath)
            # print(image.shape)
            for p in self.preprocessors:
                image = p.preprocess(image)
            s = image.shape
            image = image.reshape(s[0]* s[1]*s[2])
            # print(image.shape)
            data.append(image)
            lables.append(label)
            print(f"[INFO] Images processed {i+1}/{len(imPaths)}", end = "\r")
        print(f"Images processed")
        lables = np.array(lables)
        data= np.array(data)
        print(f"{int(data.nbytes/(1024*1024))} Mb loaded")
        # print(lables.shape, data.shape)
        return lables,data



# myImg = '/home/rohith/Pictures/Screenshots/Screenshot from 2023-11-03 11-47-33.png'
# pp = PreProcessor(32, 32)

# lst = [
#     "/home/rohith/Pictures/Attorney-jusrtice-book.webp",
#     "/home/rohith/Pictures/advocate.jpg",
# ]

# loader = ImageLoader(preprocessors=[pp])

# labels, data = loader.load(lst)





