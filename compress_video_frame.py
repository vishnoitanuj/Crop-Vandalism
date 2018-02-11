'''
This file removes frames from a videofile.
The resulting file will look faster when played back at normal speed.
The idea is to create video that can be processed by yolo and look normal speed 
'''

import cv2
import numpy as np

source_video_path = '../cruise.mp4'
capture = cv2.VideoCapture(source_video_path)
size = (
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)
codec = cv2.VideoWriter_fourcc(*'DIVX')

final_video_name = 'cruise_20_fps.avi'
output = cv2.VideoWriter(final_video_name, codec, 60.0, size)

i = 0
frame_rate_divider = 10
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        if i % frame_rate_divider == 0:
            # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
            output.write(frame)
            cv2.imshow('frame', frame)
            i += 1
        else:
            i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()