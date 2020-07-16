from tkinter import simpledialog, messagebox, Tk 
import random

if __name__ == '__main__':

    window=Tk()
    window.withdraw()
    
    
    nm = (random.randint(1,100))
    count = 0
    gameEnd = 0
    
    
    while gameEnd == 0:
        
        if count >= 10:
            gameEnd = 2
        guess1 = simpledialog.askinteger('I,m thinking of a number between 1 and 100.','What do you think it is?')
        count += 1
        
        if guess1 == nm:
            gameEnd = 1
            messagebox.showinfo('Good job.', 'You,ve successfully guessed my number, '+ str(nm) +', in '+ str(count) +' attempts.')
            exit()
        
        else:
            if nm < guess1:
                messagebox.showinfo('So close, but no cigar.', 'Aim a little lower, buckaroo.')
            else:
                messagebox.showinfo('So close, but no cigar.', 'Aim a little higher, sport.')          
                   
    messagebox.showinfo(None, 'Sorry, Buddy, but I was thinking of '+ str(nm) + '. Better luck next time.')
        
        
window.mainloop()