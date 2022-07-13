import os
import utils


def rename_files(directory, new_names, extension, rename=True):
    os.chdir(directory)
    old_names = list_files_with_extension(directory, extension)
    out = []
    for i in range(len(old_names)):
        if rename:
            os.rename(old_names[i], f"{utils.make_safe(new_names[i])}.{extension}")
        else:
            out.append(f'{old_names[i]} -> {utils.make_safe(new_names[i])}.{extension}')
    return out


def list_files_with_extension(directory, extension):
    os.chdir(directory)
    return [file for file in os.listdir() if file.endswith(extension)]


def remove_part_of_filename(directory, extension, string_to_remove):
    old_names = list_files_with_extension(directory, extension)
    new_names = []
    for name in old_names:
        new_names.append(name.replace(string_to_remove, ''))
    print("Suggested rename")
    rename_files(directory, new_names, extension, False)
    if 'y' in input("Rename? ").lower():
        rename_files(directory, new_names, extension, True)


if __name__ == '__main__':
    remove_part_of_filename(input("enter directory: "), input("enter extension: "), input("enter string to remove: "))
