from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

# Open two File Explorers
app1 = Application().start("explorer.exe C:\\Users\\Public\\Documents")
app2 = Application().start("explorer.exe C:\\Users\\Public\\Downloads")

win1 = app1.window(title_re=".*Documents")
win2 = app2.window(title_re=".*Downloads")

win1.wait("ready", timeout=10)
win2.wait("ready", timeout=10)

# Use coordinates OR locate via controls (approx example below)
src_rect = win1.rectangle()
dst_rect = win2.rectangle()

# Move mouse and drag file (simulating drag-and-drop across windows)
win1.drag_mouse_input(dst=(dst_rect.mid_point().x, dst_rect.mid_point().y))
