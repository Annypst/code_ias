import cv2
from ultralytics import YOLO


model = YOLO('models/best723.pt')

video_path = 'Player Recorded Video/2.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("无法打开视频文件")
    exit()

while True:

    ret, frame = cap.read()
    if not ret:
        print("无法接收帧（视频结束？）")
        break


    results = model(frame)


    annotated_frame = results[0].plot()


    cv2.imshow('五边形识别', annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
