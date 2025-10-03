from pywinauto.application import Application

# Connect to already open Notepad and close it
app = Application().connect(title_re=".*Notepad")
notepad = app.window(title_re=".*Notepad")
notepad.set_focus()
notepad.type_keys("Now closing...", with_spaces=True)
notepad.close()
