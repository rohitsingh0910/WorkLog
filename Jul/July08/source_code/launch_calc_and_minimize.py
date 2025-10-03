from pywinauto.application import Application

# Start Calculator and minimize it
app = Application().start("calc.exe")
calc = app.window(title_re=".*Calculator")
calc.wait('ready')
calc.minimize()
