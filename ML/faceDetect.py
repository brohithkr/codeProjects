import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# model = DeepFace.analyze

baseFace = "./today2.jpg"
# baseFace = "./22BD1A051A.jpg"


while True:
    ret, frame = cap.read()
    face = face_classifier.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    # print(face)
    if len(face) != 0:
        for (x, y, w, h) in face:
            res = DeepFace.verify(frame[y:y+h,x:x+w], baseFace, enforce_detection=False)
            # res = {"verified":False}
            if cv2.waitKey(1) & 0xFF == ord("c"):
                cv2.imwrite("./today2.jpg", frame[y:y+h,x:x+w])
            # print(res)
            if res["verified"]:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
            # print(DeepFace.analyze(frame, enforce_detection=False))
            
    cv2.imshow("frame", frame)

    # if cv2.waitKey(1) & 0xFF == ord("c"):
    #     cv2.imwrite("./today.jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
