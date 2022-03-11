import cv2


path_dir: str = r"C:\Users\user\Downloads\vids"

# Count via cv2
def fps(video):
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps
    
    
def count_frames_manual(video):
    # initialize the total number of frames read
    total = 0

    # loop over the frames of the video
    while True:
        # grab the current frame
        (grabbed, frame) = video.read()

        # check to see if we have reached the end of the
        # video
        if not grabbed:
            break

        # increment the total number of frames read
        total += 1

    # return the total number of frames in the video file
    return total
        

fps_list = []
frames_list = []
lenght_list = []

for path_file in get_files_in_folder_2(path_dir):

    video = cv2.VideoCapture(path_file)

    fps_value = fps(video)
    frames = count_frames_manual(video)
    lenght = frames/fps_value

    fps_list.append(fps_value)
    frames_list.append(frames)
    lenght_list.append(lenght)

    print(f'filename:{path_file}, fps:{fps_value}, frames:{frames}, lenght: {lenght}')
