from tkinter import messagebox, simpledialog, Tk

window=Tk()

window.withdraw()

print('hello')

messagebox.showinfo(title='what do they call a big mac over there', message='a big mac is a big mac, but they call it le big mac')

name=simpledialog.askstring(None,prompt='so what do they call a quarter pounder with cheese over there?')

messagebox.showerror(None,promt='Huh,'+name+"it's really the litte differences that get ya")

window.mainloop()