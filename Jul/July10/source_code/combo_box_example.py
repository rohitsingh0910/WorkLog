from pywinauto.application import Application

app = Application().start("notepad.exe")
notepad = app.window(title_re=".*Notepad")
notepad.type_keys("Combo box example", with_spaces=True)

# Open Save As dialog
notepad.menu_select("File->Save As")
save_dialog = app.window(title_re=".*Save As")
save_dialog.wait("ready")

# Select file type from combo box
combo = save_dialog.child_window(auto_id="1148", control_type="ComboBox")
combo.select("All Files (*.*)")

# Set filename
save_dialog.child_window(auto_id="1001", control_type="Edit").set_text("combo_example.txt")

# Click Save
save_dialog.child_window(title="Save", control_type="Button").click()
