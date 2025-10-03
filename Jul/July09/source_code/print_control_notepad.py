from pywinauto.application import Application

# List all controls in Notepad
app = Application().connect(title_re=".*Notepad")
window = app.window(title_re=".*Notepad")
window.print_control_identifiers()
