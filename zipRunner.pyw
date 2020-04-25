import os, time
import subprocess
from zipfile import ZipFile

path_to_watch = "C:\\Users\\Ben_h\\Downloads\\"
zipDirectory = "C:\\Users\\Ben_h\\Downloads\\ZipExtraction\\"
before = dict([(f, None) for f in os.listdir(path_to_watch)])
while 1:
    time.sleep(2)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        for x in added:
            if x.endswith('.zip'):
                print('Added Zip')
                with ZipFile(path_to_watch + x, 'r') as zipObj:
                    zipObj.extractall(path=zipDirectory)    
            elif x.endswith('.exe'):
                print('Added executable')
                subprocess.call([path_to_watch + x])
            else:
                print("Added normal")
    before = after