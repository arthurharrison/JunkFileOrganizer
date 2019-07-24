import os
import shutil

# por fim adicionar interface visual para nao precisar por o script no local, e pela interface informa a pasta, e assim pego o path
PATH = './'
EXTENSIONS = {
    "EXECUTABLES": ['.exe', '.msi', '.apk'],
    "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
               '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd'],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
               ".mpg", ".mpeg", ".3gp"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "DOCUMENTS": ['.txt',  '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.xps', '.dotx', '.docm', '.dox', '.xls', '.xlsx', '.ppt', '.pptx'],
    "PDFS": ['.pdf'],
    "ZIPPEDS": ['.rar', '.zip', '.7z',
                '.gzip']

}


def printFilesList(files):
    print("The following files are located in this folder:")
    for file in files:
        print(file)


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
    printFilesList(filesList)

    confirm = input("Should you proceed with this operation ?(Y/N)")
    if(confirm[0].capitalize() == "N"):
        print("Have a good day :)\nBye!")
        exit()

    filesListIndex = 1
    fileListTotal = len(filesList)
    for currentFile in filesList:
        currentFileExtension = str(currentFile[currentFile.rfind('.'):])

        for fType, extList in EXTENSIONS:
            for currentExtension in extList:
                if currentFileExtension == currentExtension:
                    print(
                        f'Now moving: {currentFile} to {fType} ----- {filesListIndex} of {fileListTotal}')
                    organizer(currentFile, fType.capitalize())
                    filesListIndex += 1

    print('\nFinnaly its done!\nEnjoy!')


if __name__ == "__main__":
    main()
