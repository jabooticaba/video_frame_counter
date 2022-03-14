import cv2


def video_reader(video_file_path):
    return cv2.VideoCapture(video_file_path)


# Count via cv2
def fps(video):
    video = video_reader(video)

    fps = video.get(cv2.CAP_PROP_FPS)
    return fps
    
    
def count_frames_manual(video):

    video = video_reader(video)
    total = 0

    # loop over the frames of the video
    while True:
        (grabbed, frame) = video.read()

        if not grabbed:
            break

        total += 1

    return total


def summary(file_path):

    fps_value = round(fps(file_path), 1)
    frames = round(count_frames_manual(file_path), 1)
    length = round(frames / fps_value, 2)

    return fps_value, frames, length

