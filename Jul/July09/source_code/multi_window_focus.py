from pywinauto.application import Application

# Launch both Notepad and Calculator
notepad_app = Application().start("notepad.exe")
calc_app = Application().start("calc.exe")

notepad = notepad_app.window(title_re=".*Notepad")
calc = calc_app.window(title_re=".*Calculator")

# Focus and interact with Notepad
notepad.wait('ready')
notepad.set_focus()
notepad.type_keys("Switching to Calculator...", with_spaces=True)

# Focus and interact with Calculator
calc.wait('ready')
calc.set_focus()
