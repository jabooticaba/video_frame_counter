import os
import PySimpleGUI as sg

from frame_counter import count_frames_manual, fps, video_reader


sg.theme('Dark Blue 3')

layout = [[sg.Text('FPS counter')],
      [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
      [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('Указать путь к файлам', layout)

event, values = window.read()

folder_path, file_path = values[0], values[1]       # get the data from the values dictionary

print(folder_path, file_path)

if folder_path:
    dir_content = os.listdir(folder_path)

    for filename in dir_content:
        file_path = os.sep.join([folder_path, filename])

        try:
            fps_value = fps(file_path)
            frames = count_frames_manual(file_path)
            lenght = frames/fps_value

            # TODO Выводит попапы один за одним для каждого файла, переделать на таблицу результатов
            sg.popup(f'fps:{fps_value}, frames:{frames}, lenght: {lenght}, filename:{file_path}')

        except Exception as e:
            sg.popup_error(f'Error: {e}')

if file_path:
    fps_value = fps(file_path)
    frames = count_frames_manual(file_path)
    lenght = frames / fps_value

    # TODO Переделать в виде таблицы в дополнительную секцию основного окна
    sg.popup(f'fps:{fps_value}, frames:{frames}, lenght: {lenght}, filename:{file_path}')

window.close()




