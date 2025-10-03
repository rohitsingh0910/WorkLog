from pywinauto.application import Application

# Example only if you have an app with checkboxes
app = Application().start("mspaint.exe")
paint = app.window(title_re=".*Paint")
paint.set_focus()

# You can explore with print_control_identifiers to find buttons
paint.print_control_identifiers()
