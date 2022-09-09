import os
import shutil

def new_folder():
    for file in extension_dict:
        if file not in os.listdir(path):
            os.mkdir(os.path.join(path, file))

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            old_path = os.path.join(path, file)

            for file_1 in extension_dict:  # For loop to move file into folder
                extension = extension_dict[file_1]
                if file.endswith(extension):
                    destination_path = os.path.join(path, file_1, file)
                    shutil.move(old_path, destination_path)
                    break


def rem_folder():  # Organize folder
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
                shutil.move(old_path, destinationPath)
            except shutil.Error:
                shutil.move(old_path, destinationPath + " - copy")


def rem_file():  # if others file extension not in the dictinory it'll handle in this fnction
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            old_path = os.path.join(path, file)
            destinationPath = os.path.join(path, ls[9], file)
            shutil.move(old_path, destinationPath)


def delete_empty_folder():  # Delete Remaining Empty Folder
    for entry in os.scandir(path):
        if os.path.isdir(entry.path) and not os.listdir(entry.path):
            os.rmdir(entry.path)


if __name__ == '__main__':  # main method

    # path = os.getcwd()    #uncomment this if you want to organize the same path which this code is in
    path = r" put your path to organize here "  # choose either one and comment this if you want to use same directory

    extension_dict = {
        # All extension and folder name is in here.. The Folder name will be in dictinory key and extension will be dictinory value
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

    ls = list(extension_dict)  # convert dictinory into list

    for file in os.listdir():

        try:
            new_folder()
            rem_file()
            rem_folder()
            delete_empty_folder()
            print("Done")

        except shutil.Error as e:
            print(e)
            break

        except Exception as k:
            print(k)
            break

