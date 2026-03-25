import cv2 as cv
from utilities import processFrame, generateResponse
from google.genai import Client
import os
from dotenv import load_dotenv

from prompt import PROMPT

load_dotenv()

client = Client(api_key=os.environ.get("GOOGLE_API_KEY"))
camera = cv.VideoCapture(0)
_, frame = camera.read()
h, w, _ = frame.shape
print(f"Captured Image Dimensions: {w}x{h}")

camera.release()

processedFrame = processFrame(frame)
result = generateResponse(
    client, 
    PROMPT,
    processedFrame
)
print(result)
norm_coords = result[0]['box_2d']
pixel_ymin = int((norm_coords[0] / 1000) * h)
pixel_xmin = int((norm_coords[1] / 1000) * w)
pixel_ymax = int((norm_coords[2] / 1000) * h)
pixel_xmax = int((norm_coords[3] / 1000) * w)
cv.rectangle(
    frame, 
    (pixel_xmin, pixel_ymin), 
    (pixel_xmax, pixel_ymax), 
    (0, 255, 0), 
    3
)

cv.imshow("The Great Filter - Detection", frame)
cv.waitKey(0)
cv.destroyAllWindows()