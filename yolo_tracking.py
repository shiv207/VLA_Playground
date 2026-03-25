from ultralytics import YOLO

# Load the YOLOv8 Nano model (efficient for M2 Apple Silicon)
# The model weights are already downloaded as 'yolov8n.pt'
model = YOLO('yolov8n.pt')

# Run tracking on the webcam (source=0)
# 'show=True' opens a window to display the video feed with bounding boxes
# 'tracker="bytetrack.yaml"' uses the ByteTrack algorithm (default)
print("Starting YOLOv8 tracking on webcam... Press 'q' to exit the window.")
results = model.track(source=0, show=True, tracker="bytetrack.yaml")
