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

## 📊 Performance Summary
Total Frames Processed: 752

Average FPS: 19.10

Unique Objects Detected (from model): 19

Actual Objects Presented (11):
book, bottle, cell phone, cup, hair drier, keyboard, laptop, person, remote, spoon, toothbrush

## 🧪 Tested On

- OS: Windows 11  
- Python: 3.10.11  
- GPU: NVIDIA GeForce GTX 1650 with Max-Q Design  
- CUDA Version: 12.5 (system), using PyTorch with CUDA 11.8 build  
- PyTorch: 2.1.2 with CUDA 11.8 build  
- Ultralytics: 8.1.23  
- OpenCV: 4.9.0.80


