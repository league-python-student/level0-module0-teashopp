import tkinter, messagebox, simpledialog, Tk 

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    i = simpledialog.askinterger(None, prompt='Give an interger:')
    
    i += 1
    i = i + 1
    
    str(i)
    
    print('My number is ' + str(i))
    
    var = 1
    
    int(var)
    
    window.mainloop()