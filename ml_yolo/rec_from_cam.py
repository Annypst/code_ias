import cv2
from ultralytics import YOLO
from datasets import load_dataset
ds = load_dataset("0-ma/geometric-shapes")


model = YOLO('models/Pentagon_self.pt')


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取帧
    ret, frame = cap.read()
    if not ret:
        print("无法接收帧（流结束？）")
        break


    results = model(frame)


    annotated_frame = results[0].plot()


    cv2.imshow('YOLOv11 Detection', annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


