import cv2
from ultralytics import YOLO
from threading import Thread, Lock


lock = Lock()

def process_frame(frame, model, frame_number):
    with lock:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow('五边形识别', annotated_frame)
        print(f"处理帧: {frame_number}")

def read_frames(cap, frame_queue):
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_queue.append((frame, frame_number))
        frame_number += 1
    cap.release()

def main():

    model = YOLO('models/Pentagon_self.pt').cuda()


    video_path = 'vid_ex/1.mov'
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("无法打开视频文件")
        return


    original_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"原始帧率: {original_fps} FPS")


    desired_fps = 30
    cap.set(cv2.CAP_PROP_FPS, desired_fps)


    frame_queue = []


    read_thread = Thread(target=read_frames, args=(cap, frame_queue))
    read_thread.start()

    while True:
        if len(frame_queue) > 0:
            frame, frame_number = frame_queue.pop(0)

            frame = cv2.resize(frame, (640, 640))


            process_thread = Thread(target=process_frame, args=(frame, model, frame_number))
            process_thread.start()


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    read_thread.join()


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
