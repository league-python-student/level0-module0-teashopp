from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
# Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
    v1 = (random.randint(0,3))
    # 2. Print your variable to the console
    print(v1)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title=None, prompt='What do you think is awesome?')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if v1 == 0:
        print('that,s an awesome thing!')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if v1 == 1:
        print('eh, that,s an ok thing...')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if v1 == 2:
        print('not to be mean, but that,s kinda boring...')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if v1 == 3:
        print('it would be better if I didn,t say anything...')
    # Run the window's .mainloop() method
window.mainloop()