import io
import json
import base64
import cv2
import PIL
from google.genai import types

def processFrame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(frame_rgb)  
    img.thumbnail([480, 640])

    image_io = io.BytesIO()
    img.save(image_io, format="jpeg")
    image_io.seek(0)

    mime_type = "image/jpeg"
    image_bytes = image_io.read()
    return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}


def generateResponse(client, prompt: str, img_data: dict):
    # To run this code you need to install the following dependencies:
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type=img_data['mime_type'],
                    data=base64.b64decode(
                        img_data['data']
                    ),
                ),
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

    buffer = ""
    for chunk in client.models.generate_content_stream(
        model='models/gemini-3-pro-preview',
        contents=contents,
    ):
        buffer+=chunk.text
        #print(chunk.text, end="")

    return parse_json(buffer)

def parse_json(json_output):
  # Parsing out the markdown fencing
  lines = json_output.splitlines()
  for i, line in enumerate(lines):
    if line == "```json":
      # Remove everything before "```json"
      json_output = "\n".join(lines[i + 1 :])
      # Remove everything after the closing "```"
      json_output = json_output.split("```")[0]
      break  # Exit the loop once "```json" is found
  return json.loads(json_output)