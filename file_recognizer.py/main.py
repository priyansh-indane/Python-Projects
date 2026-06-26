import os

current_size = 0
size = 0

while True:
    Folderpath = '##GIVE PATH OF FOLDER'

    for ele in os.scandir(Folderpath):
        size = os.path.getsize(ele)

    if size > current_size:
        print("New file arrived...")
    
    current_size = size
