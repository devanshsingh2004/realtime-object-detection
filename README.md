# Real-Time Object Detection using YOLOv8

This project is a real-time object detection system using a webcam and the YOLOv8s model from Ultralytics.

## 🔧 Features
- Detects 10+ common objects in real-time
- Uses pre-trained YOLOv8s model
- GPU acceleration for high FPS
- Live bounding boxes and confidence scores

## 🎥 Demo

https://drive.google.com/file/d/11SVBSiHdTFIUROs2HatISPbPj9Qe9i43/view?usp=sharing

## 📦 Requirements

Install using pip:

```bash
pip install -r requirements.txt
```
Make sure you have a compatible GPU and PyTorch installed with CUDA support.
## 🚀 Run
```bash
python realtime_detection.py
```
Press q to exit the live window.

## Results
Total Frames Processed: 752

Average FPS: 19.10

Unique Objects Detected (from model): 19

Actual Objects Presented (12):
book, bottle, cat, cell phone, cup, hair drier, keyboard, laptop, person, remote, spoon, toothbrush

## 🧪 Tested On
OS: Windows 11

GPU: NVIDIA GTX 1650 (Max-Q)

Python: 3.10

