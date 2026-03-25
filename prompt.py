PROMPT = '''
Return bounding boxes as a JSON array with labels. 
Never return masks or code fencing. 
Locate the blue cube.

The format must be exactly:
[{"box_2d": [ymin, xmin, ymax, xmax], "label": "blue box"}]

CRITICAL INSTRUCTIONS:
1. Use normalized coordinates from 0 to 1000. 
2. [0, 0] is the top-left, and [1000, 1000] is the bottom-right.
3. The values in box_2d must be integers.
4. Return ONLY the JSON array, no preamble.
'''