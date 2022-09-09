"""

  ~ If you don't trust the .exe I've compiled.
    you can compile this python code by yourself
        > study this code first before compile it
        > if you're confirmed there's no bad stuff in this code,
           proceed the compilation process

  ~ Install python at www.python.org

  ~ open cmd run this:
        >  pip install nuitka
        >  py -m nuitka --mingw64 --windows-disable-console .\File_Organizer.py --standalone --onefile

  ~ The compiled program is in the dist folder with exe extension
"""

import os
import shutil


def new_folder():  # Create a new folder and move file into the desire folder
    for file in extension_dict:
        if file not in os.listdir(path):
            os.mkdir(os.path.join(path, file))

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            old_path = os.path.join(path, file)

            for file_1 in extension_dict:

                extension = extension_dict[file_1]
                if file.endswith(extension):
                    destination_path = os.path.join(path, file_1, file)

                    if file != "File_Organizer.exe":  # To Exclude File_Organizer.exe from moving into folder
                        shutil.move(old_path, destination_path)
                    break


def rem_folder():  # Move Remaining folder into parent folder
    directory = os.listdir(path)
    organized_folders = []

    for folder in extension_dict:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)

    for folder in directory:
        if folder not in organized_folders:
            old_path = os.path.join(path, folder)
            destinationPath = os.path.join(path, ls[10], folder)
            try:
                if folder != "File_Organizer.exe":
                    shutil.move(old_path, destinationPath)
            except shutil.Error:
                shutil.move(old_path, destinationPath + " - copy")


def rem_file():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            old_path = os.path.join(path, file)
            destinationPath = os.path.join(path, ls[9], file)

            if file != "File_Organizer.exe":
                shutil.move(old_path, destinationPath)


def delete_empty_folder():  # Delete folder if it empty
    for entry in os.scandir(path):
        if os.path.isdir(entry.path) and not os.listdir(entry.path):
            os.rmdir(entry.path)


if __name__ == '__main__':

    path = os.getcwd()  # get current path and store it in path variable

    extension_dict = {  # You can customize this extension and folder name ikut cita rasa sendiri
        "Images": (".jpeg", ".jpg", ".gif", ".png", "svg"),
        "Videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".mpeg", ".3gp", ".mkv"),
        "Documents": (".pages", ".docx", ".doc", ".fdf", ".ods", ".xsn", ".xps", ".dotx", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"),
        "Archives": (".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"),
        "Audio": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "Project Icon": ".ico",
        "Text File": ".txt",
        "Pdf": ".pdf",
        "Exe": ".exe",
        "Other Files": "",
        "Folders": ""
    }

    ls = list(extension_dict)

    for file in os.listdir():

        try:
            new_folder()
            rem_file()
            rem_folder()
            delete_empty_folder()

        except shutil.Error as e:
            print(e)
            break

        except Exception as k:
            print(k)
            break
