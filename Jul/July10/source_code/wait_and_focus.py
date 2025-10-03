from pywinauto.application import Application

app = Application().start("notepad.exe")
notepad = app.window(title_re=".*Notepad")

# Wait until ready
notepad.wait("exists enabled visible ready")
notepad.set_focus()
notepad.type_keys("Waiting worked!", with_spaces=True)
