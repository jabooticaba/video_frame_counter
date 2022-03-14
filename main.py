import os
import PySimpleGUI as sg

from frame_counter import summary


sg.theme('Dark Blue 3')

data = []
headings = ['Filename', 'FPS', 'Frames', 'Length']
row_counter = 0


def draw_table(data_list):
    global row_counter
    global data

    result = data_list

    # TODO Форматировать размер полей таблицы
    result = [file_path, result[0], result[1], result[2]]
    data.append(result)
    row_counter += 1

    return data


layout = [[sg.Text('Указать путь к файлам')],
          [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
          [sg.Submit(),sg.Push()],
          [sg.Table(values=data, headings=headings,
                    col_widths=[80, 10, 10, 10],
                    auto_size_columns=True,
                    justification='right',
                    num_rows=5,
                    alternating_row_color='light blue',
                    key='-TABLE-',
                    row_height=25)],
          [sg.Button('Clear table'), sg.Push(), sg.Button('Exit')]
          ]

window = sg.Window('FPS counter', layout)

while True:                             # The Event Loop
    event, values = window.read()
    folder_path, file_path = values[0], values[1]  # get the data from the values dictionary

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Clear':
        values[0], values[1] = None, None
        data = []
        window['-TABLE-'].update('')

    if folder_path:
        dir_content = os.listdir(folder_path)

        for filename in dir_content:
            file_path = os.sep.join([folder_path, filename])

            try:
                window['-TABLE-'].update(values=draw_table(summary(file_path)))

            except Exception as e:
                sg.popup_error(f'Error: {e}')

    if file_path:

        window['-TABLE-'].update(values=draw_table(summary(file_path)))


window.close()

