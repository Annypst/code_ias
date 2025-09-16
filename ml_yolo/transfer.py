from ultralytics import YOLO


model=YOLO('models/best0719.pt')
results=model.export(format='onnx')