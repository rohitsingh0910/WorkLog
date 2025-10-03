from pywinauto.application import Application

# Connect to already opened Notepad
app = Application().connect(title_re=".*Notepad")

# Focus on the window
notepad = app.window(title_re=".*Notepad")
notepad.set_focus()
notepad.type_keys("App attached successfully!", with_spaces=True)
