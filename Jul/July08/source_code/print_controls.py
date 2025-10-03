from pywinauto.application import Application

# Connect to Notepad and list child elements
app = Application().connect(title_re=".*Notepad")
notepad = app.window(title_re=".*Notepad")
notepad.print_control_identifiers()
