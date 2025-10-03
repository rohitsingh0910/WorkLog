from pywinauto.application import Application

# Start Calculator
app = Application().start("calc.exe")
app.window(title_re=".*Calculator").wait('ready').print_control_identifiers()
