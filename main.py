import os
from pandas import DataFrame
import PySimpleGUI as sg

from frame_counter import summary


sg.theme('Dark Blue 3')

data = []
headings = ['File name', 'FPS  ', 'Frames', 'Length']
row_counter = 0


def draw_table(data_list):
    global row_counter

    result = data_list

    result = [os.path.basename(file_path), result[0], result[1], result[2]]
    data.append(result)
    row_counter += 1

    return data


layout = [[sg.Text('Указать путь к файлам')],
          [sg.Text('Выбрать папку', size=(21, 1)), sg.InputText(do_not_clear=False), sg.FolderBrowse('Обзор', key='folder_browse')],
          [sg.Text('Выбрать файл', size=(21, 1)),
           sg.InputText(do_not_clear=False),
           sg.FileBrowse('Обзор', key='file_browse', file_types=(('mp4 video', '*.mp4'),('ALL Files', '*.* *')))],
          [sg.Submit('Вычислить'), sg.Push(), sg.Button('Копировать результат в буфер')],
          [sg.ProgressBar(10, orientation='h', size=(51, 2), border_width=0, key='progbar', visible=True)],
          [sg.Table(values=data, headings=headings,
                    auto_size_columns=False,
                    col_widths=[39, 7, 7, 7],
                    justification='left',
                    num_rows=5,
                    alternating_row_color='light blue',
                    key='-TABLE-')],
          [sg.Button('Очистить таблицу'), sg.Push(), sg.Button('Exit')]
          ]

window = sg.Window('FPS counter', layout)

while True:
    event, values = window.read()

    try:
        folder_path, file_path = values[0], values[1]  # get the data from the values dictionary
    except TypeError:  # ловим ошибку при выходе
        pass

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Копировать результат в буфер':
        file_path = ''
        folder_path = ''
        df = DataFrame(data)
        df.to_clipboard(index=False, header=False)

    if event == 'Очистить таблицу':
        data = []
        file_path = ''
        folder_path = ''
        window['-TABLE-'].update('')
        window['progbar'].update_bar(0)

    if folder_path:
        dir_content = os.listdir(folder_path)
        window['progbar'].update_bar(0, max=len(dir_content))

        for count, filename in enumerate(dir_content):
            file_path = os.sep.join([folder_path, filename])

            if os.path.splitext(file_path)[1] == '.mp4':
                try:
                    window['-TABLE-'].update(values=draw_table(summary(file_path)))
                    window['progbar'].update_bar(count + 1)

                except Exception as e:
                    sg.popup(f'Ошибка: {e}', title='Error')

                window.refresh()

            else:
                window['progbar'].update_bar(count + 1)
                continue

    elif file_path:
        if os.path.splitext(file_path)[1] == '.mp4':
            window['progbar'].update_bar(0, max=1)
            try:
                window['-TABLE-'].update(values=draw_table(summary(file_path)))
                window['progbar'].update_bar(1)
            except Exception as e:
                sg.popup(f'Ошибка: {e}', title='Error')
        else:
            sg.popup(f'Выберите .mp4 файл', title='Error')


window.close()

