"""
This file has to be used as a main file for installing n on computer
Using python3 in /usr/bin/
Using java 8 or higher
"""

import os
import subprocess
import datetime
import time
from pathlib import Path


def shell(string):
    # just symplifying commands that used mostly in this script
    r = subprocess.run(string, shell=True)
    return r


class Plist:

    HOMEPATH = str(Path.home()) 
    PLISTPATH = HOMEPATH + "/Library/LaunchAgents"
    NPATH = os.path.dirname(os.path.abspath(__file__))
    PLIST_NAME = "/ru.jperelygin.reminder.n_app.plist"

    SCRIPT_PATH = NPATH + "/reminder.py"

    PLIST = """
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>ru.jperelygin.reminder.n_app</string>
        <key>Program</key>
            <string>{}</string>
        <key>StartCalendarInterval</key>
        <dict>
            <!-- Every Friday at 16:25 CET -->
            <key>Weekday</key>
            <integer>5</integer>
            <key>Hour</key>
            <integer>16</integer>
            <key>Minute</key>
            <integer>25</integer>
        </dict>
    </dict>
    </plist>""".format(SCRIPT_PATH)

    def create_plist(self, name, plist):
        plist_file = self.PLISTPATH + name #"/ru.jperelygin.reminder.n_app.plist"
        with open(plist_file, "w+") as file:
            file.write(plist)

        print("plist created!")

    def make_script_runnable(self, script_path):
        r = shell(f"chmod +x {script_path}")
        if r != 0:
            print(f"Script in {script_path} is still not runnable!!")

    def load_plist(self, name):
        time.sleep(3)
        r = shell(f"launchctl load {self.PLISTPATH}{name}")
        if r != 0:
            print(f"Could not load plist {name}!")
        print(f"plist {name} is loaded!")

    def unload_plist(self, name):
        #just for tests
        r = shell(f"launchctl unload {self.PLISTPATH}{name}")
        if r !=0:
            print("plist is not unloaded!?!")
        print("plist is unloaded!\n")
        shell("launchctl list | grep \"ru\"")

    def maintain(self, plist_name, plist, script_path):
        # main function
        self.create_plist(plist_name, plist)
        self.make_script_runnable(script_path)
        self.load_plist(plist_name)


class N_Installer:
    NPATH = os.path.dirname(os.path.abspath(__file__))
    HOMEPATH = str(Path.home()) 
    TARGET_PATH = NPATH + "/target/classes/"
    JAVA_PATH = NPATH + "/src/main/java/"
    JAVA_FILE = JAVA_PATH + "" # ADD: filename

    def create_n(self, java_file):
        r = shell(f"javac -d {self.TARGET_PATH} {self.JAVA_FILE}")
        if r != 0:
            print(f"{self.JAVA_FILE} is not compiled!!")
        print(f"{self.JAVA_FILE} is compiled successfully!")

    def create_sqlite_db(self):
        # TODO: code it! Create new db while maintaining
        # Save address into resources folder!!! with create_resource_xml() function!
        # Tables:
        # 1. Notes
        # Id | Date | Title | Body | Tags
        pass

    def create_resource_txt(self):
        #TODO: Refactor into xml!
        pass

    def create_resource_xml(self):
        pass

    def create_n_script(self):
        #TODO: creating script. Try to put it into /usr/bin
        #
        pass


if __name__ == "__main__":
    #make_script_runnable("/Users/ivanperelygin/python/test_print.sh")
    pass
