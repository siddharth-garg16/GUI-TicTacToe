from tkinter import *
import tkinter.messagebox as tmsg

def play():
    if(btn1['text']==btn2['text']==btn3['text']=='X'):
        btn1.configure(background='#CBC3E3')
        btn2.configure(background='#CBC3E3')
        btn3.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn4['text']==btn5['text']==btn6['text']=='X'):
        btn4.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn6.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn7['text']==btn8['text']==btn9['text']=='X'):
        btn7.configure(background='#CBC3E3')
        btn8.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn1['text']==btn4['text']==btn7['text']=='X'):
        btn1.configure(background='#CBC3E3')
        btn4.configure(background='#CBC3E3')
        btn7.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn2['text']==btn5['text']==btn8['text']=='X'):
        btn2.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn8.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn3['text']==btn6['text']==btn9['text']=='X'):
        btn3.configure(background='#CBC3E3')
        btn6.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn1['text']==btn5['text']==btn9['text']=='X'):
        btn1.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn3['text']==btn5['text']==btn7['text']=='X'):
        btn3.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn7.configure(background='#CBC3E3')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tmsg.showinfo('Winner X', 'Player X just won a game!')

    if(btn1['text']==btn2['text']==btn3['text']=='O'):
        btn1.configure(background='#CBC3E3')
        btn2.configure(background='#CBC3E3')
        btn3.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn4['text']==btn5['text']==btn6['text']=='O'):
        btn4.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn6.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn7['text']==btn8['text']==btn9['text']=='O'):
        btn7.configure(background='#CBC3E3')
        btn8.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn1['text']==btn4['text']==btn7['text']=='O'):
        btn1.configure(background='#CBC3E3')
        btn4.configure(background='#CBC3E3')
        btn7.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn2['text']==btn5['text']==btn8['text']=='O'):
        btn2.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn8.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn3['text']==btn6['text']==btn9['text']=='O'):
        btn3.configure(background='#CBC3E3')
        btn6.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn1['text']==btn5['text']==btn9['text']=='O'):
        btn1.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn9.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')

    if(btn3['text']==btn5['text']==btn7['text']=='O'):
        btn3.configure(background='#CBC3E3')
        btn5.configure(background='#CBC3E3')
        btn7.configure(background='#CBC3E3')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tmsg.showinfo('Winner O', 'Player O just won a game!')
    
 
def checker(valbutton):
    global click
    if valbutton["text"] == " " and click == True:
        valbutton["text"] = "X"
        click = False
    elif valbutton["text"] == " " and click == False:
        valbutton["text"] = "O"
        click = True
    play()

def resetGame():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "
    
    btn1.configure(background='gainsboro')
    btn2.configure(background='gainsboro')
    btn3.configure(background='gainsboro')
    btn4.configure(background='gainsboro')
    btn5.configure(background='gainsboro')
    btn6.configure(background='gainsboro')
    btn7.configure(background='gainsboro')
    btn8.configure(background='gainsboro')
    btn9.configure(background='gainsboro')
    

def newGame():
    resetGame()
    PlayerX.set(0)
    PlayerO.set(0)

if __name__ == "__main__":
    root = Tk()
    root.title("TicTacToe")
    root.geometry('1075x600')
    root.configure(background='#8A2BE2')

    Top = Frame(root, bg='#8A2BE2', pady=2, width=1350, height=100, relief=RIDGE)
    Top.grid(row=0, column=0)

    label_title = Label(Top, text="TIC TAC TOE", font=('segoe', 30, 'bold'), bd=21, bg='#8A2BE2', fg='#E6E6FA', justify=CENTER)
    label_title.grid(row=0, column=0)

    MainFrame = Frame(root, bg='#E6E6FA', pady=2, width=1350, height=600, relief=RIDGE)
    MainFrame.grid(row=1, column=0)

    LeftFrame = Frame(MainFrame, bd=10, padx=10, pady=2, bg='#8A2BE2', width=750, height=500, relief=RIDGE)
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(MainFrame, bd=10, padx=2, pady=10, bg='#8A2BE2', width=560, height=500, relief=RIDGE)
    RightFrame.pack(side=RIGHT)

    RightFrame1 = Frame(RightFrame, bd=10, padx=2, pady=10, bg='#8A2BE2', width=560, height=250, relief=RIDGE)
    RightFrame1.grid(row=0, column=0)

    RightFrame2 = Frame(RightFrame, bd=10, padx=2, pady=10, bg='#8A2BE2', width=560, height=250, relief=RIDGE)
    RightFrame2.grid(row=1, column=0)

    PlayerX=IntVar()
    PlayerO=IntVar()

    PlayerX.set(0)
    PlayerO.set(0)

    valbutton = StringVar()
    click = True

    lbl_playerX = Label(RightFrame1, text="Player X :", font=('segoe', 25, 'bold'), bd=21, bg='#8A2BE2', fg='#E6E6FA', justify=CENTER, padx=2, pady=2)
    lbl_playerX.grid(row=0, column=0, sticky=W)

    txt_playerX = Entry(RightFrame1, textvariable=PlayerX, bd=2, font=('segoe',24,'bold'), fg='black', justify=LEFT, width=14)
    txt_playerX.grid(row=0, column=1, padx=1)

    lbl_playerO = Label(RightFrame1, text="Player O :", font=('segoe', 24, 'bold'), bd=21, bg='#8A2BE2', fg='#E6E6FA', justify=CENTER, padx=2, pady=2)
    lbl_playerO.grid(row=1, column=0, sticky=W)

    txt_playerO = Entry(RightFrame1, textvariable=PlayerO, bd=2, font=('segoe',25,'bold'), fg='black', justify=LEFT, width=14)
    txt_playerO.grid(row=1, column=1, padx=1)

    ResetBtn = Button(RightFrame2, text="Reset", height=1, width=20, font=('times', 26, 'bold'), bg='gainsboro', relief=GROOVE, command=resetGame)
    ResetBtn.grid(row=0, column=0, padx=8, pady=11)

    newGameBtn = Button(RightFrame2, text="New Game", height=1, width=20, font=('times', 26, 'bold'), bg='gainsboro', relief=GROOVE, command = newGame)
    newGameBtn.grid(row=1, column=0, padx=8, pady=11)
    
    btn1 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn1))
    btn1.grid(row=0, column=0, sticky=S+N+E+W)

    btn2 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn2))
    btn2.grid(row=0, column=1, sticky=S+N+E+W)

    btn3 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn3))
    btn3.grid(row=0, column=2, sticky=S+N+E+W)

    btn4 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn4))
    btn4.grid(row=1, column=0, sticky=S+N+E+W)

    btn5 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn5))
    btn5.grid(row=1, column=1, sticky=S+N+E+W)

    btn6 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn6))
    btn6.grid(row=1, column=2, sticky=S+N+E+W)

    btn7 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn7))
    btn7.grid(row=2, column=0, sticky=S+N+E+W)

    btn8 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn8))
    btn8.grid(row=2, column=1, sticky=S+N+E+W)

    btn9 = Button(LeftFrame, text=" ", height=3, width=8, font=('times', 26, 'bold'), bg='gainsboro', command=lambda:checker(btn9))
    btn9.grid(row=2, column=2, sticky=S+N+E+W)

    root.mainloop()