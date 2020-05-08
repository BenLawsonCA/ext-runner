import os, time
import subprocess
from zipfile import ZipFile
import action as action

path_to_watch = "C:\\Users\\Ben_h\\Downloads\\"
zipDirectory = "C:\\Users\\Ben_h\\Downloads\\ZipExtraction\\"
cfg = {
    "dir": "C:/Users/%USERNAME%/Downloads",
    "actions": [
        {
            "pattern": "*.zip",
            "command": "powershell.exe Expand-Archive -Force {name}{ext} {name}"
        },
        {
            "pattern": "*.exe",
            "command": "powershell.exe  .\{name}{ext}"
        }
    ]
}


# name, ext = os.path.splitext(example_file)
#
# # Get the first action from the list of actions in the config file.
# action = cfg["actions"][0]
#
# # Replace {name} with the name of the file, and {ext} with the extension.
# cmd = action["command"].replace("{name}", name).replace("{ext}", ext)
# print(cmd)
#
# # Execute the command and get the output (usually no output).
# out = subprocess.check_output(cmd)
# print(out)

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
                result = tkinter.messagebox.askquestion(title=Confirm Procses, message="Do you want to run the .exe added to" + path_to_watch)
                if result == "yes":
                    print('Added executable')
                    subprocess.call([path_to_watch + x])
                else:
                    print('Cancelled running executable!')
            else:
                print("Added normal")
    before = after