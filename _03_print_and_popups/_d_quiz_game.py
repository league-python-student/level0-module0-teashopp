from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
     
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question = simpledialog.askstring(title=None, prompt = 'Who was the killer in the original Friday the 13th move?')
    #      // 3.  Use an if statement to check if their answer is correct
    if question == 'Pamela Voorhees':
        print('correct; you would survive the first Scream movie')
    #      // 4.  if the user's answer was correct, add one to their score 
        score += 1
    else:
        print('incorrect; you would not survive the first Scream movie ')
        score -= 1
    print(score)
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question2 = simpledialog.askstring(title=None, prompt = 'What did Alfred Hitchcock use in place of blood in his movie Psycho?')
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    if question2 == 'chocolate syrup':
        print('correct')
        score += 1
    else:
        print('incorrect')
        score -= 1
    print(score)
    
    question3 = simpledialog.askstring(title=None, prompt = 'How many timelines are canon in the Halloween franchise?')
    if question3 == '3':
        print('correct, it gets confusing')
        score += 1
    elif question3 == '4':
        print('technically correct, but people debate over the third movie')
        score += 1
    else:
        print('incorrect')
        score -= 1
    print(score)
    # Run the window's .mainloop() method
    window.mainloop()