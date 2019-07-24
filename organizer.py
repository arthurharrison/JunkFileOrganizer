import os
import shutil

# TODO: Better documentation, do a GUI, deal with a proper count of the files located
PATH = './'
EXTENSIONS = {
    "EXECUTABLES": ['.exe', '.msi', '.apk'],
    "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
               '.png', '.bpg', '.svg', '.heif', '.psd'],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
               ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "DOCUMENTS": ['.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.xps', '.dotx', '.docm', '.dox', '.xls', '.xlsx', '.ppt', '.pptx'],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDFS": ['.pdf'],
    "ZIPPEDS": ['.rar', '.zip', '.7z', '.bzip2',
                '.gzip', '.tar', '.wim', '.xz', ]
}


def printFilesList(files):
    fileListTotal = 0
    print("The following files are located in this folder:")
    for file in files:
        if('.' in file):
            fileListTotal += 1
        print(file)
    fileListTotal -= 1  # excluding the .py file that executes this
    return fileListTotal


def organizer(fileName, destinyFolder):
    if not os.path.exists(destinyFolder):
        os.makedirs(destinyFolder)
    filesMover(fileName, destinyFolder)


def filesMover(fileName, destinyFolder):
    try:
        shutil.move(fileName, destinyFolder)
    except Exception as e:
        print(
            f'During the process of moving {fileName} a Error has appeared: \n{e}')


def main():
    filesList = os.listdir(PATH)
    fileListTotal = printFilesList(filesList)

    confirm = input("\nShould you proceed with this operation ?(Y/N)\n")
    if(confirm[0].capitalize() == "N"):
        print("Have a good day :)\nBye!")
        exit()

    filesListIndex = 1

    for currentFile in filesList:
        currentFileExtension = str(currentFile[currentFile.rfind('.'):])

        for fType, extList in EXTENSIONS.items():
            for currentExtension in extList:
                if currentFileExtension == currentExtension:
                    print(
                        f'Now moving: {currentFile} to {fType} ----- {filesListIndex} of {fileListTotal}')
                    organizer(currentFile, fType.capitalize())
                    filesListIndex += 1

    print('\nFinnaly its done!\nEnjoy!')


if __name__ == "__main__":
    main()
