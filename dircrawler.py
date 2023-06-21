import os

rootDir = os.getcwd()

sep = "/"
if os.name == 'nt':
    sep = "\\"

for directory, subdirectoryList, fileList in os.walk(rootDir):
    for filename in fileList:
        print(f'{directory}{sep}{filename}')