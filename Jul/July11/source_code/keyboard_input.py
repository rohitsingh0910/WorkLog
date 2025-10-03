from pywinauto.application import Application

# Start Notepad
app = Application().start("notepad.exe")
notepad = app.window(title_re=".*Notepad")

# Type using keyboard
notepad.type_keys("Hello Pywinauto!{ENTER}", with_spaces=True)

# Simulate key combinations
notepad.type_keys("^a")  # Ctrl+A (Select All)
notepad.type_keys("^c")  # Ctrl+C (Copy)
notepad.type_keys("^v")  # Ctrl+V (Paste)
