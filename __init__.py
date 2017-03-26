from tkinter import *
import tkinter.messagebox as mbox
from tkinter.font import Font
import  MainMaxAlgo
import ScoreManager

root = Tk()
root.title('Tic tac toe')
frame = Frame(root)
frame.pack(side=TOP)
frame1 = Frame (root)
frame1.pack(side=BOTTOM)
frame2 = Frame (root)
frame2.pack(side=BOTTOM)
frame3 = Frame (root)
frame3.pack(side=BOTTOM)





#----------------------------------------------------------------------------------------------------------------------
matrex = [[-1,-1,-1],
          [-1,-1,-1],
          [-1,-1,-1]]


# change the "lvl" value to make game difficulty .....
# increas a value to be hard
# decrease a value to be easy
lvl = 5




def checks(materx1,matrex2):
        l = 0
        for i in range(0,3):
                for j in range(0, 3):
                        l = l+1
                        if materx1[i][j] != matrex2[i][j]:
                                return l;



def drew_X(num):
        if num==1:
                bottom1.config(text="X")
                matrex[0][0]='x'
        if num==2:
                bottom2.config(text="X")
                matrex[0][1] = 'x'
        if num==3:
                bottom3.config(text="X")
                matrex[0][2] = 'x'
        if num==4:
                bottom4.config(text="X")
                matrex[1][0] = 'x'
        if num==5:
                bottom5.config(text="X")
                matrex[1][1] = 'x'
        if num==6:
                bottom6.config(text="X")
                matrex[1][2] = 'x'
        if num==7:
                bottom7.config(text="X")
                matrex[2][0] = 'x'
        if num==8:
                bottom8.config(text="X")
                matrex[2][1] = 'x'
        if num==9:
                bottom9.config(text="X")
                matrex[2][2] = 'x'
        pp()



def mat_is_combleat(materx):
        for i in range(0, 3):
                for j in range(0, 3):
                        if materx[i][j] ==-1 :
                                return 0;
        return 1



def reset():
        bottom1.config(text=".")
        bottom2.config(text=".")
        bottom3.config(text=".")
        bottom4.config(text=".")
        bottom5.config(text=".")
        bottom6.config(text=".")
        bottom7.config(text=".")
        bottom8.config(text=".")
        bottom9.config(text=".")
        dd()
        pp()



def  pp():
        print(matrex)
def dd():
        matrex.clear()
        matrex.append([-1,-1,-1])
        matrex.append([-1,-1,-1])
        matrex.append([-1,-1,-1])


def button9():
    text = bottom9["text"]
    if(text=="."):
            bottom9.config(text ="O")
            matrex[2][2]='o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex,lvl,'x')
                    num = checks(matrex,mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if(win == 'x'):
                         mbox.showinfo("", "YOU LOSE !!")
                         reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()


def button8():
    text = bottom8["text"]
    if(text=="."):
            bottom8.config(text ="O")
            matrex[2][1] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex,mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()


def button7():
    text = bottom7["text"]
    if(text=="."):
            bottom7.config(text ="O")
            matrex[2][0] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button6():
    text = bottom6["text"]
    if(text=="."):
            bottom6.config(text ="O")
            matrex[1][2] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button5():
    text = bottom5["text"]
    if(text=="."):
            bottom5.config(text ="O")
            matrex[1][1] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button4():
    text = bottom4["text"]
    if(text=="."):
            bottom4.config(text ="O")
            matrex[1][0] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button3():
    text = bottom3["text"]
    if(text=="."):
            bottom3.config(text ="O")
            matrex[0][2] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button2():
    text = bottom2["text"]
    if(text=="."):
            bottom2.config(text ="O")
            matrex[0][1] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()



def button1():
    text = bottom1["text"]
    if(text=="."):
            bottom1.config(text ="O")
            matrex[0][0] = 'o'
            win = ScoreManager.Check_Win(matrex)
            pp()
            if win == 'o':
                    mbox.showinfo("", "YOU WIN !!!")
                    reset()
            else:
                    mat = MainMaxAlgo.Min_max(matrex, lvl, 'x')
                    num = checks(matrex, mat.matrex)
                    drew_X(num)
                    win = ScoreManager.Check_Win(matrex)
                    if (win == 'x'):
                            mbox.showinfo("", "YOU LOSE !!")
                            reset()
                    else:
                        num=mat_is_combleat(matrex)
                        if num==1:
                                 mbox.showinfo("", "TIE")
                                 reset()





#----------------------------------------------------------------------------------------------------------------------


bottom7 = Button (frame1, text=".", relief=RAISED,width = 10,height =5 ,command = button7)
bottom7.pack(side=LEFT)
bottom8 = Button (frame1, text=".", relief=RAISED,width = 10,height =5,command =button8)
bottom8.pack(side=LEFT)
bottom9 = Button (frame1, text=".", relief=RAISED,width = 10,height =5,command =button9)
bottom9.pack(side=LEFT)
bottom4 = Button(frame2, text=".", relief=RAISED,width =10,height =5,command =button4)
bottom4.pack(side=LEFT)
bottom5 = Button (frame2, text=".", relief=RAISED,width = 10,height =5,command =button5)
bottom5.pack(side=LEFT)
bottom6 = Button (frame2, text=".", relief=RAISED,width =10,height =5,command =button6)
bottom6.pack(side=LEFT)
bottom1 = Button (frame3, text=".", relief=RAISED,width = 10,height =5,command =button1)
bottom1.pack(side=LEFT)
bottom2 = Button (frame3, text=".", relief=RAISED,width =10,height =5,command =button2)
bottom2.pack(side=LEFT)
bottom3 = Button (frame3, text=".", relief=RAISED,width = 10,height=5,command =button3)
bottom3.pack(side=LEFT)




restart = Button (frame,text="Restart",bg ="black",fg = "white",command=reset)
restart.pack()







root.mainloop()
