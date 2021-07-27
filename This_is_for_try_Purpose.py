
#todo : Messagebox in Python Without window 1
from tkinter import *
from tkinter import messagebox
window = Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.withdraw()
messagebox.showwarning("Warning","Warning message")
window.deiconify()
window.destroy()
window.quit()
exit()

#todo : Messagebox in Python Without window 2
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.overrideredirect(1)
root.withdraw()
messagebox.showinfo("Showinfo", "So many windows!")
root.destroy()
exit()

#todo : Messagebox in Python 3
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()
# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
exit()

#todo : Messagebox in Python Without window 4
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.overrideredirect(1)
root.withdraw()
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askretrycancel("askretrycancel", "Try again?")
messagebox.showinfo("showinfo", "Information")
root.destroy()
exit()

#todo : Notification Label with python
from plyer import notification
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"E:\Python\Cs_Project\Hotel_icon.ico",
        timeout = 6
    )
notifyMe("Ujjwal Saini","Ujjwal you are the python intermediate level programmer")
exit()