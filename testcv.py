import cv2
import numpy as np
import time

def capture_and_display():
    # Open video capture device
    cap = cv2.VideoCapture(0)  # /dev/video0 corresponds to index 0
    
    # Set video format properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('R', 'G', 'B', '3'))
    
    # Set buffer size (equivalent to --stream-mmap=4)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 4)
    
    if not cap.isOpened():
        print("Error: Could not open video device")
        return
    
    print("Video device opened successfully")
    print(f"Resolution: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
    
    frame_count = 0
    skip_frames = 3  # Equivalent to --stream-skip=3
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Failed to capture frame")
                break
            
            frame_count += 1
            
            # Skip frames as specified
            if frame_count <= skip_frames:
                continue
                
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Display the frame
            cv2.imshow('HDMI Input', frame)
            
            # Break on 'q' key press or ESC
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                break
            
            
            # Optional: Capture only 2 frames (equivalent to --stream-count=2)
            # Uncomment the following lines if you want to capture only 2 frames
            # if frame_count - skip_frames >= 2:
            #     break
    
    except KeyboardInterrupt:
        print("\nCapture interrupted by user")
    
    finally:
        # Clean up
        cap.release()
        cv2.destroyAllWindows()
        print("Video capture released")

if __name__ == "__main__":
    capture_and_display()
