from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

print('print message')
messagebox.showinfo(None,message='message box message')

age = simpledialog.askstring(None,prompt='What is your age?')

if age == '10':
    print('impressive')
elif age == '15':
    print('perfect')
else:
    print('dissapointing')

window.mainloop()