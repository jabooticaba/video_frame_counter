from os import listdir, sep


def get_files_in_folder(folder) -> list:
    """Возвращает список с путями до файлов папки folder.

    :param folder: Путь до папки
    :return: List
    """
    file_list = []

    for filename in listdir(folder):
        path_file = sep.join([folder, filename])
        file_list.append(path_file)

    return file_list
