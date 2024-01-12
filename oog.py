import tkinter as tk
from tkinter import PhotoImage, Entry, Button, Label
import cv2
import math
import requests
from ultralytics import YOLO
from PIL import Image, ImageTk
import io
import datetime;

# Initialize YOLO model
model = YOLO('best.pt')

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Define class names
classNames = ['Grenade', 'Knife', 'Pistol', 'Rifle', 'Shotgun']

# Initialize detection status
is_detecting = False

# API Endpoint
api_url = 'http://127.0.0.1:8000/upload/'

# Create a function to start or stop detection
def toggle_detection():
    global is_detecting
    is_detecting = not is_detecting
    toggle_button.config(text="Stop Detection" if is_detecting else "Start Detection")
    toggle_button.config(bg="red" if is_detecting else "green")

# Create the main detection function
def detect_objects():
    if is_detecting:
        success, img = cap.read()
        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                confidence = math.ceil((box.conf[0] * 100)) / 100
                if confidence >= 0.75:
                    print("Confidence --->", confidence)
                    address = address_entry.get()+" "+ str(datetime.datetime.now()) # Get text input from the Entry widget
                    send_data_to_api(img, address)  # Send image and address to the API

                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls] + str(confidence), org, font, fontScale, color, thickness)

        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        photo = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=photo)
        label.imgtk = imgtk
        label.config(image=imgtk)
        label.after(10, detect_objects)
    else:
        label.after(10, detect_objects)

# Create a function to send data (image and address) to the API
def send_data_to_api(image, address):
    try:
        _, img_encoded = cv2.imencode('.jpg', image)
        response = requests.post(api_url, files={'image': ('image.jpg', img_encoded.tobytes())}, data={'address': address})
        if response.status_code == 201:
            print("Data sent to the API successfully.")
        else:
            print("Failed to send data to the API.")
    except Exception as e:
        print("Error:", str(e))

# Create the main application window
app = tk.Tk()
app.title("Weapon Detection")
app.geometry("800x600")  # Set initial window size

# Create a label widget for displaying the video stream
label = tk.Label(app)
label.pack(fill=tk.BOTH, expand=True)  # Expand label to fill available space

# Create Start/Stop button with styling
toggle_button = tk.Button(app, text="Start Detection", command=toggle_detection, bg="green")
toggle_button.pack(pady=10)  # Add padding around the button

# Create an Entry widget for text input (address)
address_label = Label(app, text="Enter Address:")
address_label.pack()
address_entry = Entry(app)
address_entry.pack()
address_entry.insert(0, "ITEC,Palayad,Dharmadam,Kannur")  # Set a default address

# Start the detection loop
label.after(10, detect_objects)

# Start the application
app.mainloop()
