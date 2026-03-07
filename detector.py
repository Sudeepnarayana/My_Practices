from ultralytics import YOLO
import cv2
import time

class ObjectDetector:
    def __init__(self, model_path="models/yolov8m.pt", conf=0.6):
        self.model = YOLO(model_path)
        self.conf = conf

    # -------------------------------------------------
    # Detect objects in single frame
    # classes=None → detect ALL objects
    # classes=[...] → detect specific classes only
    # -------------------------------------------------
    def detect_frame(self, frame, classes=None):
        results = self.model(frame, conf=self.conf, classes=classes)

        annotated = results[0].plot()

        count = len(results[0].boxes)

        return annotated, count


    # -------------------------------------------------
    # Image detection → ALL objects
    # -------------------------------------------------
    def detect_image(self, path):
        img = cv2.imread(path)

        annotated, count = self.detect_frame(img, classes=None)

        cv2.putText(annotated, f"Objects: {count}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        cv2.imshow("Image Detection", annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    # -------------------------------------------------
    # Video detection → ONLY vehicles
    # -------------------------------------------------
    def detect_video(self, source=0):
        cap = cv2.VideoCapture(source)

        if not cap.isOpened():
            print("Error: Cannot open video source")
            return

        prev_time = 0

        vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            annotated, count = self.detect_frame(frame, classes=vehicle_classes)

            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time

            cv2.putText(annotated, f"FPS: {int(fps)}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            cv2.putText(annotated, f"Vehicles: {count}",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            cv2.imshow("Vehicle Detection (Video)", annotated)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    # -------------------------------------------------
    # Webcam detection → ALL objects
    # -------------------------------------------------
    def detect_webcam(self):
        self.detect_video(source=0)   # uses all classes by default
