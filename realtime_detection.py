from ultralytics import YOLO
import cv2
import time

# Load YOLOv8 small model (accurate & real-time capable)
model = YOLO("yolov8s.pt")  # Make sure this file exists or is downloaded

# Open webcam (0 = default)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize trackers
frame_count = 0
start_time = time.time()
detected_objects = set()  # To track unique labels

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to speed up processing
    frame = cv2.resize(frame, (640, 480))

    # Run inference using YOLO
    results = model(frame)

    # Loop over detections and collect unique object labels
    for box in results[0].boxes:
        class_id = int(box.cls[0].item())
        label = results[0].names[class_id]
        print("Detected:", label)
        detected_objects.add(label)

    # Annotate the frame with bounding boxes
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    frame_count += 1

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

# Final performance reporting
elapsed_time = time.time() - start_time
fps = frame_count / elapsed_time

print(f"\n--- Performance Summary ---")
print(f"Total Frames Processed: {frame_count}")
print(f"Average FPS: {fps:.2f}")
print(f"Unique objects detected: {len(detected_objects)}")
print("Objects:", ', '.join(sorted(detected_objects)))
