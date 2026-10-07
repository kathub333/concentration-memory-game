import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import random as r
import mysql.connector as ms
con=ms.connect(host="localhost",user="root",password="your_password")
cur=con.cursor()


flag=0; selected1=''; selected2=''; turn=0; scoreP1=0; scoreP2=0; winner = ' '; pl1=''; pl2=''; set1Error=''; set2Error=''

#making window 1
window1=Tk()
window1.title('opening screen')
window1.geometry('800x500')
window1.configure(bg = 'light yellow')
wel_msg=tk.Label(window1, text = 'Memory Game !!', font = ('Calibri', 75, 'bold'), fg = '#f7be00', bg = 'light yellow').pack(pady = 75)

def open_window2():
    #making window 2
    window1.destroy()
    window2 = Tk()
    window2.title("player input")
    window2.geometry('750x500')
    window2.configure(bg = 'light blue')

    #to only allow alphabets
    def on_validate_input(P):
        if P == "" or P.isalpha():
            return True
        return False
    vcmd = window2.register(on_validate_input)
    
    playerLabel = Label(window2, text = 'ENTER PLAYER NAMES', font = ('Calibri', 50, 'bold'), fg = '#00537f', bg = 'light blue').place(x = 50, y = 50)
    p1entryLabel = Label(window2, text = 'player 1:', font = ('Calibri', 50), fg = 'black', bg = 'light blue').place(x = 50, y = 150)
    p1entry = tk.StringVar()
    p1=Entry(window2, font=('Calibri',20), textvariable = p1entry, validate='key', validatecommand=(vcmd, '%P')).place(x = 350, y = 170, height = 50, width = 300)
    p2entryLabel = Label(window2, text = 'player 2:', font = ('Calibri', 50), fg = 'black', bg = 'light blue').place(x = 50, y = 250)
    p2entry = tk.StringVar()
    p2=Entry(window2, font=('Calibri',20), textvariable = p2entry, validate='key', validatecommand=(vcmd, '%P')).place(x = 350, y = 270, height = 50, width = 300)

    #not null constraint
    def constraint():
        if(p1entry.get()=="" or p2entry.get()==""):
            constraint=Tk()
            constraint.title('Error')
            constraint.geometry('365x100')
            errorLabel=Label(constraint, text='Warning: names cannot be empty', font = ('Arial', 17), foreground='red').place(x = 10, y = 10)
            def tryAgainButtonClick():
                constraint.destroy()
            tryAgainButton = Button(constraint, text="Try Again", command=tryAgainButtonClick, foreground='black', background='light grey').place(x = 150, y = 55)
            constraint.mainloop()
        else:
            open_window3()

    def open_window3():
        global c
        #adding sr no and players to mysql table
        pl1=p1entry.get()
        pl2=p2entry.get()
        cur.execute("show databases")
        data=cur.fetchall()
        if(("card_game",) not in data):
            cur.execute("create  database card_game")
        cur.execute("use card_game")
        cur.execute("show tables")
        data=cur.fetchall()
        if(("memory",) not in data):       
            cur.execute("create  table memory(sr_no int, player1 varchar(20) , player2 varchar(20), winner varchar(20))")
        cur.execute("select sr_no from memory")
        data=cur.fetchall()
        c=len(data)+1 
        cur.execute("insert into memory(sr_no,player1,player2) values({},'{}','{}')".format(c,pl1,pl2))
        con.commit()

        #making window 3
        window2.destroy()
        window3=Tk()
        window3.title("memory game")
        window3.geometry('900x500')
        window3.configure(bg = 'white')

        #stuff in window 3 [leftside - cards]
        card_back=PhotoImage(file='back.png')
        l=['1','2','3','4','5','6','7','8','1','2','3','4','5','6','7','8']

        b1 = r.choice(l)
        l.remove(b1)
        c1=PhotoImage(file=b1+'.png')
        def click1():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b1
            if flag==2:
                selected2=b1
            if flag<=2:
                button1=Button(window3, image=c1).place(x = 10, y = 10, height =100, width = 100)
        button1=Button(window3, image=card_back, command = click1).place(x = 10, y = 10, height =100, width = 100)

        b2 = r.choice(l)
        l.remove(b2)
        c2=PhotoImage(file=b2+'.png')
        def click2():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b2
            if flag==2:
                selected2=b2
            if flag<=2:
                button2=Button(window3, image=c2).place(x = 135, y = 10, height =100, width = 100)
        button2=Button(window3, image=card_back, command = click2).place(x = 135, y = 10, height =100, width = 100)

        b3 = r.choice(l)
        l.remove(b3)
        c3=PhotoImage(file=b3+'.png')
        def click3():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b3
            if flag==2:
                selected2=b3
            if flag<=2:
                button3=Button(window3, image=c3).place(x = 260, y = 10, height =100, width = 100)
        button3=Button(window3, image=card_back, command = click3).place(x = 260, y = 10, height =100, width = 100)

        b4 = r.choice(l)
        l.remove(b4)
        c4=PhotoImage(file=b4+'.png')
        def click4():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b4
            if flag==2:
                selected2=b4
            if flag<=2:
                button4=Button(window3, image=c4).place(x = 385, y = 10, height =100, width = 100)
        button4=Button(window3, image=card_back, command = click4).place(x = 385, y = 10, height =100, width = 100)

        b5 = r.choice(l)
        l.remove(b5)
        c5=PhotoImage(file=b5+'.png')
        def click5():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b5
            if flag==2:
                selected2=b5
            if flag<=2:
                button5=Button(window3, image=c5).place(x = 10, y = 135, height =100, width = 100)
        button5=Button(window3, image=card_back, command = click5).place(x = 10, y = 135, height =100, width = 100)

        b6 = r.choice(l)
        l.remove(b6)
        c6=PhotoImage(file=b6+'.png')
        def click6():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b6
            if flag==2:
                selected2=b6
            if flag<=2:
                button6=Button(window3, image=c6).place(x = 135, y = 135, height =100, width = 100)
        button6=Button(window3, image=card_back, command = click6).place(x = 135, y = 135, height =100, width = 100)

        b7 = r.choice(l)
        l.remove(b7)
        c7=PhotoImage(file=b7+'.png')
        def click7():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b7
            if flag==2:
                selected2=b7
            if flag<=2:
                button7=Button(window3, image=c7).place(x = 260, y = 135, height =100, width = 100)
        button7=Button(window3, image=card_back, command = click7).place(x = 260, y = 135, height =100, width = 100)

        b8 = r.choice(l)
        l.remove(b8)
        c8=PhotoImage(file=b8+'.png')
        def click8():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b8
            if flag==2:
                selected2=b8
            if flag<=2:
                button8=Button(window3, image=c8).place(x = 385, y = 135, height =100, width = 100)
        button8=Button(window3, image=card_back, command = click8).place(x = 385, y = 135, height =100, width = 100)

        b9 = r.choice(l)
        l.remove(b9)
        c9=PhotoImage(file=b9+'.png')
        def click9():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b9
            if flag==2:
                selected2=b9
            if flag<=2:
                button9=Button(window3, image=c9).place(x = 10, y = 260, height =100, width = 100)
        button9=Button(window3, image=card_back, command = click9).place(x = 10, y = 260, height =100, width = 100)

        b10 = r.choice(l)
        l.remove(b10)
        c10=PhotoImage(file=b10+'.png')
        def click10():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b10
            if flag==2:
                selected2=b10
            if flag<=2:
                button10=Button(window3, image=c10).place(x = 135, y = 260, height =100, width = 100)
        button10=Button(window3, image=card_back, command = click10).place(x = 135, y = 260, height =100, width = 100)

        b11 = r.choice(l)
        l.remove(b11)
        c11=PhotoImage(file=b11+'.png')
        def click11():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b11
            if flag==2:
                selected2=b11
            if flag<=2:
                button11=Button(window3, image=c11).place(x = 260, y = 260, height =100, width = 100)
        button11=Button(window3, image=card_back, command = click11).place(x = 260, y = 260, height =100, width = 100)

        b12 = r.choice(l)
        l.remove(b12)
        c12=PhotoImage(file=b12+'.png')
        def click12():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b12
            if flag==2:
                selected2=b12
            if flag<=2:
                button12=Button(window3, image=c12).place(x = 385, y = 260, height =100, width = 100)
        button12=Button(window3, image=card_back, command = click12).place(x = 385, y = 260, height =100, width = 100)

        b13 = r.choice(l)
        l.remove(b13)
        c13=PhotoImage(file=b13+'.png')
        def click13():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b13
            if flag==2:
                selected2=b13
            if flag<=2:
                button13=Button(window3, image=c13).place(x = 10, y = 385, height =100, width = 100)
        button13=Button(window3, image=card_back, command = click13).place(x = 10, y = 385, height =100, width = 100)

        b14 = r.choice(l)
        l.remove(b14)
        c14=PhotoImage(file=b14+'.png')
        def click14():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b14
            if flag==2:
                selected2=b14
            if flag<=2:
                button14=Button(window3, image=c14).place(x = 135, y = 385, height =100, width = 100)
        button14=Button(window3, image=card_back, command = click14).place(x = 135, y = 385, height =100, width = 100)

        b15 = r.choice(l)
        l.remove(b15)
        c15=PhotoImage(file=b15+'.png')
        def click15():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b15
            if flag==2:
                selected2=b15
            if flag<=2:
                button15=Button(window3, image=c15).place(x = 260, y = 385, height =100, width = 100)
        button15=Button(window3, image=card_back, command = click15).place(x = 260, y = 385, height =100, width = 100)

        b16 = r.choice(l)
        l.remove(b16)
        c16=PhotoImage(file=b16+'.png')
        def click16():
            global flag, selected1, selected2
            flag+=1
            if flag==1:
                selected1=b16
            if flag==2:
                selected2=b16
            if flag<=2:
                button16=Button(window3, image=c16).place(x = 385, y = 385, height =100, width = 100)
        button16=Button(window3, image=card_back, command = click16).place(x = 385, y = 385, height =100, width = 100)
        
        #cheatcode for game
        print(b1,b2,b3,b4)
        print(b5,b6,b7,b8)
        print(b9,b10,b11,b12)
        print(b13,b14,b15,b16)

        #stuff in window 3 [rightside - widgits]
        global turn, scoreP1, scoreP2
        players = Label(window3, text = 'PLAYERS', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white').place(x = 550, y = 20)
        scores = Label(window3, text = 'SCORES', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white').place(x = 715, y = 20)
        turns = Label(window3, text = 'TURN: ', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white').place(x = 550, y = 200)
        P1Label = Label(window3, text = pl1, font = ('Calibri', 15, 'bold'), fg = 'red', bg = 'white').place(x = 550, y = 75)
        P2Label = Label(window3, text = pl2, font = ('Calibri', 15, 'bold'), fg = 'green', bg = 'white').place(x = 550, y = 125)
        S1Label = Label(window3, text = scoreP1, font = ('Calibri', 15), fg = 'black', bg = 'white').place(x = 750, y = 75)
        S2Label =Label(window3, text = scoreP2, font = ('Calibri', 15), fg = 'black', bg = 'white').place(x = 750, y = 125)
        turn=1
        turnLabel = Label(window3, text = pl1+"'s turn", font = ('Calibri', 20, 'bold'), fg = 'red', bg = 'white').place(x = 650, y = 200)

        def nextButtonClick():
            global flag, selected1, selected2, turn, scoreP1, scoreP2, c
            #if match is made correclty
            if flag>=2 and selected1!='' and selected1==selected2:
                if turn%2==0:
                     scoreP2+=1
                     Label(window3, text = scoreP2, font = ('Calibri', 15, ), fg = 'black', bg = 'white').place(x = 750, y = 125)
                else:
                    scoreP1+=1
                    Label(window3, text = scoreP1, font = ('Calibri', 15, ), fg = 'black', bg = 'white').place(x = 750, y = 75)
                flag=0; selected1=''; selected2=''

            #if match is made incorreclty
            if flag>=2 and selected1!='' and selected1!=selected2:
                turn+=1
                if turn%2==0:
                    turnLabel = Label(window3, text = pl1+"'s turn", font = ('Calibri', 20, 'bold'), fg = 'white', bg = 'white').place(x = 650, y = 200)
                    turnLabel = Label(window3, text = pl2+"'s turn", font = ('Calibri', 20, 'bold'), fg = 'green', bg = 'white').place(x = 650, y = 200)
                else:
                    turnLabel = Label(window3, text = pl2+"'s turn", font = ('Calibri', 20, 'bold'), fg = 'white', bg = 'white').place(x = 650, y = 200)
                    turnLabel = Label(window3, text = pl1+"'s turn", font = ('Calibri', 20, 'bold'), fg = 'red', bg = 'white').place(x = 650, y = 200)
                    
                if selected1 == b1 or selected2 == b1:
                    button1=Button(window3, image=card_back, command = click1).place(x = 10, y = 10, height =100, width = 100)
                if selected1 == b2 or selected2 == b2:
                    button2=Button(window3, image=card_back, command = click2).place(x = 135, y = 10, height =100, width = 100)
                if selected1 == b3 or selected2 == b3:
                    button3=Button(window3, image=card_back, command = click3).place(x = 260, y = 10, height =100, width = 100)
                if selected1 == b4 or selected2 == b4:
                    button4=Button(window3, image=card_back, command = click4).place(x = 385, y = 10, height =100, width = 100)
                if selected1 == b5 or selected2 == b5:
                    button5=Button(window3, image=card_back, command = click5).place(x = 10, y = 135, height =100, width = 100)
                if selected1 == b6 or selected2 == b6:
                    button6=Button(window3, image=card_back, command = click6).place(x = 135, y = 135, height =100, width = 100)
                if selected1 == b7 or selected2 == b7:
                    button7=Button(window3, image=card_back, command = click7).place(x = 260, y = 135, height =100, width = 100)
                if selected1 == b8 or selected2 == b8:
                    button8=Button(window3, image=card_back, command = click8).place(x = 385, y = 135, height =100, width = 100)
                if selected1 == b9 or selected2 == b9:
                    button9=Button(window3, image=card_back, command = click9).place(x = 10, y = 260, height =100, width = 100)
                if selected1 == b10 or selected2 == b10:
                    button10=Button(window3, image=card_back, command = click10).place(x = 135, y = 260, height =100, width = 100)
                if selected1 == b11 or selected2 == b11:
                    button11=Button(window3, image=card_back, command = click11).place(x = 260, y = 260, height =100, width = 100)
                if selected1 == b12 or selected2 == b12:
                    button12=Button(window3, image=card_back, command = click12).place(x = 385, y = 260, height =100, width = 100)
                if selected1 == b13 or selected2 == b13:
                    button13=Button(window3, image=card_back, command = click13).place(x = 10, y = 385, height =100, width = 100)
                if selected1 == b14 or selected2 == b14:
                    button14=Button(window3, image=card_back, command = click14).place(x = 135, y = 385, height =100, width = 100)
                if selected1 == b15 or selected2 == b15:
                    button15=Button(window3, image=card_back, command = click15).place(x = 260, y = 385, height =100, width = 100)
                if selected1 == b16 or selected2 == b16:
                    button16=Button(window3, image=card_back, command = click16).place(x = 385, y = 385, height =100, width = 100)
                flag=0; selected1=''; selected2=''

            #when all matches are made
            if scoreP1+scoreP2==8:
                if scoreP1>scoreP2:
                    winnerLabel = Label(window3, text="WINNER IS "+pl1.upper(), font=('Calibri', 25 , 'bold'), fg='gold', bg='white').place(x=550, y=320)
                    cur.execute("update memory set winner ='{}' where sr_no={}".format(pl1,c)) 
                elif scoreP2>scoreP1:
                    winnerLabel = Label(window3, text="WINNER IS "+pl2.upper(), font=('Calibri', 25 , 'bold'), fg='gold', bg='white').place(x=550, y=320)
                    cur.execute("update memory set winner ='{}' where sr_no={}".format(pl2,c)) 
                else:
                    winnerLabel = Label(window3, text="THIS GAME IS A DRAW", font=('Calibri', 25 , 'bold'), fg='black', bg='white').place(x=500, y=320)
                    cur.execute("update memory set winner ='{}' where sr_no={}".format('tie',c)) 
                con.commit()

                def open_window4():
                    #making window 4
                    window3.destroy()
                    window4=Tk()
                    window4.title('post game screen')
                    window4.geometry('400x200')
                    window4.configure(bg = '#ffc1c1')

                    def leaderboard():
                        window4.destroy()
                        lb=Tk()
                        lb.title('leaderboard')
                        lb.configure(bg = 'light green')
                        cur.execute("select winner from memory")
                        winner_all=cur.fetchall()
                        cur.execute("select distinct winner from memory where winner is not null")
                        winner_distinct=cur.fetchall()
                        ht=len(winner_distinct)
                        lb.geometry('580x'+str(240+(ht*50)))

                        l=[]
                        for i in winner_distinct:
                            l.append([i,winner_all.count(i)])

                        for i in range(0,len(l)-1):
                            for j in range(0,len(l)-1):
                                if(l[j][1]<l[j+1][1]):
                                    l[j],l[j+1]=l[j+1],l[j]
                        lbLabel = Label(lb,text="LEADERBOARD", font = ('Calibri', 50, 'bold'), fg = '#1d5e2f', bg = 'light green').place(x = 70, y = 10)
                        winnerLabel = Label(lb,text="WINNER NAME", font = ('Calibri', 20, 'bold'), fg = 'white', bg = 'light green').place(x = 60, y = 100)
                        winsLabel = Label(lb,text="NUMBER OF WINS", font = ('Calibri', 20, 'bold'), fg = 'white', bg = 'light green').place(x = 300, y = 100)
                        y1 = 150
                        for i in range(0,len(l)):
                            if (l[i][0][0]) == 'tie':
                                continue
                            winnerNameLabel = Label(lb,text=l[i][0][0], font = ('Calibri', 15), fg = 'black', bg = 'light green').place(x = 80, y = y1)
                            winsCountLabel = Label(lb,text=l[i][1], font = ('Calibri', 15), fg = 'black', bg = 'light green').place(x = 400, y = y1)
                            y1+=40
                        def doneButtonClick():
                            lb.destroy()
                        doneButton = Button(lb, text='DONE', font= ('Calibri', 20, 'bold'), bg = '#1d5e2f', fg = 'white',  command=doneButtonClick).place(x=225, y=y1+20, height = 50, width= 100)
                        
                    lbButton = Button(window4, text='LEADER BOARD', font= ('Calibri', 20, 'bold'), bg = '#ce402a', fg = 'white',  command=leaderboard).place(x=100, y=30, height = 50, width= 200)

                    def endButtonClick():
                        window4.destroy()
                    endButton = Button(window4, text='END', font= ('Calibri', 20, 'bold'), bg = '#ce402a', fg = 'white',  command=endButtonClick).place(x=100, y=110, height = 50, width= 200)
                
                finishButton = Button(window3, text = 'FINISH', font= ('Calibri', 20, 'bold'), bg = '#e0d8c3', fg = 'black', command=open_window4).place(x = 640, y = 400,  height = 40)
    
        nextButton = Button(window3, text = 'NEXT', font= ('Calibri', 20, 'bold'), bg = '#e0d8c3', fg = 'black', command=nextButtonClick).place(x = 640, y = 320,  height = 40)
        window3.mainloop()
    playButton = Button(window2, text='PLAY', font= ('Calibri', 30, 'bold'), bg = '#00537f', fg = 'white',  command=constraint).place(x = 320, y = 375,  height = 60)
    window2.mainloop()  
startButton = Button(window1, text='START', font= ('Calibri', 30, 'bold'), bg = '#f7be00', fg = 'white',  command = open_window2).place(x = 325, y = 300, height = 60)
window1.mainloop()
