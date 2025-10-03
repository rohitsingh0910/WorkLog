from pywinauto.application import Application

app = Application().start("notepad.exe")
notepad = app.window(title_re=".*Notepad")

# Click to focus
notepad.click_input()

# Double-click (example only, doesn't do much in notepad)
notepad.double_click_input()

# Right-click in notepad (context menu)
notepad.right_click_input()
