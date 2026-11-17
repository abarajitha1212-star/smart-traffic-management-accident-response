# Architecture

CCTV/Sensors -> Detection Adapter -> Event Classification -> Priority Manager -> Signal State Manager -> Dashboard

Priority:
Safety event > Emergency vehicle > Traffic density > Fair rotation

The default package uses simulation events so it runs without cameras or hardware.

Future computer-vision integration can map OpenCV/YOLO detections into `DetectionEvent` objects. Accident detection should be validated across multiple frames/events rather than trusting one frame.
