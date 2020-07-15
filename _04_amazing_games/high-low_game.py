from tkinter import simpledialog, Tk 
    
if __name__ == '__main__':

    window=Tk()
    window.withdraw()
    
    v = (random.randint(1,100))
    
    counter = 0
    gameEnd = 0
    
    guess1 = simpledialog.interger(title=None, prompt='What number am I thinking of?')
    counter+=1

    if guess1 == v:
        gameEnd = 1
    else:
        if v>guess1:
            messagebox.showinfo('Too Low! Try Again!')
        else:
            messagebox.showinfo('Too High! Try Again!')
            
    messagebox.showinfo('Perfect! The number I was thinking of was '+v)
window.mainloop()