import tkinter as tk
import sqlite3
a=tk.Tk()
a.title("Test GUI")
a.geometry("360x650")
tk.Entry().place()
a.mainloop()
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("create Table Mirafra(sales char (99),salary int(32)")
conn.commit()
conn.close()
