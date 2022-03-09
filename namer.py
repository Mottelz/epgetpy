import os
import utils


def rename_files(directory, new_names, extension, rename=True):
    os.chdir(directory)
    old_names = list_files_with_extension(directory, extension)
    for i in range(len(old_names)):
        if rename:
            os.rename(old_names[i], f"{utils.make_safe(new_names[i])}.{extension}")
        else:
            print(f'{old_names[i]} -> {utils.make_safe(new_names[i])}.{extension}')


def list_files_with_extension(directory, extension):
    os.chdir(directory)
    return [file for file in os.listdir() if file.endswith(extension)]


if __name__ == '__main__':
    test_data = list_files_with_extension(r"D:/Users/Mottel/Downloads/Torrents/Euphoria", 'mp4')
    for f in test_data:
        print(f)
