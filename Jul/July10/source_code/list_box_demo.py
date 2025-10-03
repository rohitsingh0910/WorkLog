from pywinauto.application import Application

# You can try with WordPad or any list box based app
app = Application().start("wordpad.exe")
wordpad = app.window(title_re=".*WordPad")
wordpad.print_control_identifiers()  # Then identify the list box if available
