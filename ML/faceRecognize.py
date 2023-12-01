from deepface import DeepFace

import cv2

res = DeepFace.verify(img1_path="./today2.jpg",img2_path="./today.jpg", enforce_detection=False)

print(res)