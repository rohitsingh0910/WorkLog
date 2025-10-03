from pywinauto.application import Application

# Print window and child elements of Notepad
app = Application().connect(title_re=".*Notepad")
window = app.window(title_re=".*Notepad")
window.print_control_identifiers()
