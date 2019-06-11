import maintain
import time


plister = maintain.Plist()
script = plister.NPATH + "/test_reminder.py"

test_plist = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>ru.jperelygin.reminder.n_app</string>
    <key>Program</key>
        <string>{}</string>
    <key>StartInterval</key>
    <integer>20</integer>
</dict>
</plist>""".format(script)

name = "ru.jperelygin.test_reminder.plist"


if __name__ == "__main__":
    plister.create_plist(name, test_plist)
    plister.make_script_runnable(script)
    plister.load_plist(name)
    time.sleep(40)
    plister.unload_plist(name)