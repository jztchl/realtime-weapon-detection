from ultralytics import YOLO
import cv2
import math 
import pygame

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load a COCO-pretrained YOLOv8n model
model = YOLO('best.pt')
pygame.mixer.init()

# Display model information (optional)
#model.info()

# Train the model on the COCO8 example dataset for 100 epochs
#results = model.train(data='coco8.yaml', epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
#results = model('a.jpg')
classNames = ['Grenade', 'Knife', 'Pistol', 'Rifle', 'Shotgun']
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            if confidence>=0.65:
             play_audio("alarm.mp3")
             print("Confidence --->",confidence)

            # class name
             cls = int(box.cls[0])
             print("Class name -->", classNames[cls])

            # object details
             org = [x1, y1]
             font = cv2.FONT_HERSHEY_SIMPLEX
             fontScale = 1
             color = (255, 0, 0)
             thickness = 2

             cv2.putText(img, classNames[cls]+str(confidence), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()