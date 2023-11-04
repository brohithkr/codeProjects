import cv2

image = cv2.imread("/home/rohith/Downloads/dogs-vs-cats/train/cat.0.jpg")

print(image.shape)

im2 = cv2.resize(image, (400,400), interpolation=cv2.INTER_AREA)

print(im2.shape)
