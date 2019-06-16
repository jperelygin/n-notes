"""
This file has to be used as a main file for installing n on computer
Using python3 in /usr/bin/
Using java 8 or higher
"""

import os
import subprocess
import datetime
import time
import json
import sqlite3
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
        print("---plist created!")

    def make_script_runnable(self, script_path):
        r = shell(f"chmod +x {script_path}")
        if r != 0:
            print(f"Script in {script_path} is still not runnable !!!")

    def load_plist(self, name):
        time.sleep(3)
        r = shell(f"launchctl load {self.PLISTPATH}{name}")
        if r != 0:
            print(f"Could not load plist {name} !!!")
        else:
            print(f"---plist {name} is loaded!")

    def unload_plist(self, name):
        #just for tests
        r = shell(f"launchctl unload {self.PLISTPATH}{name}")
        if r !=0:
            print("plist is not unloaded !?!")
        else:
            print("---plist is unloaded!\n")
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
    RESOURCES_PATH = NPATH + "/src/main/resources"
    JAVA_FILE = JAVA_PATH + "/Main.java"

    def create_n(self, java_file):
        # Not usefull anymore. Need to fix into mvn script
        r = shell(f"javac -d {self.TARGET_PATH}/{self.JAVA_FILE}")
        if r != 0:
            print(f"{self.JAVA_FILE} is not compiled !!!")
        else:
            print(f"---{self.JAVA_FILE} is compiled successfully!")

    def create_sqlite_db(self):
        # Notes.db
        # Tables:
        # 1. Notes
        # Id (Primary key, autoincr) | Date | Title | Body | Tags
        connect = sqlite3.connect(self.NPATH + "/Notes.db")
        c = connect.cursor()
        c.execute("""CREATE TABLE Notes(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT,
            Title TEXT,
            Body TEXT,
            Tags TEXT)""")
        connect.commit()
        print(f"---Database {self.NPATH}/Notes.db is initialised!")

    def create_resource_json(self):
        config_file = self.NPATH + "/config.json"
        shell(f"touch {config_file}")
        with open(config_file, "w+") as jsn:
            address = self.NPATH + "/Notes.db"
            jsn.write(json.dumps({"ServerAddress": address}))
        print(f"---Address of the database is written into {config_file}")

    def create_n_script(self):
        n_path = self.NPATH + "/n"
        with open(n_path, "w+") as n:
            n.write("#!/bin/bash\n")
            n.write(f"java -jar {self.NPATH}/n-1.jar") # "Works after mvn clean package" and renaming n-1.jar into n.jar
        shell(f"chmod +x {n_path}")§
        shell(f"mv {n_path} /usr/local/bin/")


def maintain(n_installer: N_Installer):
    # main function that would build everything
    n_installer.create_sqlite_db()
    n_installer.create_resource_json()
    n_installer.create_n_script()
    p = Plist()
    # p.maintain() deal with it later


def install():
    # Using for installing into /usr/local/n
    n = N_Installer()
    #shell(f"mkdir /usr/local/n")
    shell(f"cp -r {n.NPATH}/ /usr/local/n")
    n.NPATH = "/usr/local/n"
    maintain(n)


if __name__ == "__main__":
    install()
