import cv2

def draw_trail(frame, trail):
    for i in range(1, len(trail)):
        if trail[i - 1] is None or trail[i] is None:
            continue
        cv2.line(frame, trail[i - 1], trail[i], (0, 0, 255), 2)
