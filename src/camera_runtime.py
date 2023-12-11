import cv2
import numpy as np
import requests
from roboflow import Roboflow
import time
import threading

class CameraOBJ:
    def __init__(self):
        self.machine_capture = cv2.VideoCapture(0)
        self.detect_status  = 0
        self.original_image = np.zeros((1080, 1920, 3), dtype=np.uint8)
        self.output_frame = np.zeros((480, 270, 3), dtype=np.uint8)
        self.status_subsidi = 0
        self.jenis_mobil = f"Predict ..."
        self.detect_toggle_timer = time.time()
        self.detect_toggle_interval = 3  # interval
        # self.rf = Roboflow(api_key="LXOurZvEHJmFoPfA7TeR")
        # self.project = self.rf.workspace().project("rsbp_kelompok3")
        # self.model = self.project.version(1).model
        self.rf = Roboflow(api_key="0luIXfVr4TvXOnHEZrhm")
        self.project = self.rf.workspace().project("smart-nozzle")
        self.model = self.project.version(1).model
        self.frame_lock = threading.Lock()
       
    def switch_detect_status(self):
        self.detect_status = not self.detect_status

    def send_frame_to_roboflow(self, frame):
        # Perform object detection on the frame and return the JSON response
        response = self.model.predict(frame, confidence=70, overlap=40).json()

        if "predictions" in response and len(response["predictions"]) > 0:
            class_value = response["predictions"][0]["class"]
            self.jenis_mobil = f"{class_value}"
            # if self.jenis_mobil == "SUV-MPV" or self.jenis_mobil == "Hatchback" :
            if self.jenis_mobil == "Honda Brio" or self.jenis_mobil == "Honda Jazz" or self.jenis_mobil == "Toyota Avanza" :
                self.status_subsidi = 1
            else :
                self.status_subsidi = 0
        else :
            self.status_subsidi = 0
            self.jenis_mobil = f"Predict.."
        # print(response, self.status_subsidi)

        return response
    
    def send_frame_to_roboflow_threaded(self, frame):
        with self.frame_lock:
            # Send the frame to Roboflow for object detection
            self.send_frame_to_roboflow(frame)
    
    def capture_runtime(self):
        while True:
            # Check if it's time to toggle detect status
            if time.time() - self.detect_toggle_timer >= self.detect_toggle_interval:
                self.switch_detect_status()
                self.detect_toggle_timer = time.time()

            success, frame = self.machine_capture.read()
            if not success:
                break
            else:
                if self.detect_status == 0:
                    self.output_frame = cv2.resize(frame, (480, 270))
                else:
                    # Start a new thread for sending the frame to Roboflow
                    send_thread = threading.Thread(target=self.send_frame_to_roboflow_threaded, args=(frame,))
                    send_thread.start()

                    # Update the output frame with the processed frame
                    self.output_frame = cv2.resize(frame, (480, 270))
                    self.switch_detect_status()

                ret, buffer = cv2.imencode('.jpg', self.output_frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

                # Wait for the send_thread to finish
                # send_thread.join()