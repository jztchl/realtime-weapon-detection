from ultralytics import YOLO
import datetime
 
# Load the model.
model = YOLO('yolov8m.pt')
 
# Training.
results = model.train(
   data='dataset\data.yaml',
   imgsz=640,
   epochs=900,
   batch=4,
   name="yolov8m "+str(datetime.datetime.now()).replace(":","-"))