import cv2
import numpy as np
from utils import draw_trail

INPUT_PATH = '../assets/MacV.mp4'
OUTPUT_PATH = '../output/output_video.mp4'

def main():
    cap = cv2.VideoCapture(INPUT_PATH)
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    # Select multiple objects to track on the first frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read video frame.")
        return

    # Select multiple objects (ROI) and handle cancelation
    rois = cv2.selectROIs("Select Objects", frame, fromCenter=False, showCrosshair=True)
    if len(rois) == 0:
        print("No objects selected. Exiting...")
        return

    trackers = []

    # Create a tracker for each ROI
    for roi in rois:
        tracker = tracker = cv2.TrackerCSRT_create()
        tracker.init(frame, roi)
        trackers.append(tracker)

    fourcc = cv2.VideoWriter_fourcc(*'H', '2', '6', '4')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

    object_id = 0
    centroid_trail = [[] for _ in range(len(rois))]
    object_tracking_times = [0] * len(rois)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for i, tracker in enumerate(trackers):
            success, bbox = tracker.update(frame)
            if success:
                x, y, w, h = [int(v) for v in bbox]
                centroid = (x + w // 2, y + h // 2)
                centroid_trail[i].append(centroid)
                object_tracking_times[i] += 1  

                # Draw bounding box & centroid
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame, centroid, 5, (255, 0, 0), -1)

                # Draw trail for each object
                draw_trail(frame, centroid_trail[i])

        # Draw unique object IDs on the video
        for i in range(len(rois)):
            cv2.putText(frame, f'Object ID: {i+1}', (10, 30 + 30 * i),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        frame_count += 1
        out.write(frame)

        # Show the processed frame
        cv2.imshow('Tracking', frame)

        # Exit the loop when 'ESC' key is pressed
        if cv2.waitKey(int(1000 / fps)) & 0xFF == 27:
            print("Exiting...")
            break
            

    total_time = frame_count / fps
    print(f"\nTotal time in video: {total_time:.2f} seconds")
    print(f"Unique Object IDs: {len(rois)}")

    for i, tracked_frames in enumerate(object_tracking_times):
        time_visible = tracked_frames / fps
        print(f"Object {i+1} visible for: {time_visible:.2f} seconds")

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
