<p align="center">
  <img src="weapon_detection.png" alt="weapon detection Logo" width="200">
</p>

```markdown
# Real-Time Weapon Detection

This project aims to detect weapons in real-time through cameras and notify authorities instantly. It's a mini project demonstrating the use of deep learning for security purposes.

## Features

- **Real-time Detection**: Utilizes live camera feeds to detect weapons.
- **Instant Notifications**: Sends immediate alerts to authorities when a weapon is detected.
- **GUI Application**: User-friendly graphical interface for monitoring.
- **Customizable Alerts**: Alarm sound (`alarm.mp3`) can be customized.
- **Web Server**: Includes a web server component for managing and viewing detections.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jztchl/realtime-weapon-detection.git
   cd realtime-weapon-detection
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, install the required Python packages:
   ```bash
   pip install -r needs.txt
   ```

3. **Download YOLOv8 Model**
   The project uses a pre-trained YOLOv8 model (`yolov8m.pt`) for detection.

## Usage

1. **Running the GUI Application**
   ```bash
   python guiapp.py
   ```

2. **Running the Web Server**
   Navigate to the `weapon_detection_server` directory and start the server:
   ```bash
   cd weapon_detection_server
   python manage.py runserver
   ```

3. **Training the Model**
   To train the model on a new dataset, use:
   ```bash
   python train.py
   ```

4. **Testing the Model**
   To test the model, run:
   ```bash
   python test.py
   ```

5. **Downloading Images**
   To download images for training or testing, use:
   ```bash
   python download_images.py
   ```

## Project Structure

- **alarm.mp3**: The sound file played when a weapon is detected.
- **best.pt**: The best performing model checkpoint.
- **download_images.py**: Script to download images for training/testing.
- **guiapp.py**: Main script to run the graphical user interface application.
- **needs.txt**: File listing required Python packages.
- **oog.py**: Additional script for miscellaneous tasks.
- **test.py**: Script to test the trained model.
- **train.py**: Script to train the model.
- **yolov8m.pt**: Pre-trained YOLOv8 model.
- **weapon_detection_server/**: Directory containing the web server application.
  - **app1/**: Django app handling weapon detection.
  - **media/**: Directory for media files.
  - **static/**: Directory for static files.
  - **template/**: Directory for HTML templates.
  - **db.sqlite3**: SQLite database file.
  - **manage.py**: Django management script.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License.
```
