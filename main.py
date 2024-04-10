import shutil, os
import send2trash
import sys

from pathlib import Path
###SETTINGS###

desktop = os.environ['ONEDRIVE']+"\\Desktop"


##
public_desktop = os.environ['PUBLIC']+"\\Desktop"

backup_folder = os.environ['ONEDRIVE']+"\\Desktop\\desktop_backup"

ignore = ["Discord.lnk", "desktop.ini", "GitHub Desktop.lnk", "Tiled.lnk", "Radzen.lnk"
    , "Steam.lnk", "Unity Hub.lnk", "Google Chrome.lnk"]

extensions_delete = ["url", "lnk"]



###TODO
# create logfile for errors
# create config file for ease of setup
# create batch file to run the script or use advanced python scheduler
###

def ensure_backup():
    if (os.path.exists(backup_folder)):
        return
        #print(f"backup folder exists at: {backup_folder}")
    os.mkdir(backup_folder)
    #print(f"backup folder created at: {backup_folder}")


def purge_desktop(path):
    for filename in os.listdir(Path(path)):
    #for filename in os.listdir(r"C:\Users\jrgra\OneDrive\Desktop"):
        if((filename in ignore) or (filename == backup_folder.split('\\')[-1])): #file is to not be touched
            # do nothing with file
            #print(f"{filename}: KEEP")
            continue
        if(os.path.isfile(path+"\\"+filename)):
            if(filename.split('.')[-1] in extensions_delete):
                #print(f"{filename}: DELETED")
                send2trash.send2trash(path+"\\"+filename)
                continue
        #print(f"{filename}: MOVE")
        shutil.move(path+"\\"+filename, backup_folder)


if __name__ == '__main__':
    ensure_backup()
    purge_desktop(desktop)
    purge_desktop(public_desktop)


