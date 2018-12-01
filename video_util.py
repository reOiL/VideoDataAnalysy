import cv2
import file_util


def clip_video(file_name, out_file_type):
    video_stream = cv2.VideoCapture(file_name)
    FPS = video_stream.get(cv2.CAP_PROP_FPS)
    list_frames = []

    while True:
        for i in range(int(FPS)):  # skip some frames
            video_stream.grab()

        (grabbed, frame) = video_stream.read()

        if not grabbed:
            return list_frames

        list_frames.append(bytearray(cv2.imencode(out_file_type, frame)[1]))

# file_util.save_mas_file('video', 'jpeg', clip_video('l_07_persons_1_01.mp4', '.jpeg')) # example
