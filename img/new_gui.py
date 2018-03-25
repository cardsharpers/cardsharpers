#==============================================================================================================
#inport section
from time import sleep
import tkinter as tk
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
from popup import *
import PIL.Image, PIL.ImageTk
import shuffleDeck
from time import sleep
#======================================================================================================================
def vp_start_gui():
    #starting gui++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    root = Tk()


    font10 = "-family {Noto Sans} -size 19 -weight bold " \
             "-slant italic -underline 1 -overstrike 0"
    font9 = "-family {Noto Sans} -size 14 -weight normal " \
            "-slant italic -underline 0 -overstrike 0"

    root.geometry("1351x714+-10+-8")
    root.title("New rootlevel 1")
    root.resizable(0, 0)
    root.configure(background="#070")
    root.configure(highlightcolor="black")
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




#======================================================================================================================
#                               FUNCTION DEFINITIONS
#======================================================================================================================
    potlabel = [""] * 6
    potimg = [""] * 6
    p=[]
    def showPotCards(selectedCard):
        p.append(selectedCard)
        psize=len(p)
        path = "resources/cards/" + p[psize-1] + ".png"
        potimg[i] = PIL.Image.open(path)
        potimg[i] = potimg[i].resize((50, 70))
        potimg[i] = PIL.ImageTk.PhotoImage(potimg[i])
        potlabel[i]=ttk.Label(Frame16)
        potlabel[i].config(image=potimg[i])
        potlabel[i].configure(relief=FLAT,background="#d9d9d9")
        potlabel[i].pack(fill="both")
        if(i==0):
            potlabel[i].place(relx=0.1, rely=0.16, height=80, width=54)
        elif(i==1):
            potlabel[i].place(relx=0.38, rely=0.08, height=80, width=54)
        elif (i == 2):
            potlabel[i].place(relx=0.73, rely=0.16, height=80, width=54)
        elif (i == 3):
            potlabel[i].place(relx=0.67, rely=0.54, height=80, width=54)
        elif (i == 4):
            potlabel[i].place(relx=0.41, rely=0.69, height=80, width=54)
        elif (i == 5):
            potlabel[i].place(relx=0.1, rely=0.57, height=80, width=54)

    def throwToPot(thrownCard, potLabelIndicator, potCards):
        for i in range(6):
            if (potLabelIndicator[i] == 0):
                potCards.append(thrownCard)
                showPotCards(thrownCard, potlabel[i])
                break
        # =========================fUNCTION TO SHOW CARD OF PLAYER====================

    panel = [""] * 12
    img = [""] * 12
    c = [""] * 12

    def showPlayerCards(playerCards, startxxoord):
        c[i] = playerCards
        path = "resources/cards/" + c[i] + ".png"
        img[i] = PIL.Image.open(path)
        img[i] = img[i].resize((62, 85))
        img[i] = PIL.ImageTk.PhotoImage(img[i])
        panel[i] = tk.Label(root, image=img[i], fg="#070")
        panel[i].configure(relief=FLAT)
        panel[i].pack(fill="both")
        panel[i].place(relx=startxxoord, rely=0.76, relheight=0.12, relwidth=0.05)

    button = [""] * 12
    buttonRelX = 0.15
    def createButtons():
        for i in range(12):
            button[i] = Button(root)
            button[i].place(relx=buttonRelX + (i * 0.06), rely=0.9, height=30, width=64)
            button[i].configure(activebackground="#d9d9d9")
            button[i].configure(text='''Select''')
            button[i]["command"] = lambda: optionWindow(c[i], shuffleDeck.potCards, button[i], panel[i])


        # ================================================================================
        #                       function to delete card of player
        # =================================================================================
    def delPlayerCard(button, label):
        button.destroy()
        label.destroy()
    def delPotCard(label):
        label.destroy()



    # =============================================================================================
    #function to call bid value
    def bidCard(botCards):
        string = "there\'s no card with value greater that 9 , Restrating game "
        bid = 9
        for i in range(4):
            if int(str(botCards[i][1:])) >= 9:
                if botCards[i][:1] != 's':
                    bid = botCards[i][1:]
                else:
                    bid = botCards[i][1:]
            else:
                if 1==3:
                    lambda:showError(string)
        return str(bid)

    #=========================function to throw card=============================
    def throw(selectedCard, potCards, button, panel):
        flag = 5
        yourcard=int(str(selectedCard[1:]))
        for i in range(len(potCards)):
            if (selectedCard == potCards[i]):
                flag = 1
                break
            else:
                for i in range(len(potCards) - 1):
                    j = i + 1
                    sum = 0
                    while (j < (len(potCards))):
                        sum = int(str(potCards[i][1:])) + int(str(potCards[j][1:]))
                        if (sum < yourcard):
                            if (j + 1 < len(potCards)):
                                sum = sum + int(str(potCards[j + 1][1:]))
                                if (sum < yourcard):
                                    if (j + 2 < len(potCards)):
                                        sum = sum + int(str(potCards[j + 2][1:]))
                                    elif (sum == yourcard):
                                        flag = 4
                                        break
                                elif (sum == yourcard   ):
                                    flag = 3
                                    break
                            elif (sum == yourcard):
                                flag = 2
                                break
                        if (flag <= 4):
                            break

            if (flag <= 4):
                # call pick funtion
                pickCards()
            else:
                delPlayerCards(button, panel)
                throwToPot(selectedCard, potLabelIndicator, potCards)

    def pickCards(selelctedCard, potCards, potlabel, pimg, potLabelIndicator,botPlayer):#for bots first move botPlayer =0 else 1
        print("this is pick function")
        print(potCards)
        print(potLabelIndicator)
        if(botPlayer==0):
            cardVal=int(selelctedCard)
        else:
            cardVal=int(str(selelctedCard[1:]))
        for i in range(len(potCards)):
            if (potLabelIndicator[i] == 1):
                print("upr")
                if ((int(str(potCards[i][1:])))== cardVal):
                    #points(potCards[i], selectedCard)
                    print("aa gya")
                    for n in range(len(pimg)):
                        if(potCards[i] == pimg[n]):
                            del(pimg[n])
                            del(potCards[i])
                            delPotCard(potlabel[n])#this is not working
                            potLabelIndicator[n] = 0

                            print(pimg)
                            return potLabelIndicator, pimg






    house1=[]
    def buildBiddedHouse(bid, potCards, botCards,potlabel,pimg,potLabelIndicator):
        print(potCards)
        print(bid)
        flag=3
        for k in range(4):
            if int(str(potCards[k][1:])) == int(bid):
                pickCards(bid,potCards,potlabel,pimg,potLabelIndicator,0)
                break
            else:
                for i in range(4):
                    for j in range(4):
                        print(i , j)
                        if(int(str(potCards[i][1:])) + int(str(botCards[j][1:]))==int(bid)):
                            print("true")
                            for  n in range(len(pimg)):
                                if(botCards[i]==pimg[n]):
                                    delPotCard(potCards[n])
                                    potLabelIndicator[n]=0
                                    del(pimg[n])
                                    return potLabelIndicator
                                    return potlabel
                            house1.append(potCards[i])
                            house1.append(botCards[j])
                            del (botCards[j])
                            del (potCards[i])
                            print()
                            flag=1
                            break
                    if flag==1:
                        break
            if flag==1:
                break;
            for k in range(4):
                if int(botCards[k][1:]) == bid:
                    print("new false")
                    throwToPot(botCards[k],potLabelIndicator)
                    showPotCards(botCards[k],potlabel[4])
                    potLabelIndicator[4]=1
                    del (botCards[k])


    def optionWindow(selectedCard, potCards, button, panel):
        toplevel = Toplevel()
        toplevel.title("YOUR CHOICE")
        toplevel.geometry("300x300")
        button11 = Button(toplevel, text="THROW", height=3, width=10)
        button11.pack(expand=YES, fill=X)
        button11["command"] = lambda: throw(selectedCard, potCards, button, panel)
        button22 = Button(toplevel, text="PICK", height=3, width=10)
        button22.pack(expand=YES, fill=X)

        button33 = Button(toplevel, text="BUILD", height=3, width=10)
        button33.pack(expand=YES, fill=X)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ================================INITIALIZATION -----------------------------------------------
    #distribute cards phase 1
    # shuffleDeck.distribute cards
    shuffleDeck.distribute(4, 2)  # cards for pot
    shuffleDeck.distribute(12, 0)  # cards for bot
    shuffleDeck.distribute(12, 1)  # cards for players
    print(shuffleDeck.potCards)
    print(shuffleDeck.botCards)
    CalledBidCard = bidCard(shuffleDeck.botCards)
    createButtons()
    for i in range(12):
        showPlayerCards(shuffleDeck.playerCards[i], startxxoord=0.15 + i * 0.06)
    ##======================================================================================================================
    #                                   show 4 pot cards initialization
    #======================================================================================================================
    # ============================================================================
    # Special case to show potCards
    Canvas2 = Canvas(root)
    Canvas2.place(relx=0.22, rely=0.24, relheight=0.48, relwidth=0.58)
    Canvas2.configure(background="#d9ffd9")
    Canvas2.configure(borderwidth="2")
    Canvas2.configure(relief=RIDGE)
    Canvas2.configure(selectbackground="#c4c4c4")
    Canvas2.configure(width=781)

    Frame16 = Frame(Canvas2)
    Frame16.place(relx=0.29, rely=0.12, relheight=0.78, relwidth=0.4)
    Frame16.configure(relief=FLAT)
    Frame16.configure(borderwidth="2")
    Frame16.configure(relief=FLAT)
    Frame16.configure(width=315)



    print(shuffleDeck.potCards)
    potSize=len(shuffleDeck.potCards)
        # ======================
    for i in range(potSize):
        showPotCards(shuffleDeck.potCards[i])
        shuffleDeck.potLabelIndicator[i] = 1
    buildBiddedHouse(CalledBidCard, shuffleDeck.potCards, shuffleDeck.botCards, potlabel, p,
                     shuffleDeck.potLabelIndicator)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                              flames pots etc
    # ==============================================================


    Frame14 = Frame(Canvas2)
    Frame14.place(relx=0.06, rely=0.29, relheight=0.54, relwidth=0.22)
    Frame14.configure(relief=FLAT)
    Frame14.configure(borderwidth="2")
    Frame14.configure(relief=FLAT)
    Frame14.configure(width=175)

    Frame15 = Frame(Canvas2)
    Frame15.place(relx=0.7, rely=0.29, relheight=0.54, relwidth=0.22)
    Frame15.configure(relief=FLAT)
    Frame15.configure(borderwidth="2")
    Frame15.configure(relief=FLAT)
    Frame15.configure(width=175)

    Message1 = Message(Canvas2)
    Message1.place(relx=0.12, rely=0.85, relheight=0.11, relwidth=0.11)
    Message1.configure(text='''House1''')
    Message1.configure(width=87)

    Message2 = Message(Canvas2)
    Message2.place(relx=0.78, rely=0.85, relheight=0.08, relwidth=0.1)
    Message2.configure(text='''House2''')
    Message2.configure(width=77)



    Label1 = Label(root)
    Label1.place(relx=0.25, rely=0.28, height=42, width=155)
    Label1.configure(activebackground="#f9f9f9")
    Label1.configure(background="#fffdd9")
    Label1.configure(text='''House 1''')

    Label2 = Label(root)
    Label2.place(relx=0.65, rely=0.29, height=42, width=155)
    Label2.configure(activebackground="#f9f9f9")
    Label2.configure(activeforeground="#0000a8")
    Label2.configure(background="#fffdd9")
    Label2.configure(text='''House 2''')

    Labelbid = Label(root)
    Labelbid.place(relx=0.85, rely=0.29, height=42, width=155)
    Labelbid.configure(activebackground="#f9f9f9")
    Labelbid.configure(activeforeground="#0000a8")
    Labelbid.configure(background="#fffdd9")
    Msg1 = "Bidded Card is : " + CalledBidCard
    Labelbid.configure(text=Msg1)
    # ++================================================================

    Message3 = Message(root)
    Message3.place(relx=0.37, rely=0.03, relheight=0.09, relwidth=0.29)
    Message3.configure(background="#750")
    Message3.configure(font=font10)
    Message3.configure(foreground="#00007b")
    Message3.configure(highlightbackground="#d91b14")
    Message3.configure(highlightcolor="#000081")
    Message3.configure(relief=RAISED)
    Message3.configure(takefocus="1")
    Message3.configure(text='''SEEP - THE CARD GAME''')
    Message3.configure(width=397)
    # button for rules!!!

    Button16 = Button(root)
    Button16.place(relx=0.88, rely=0.03, height=60, width=130)
    Button16.configure(activebackground="#d9d9d9")
    Button16.configure(background="#ff0000")
    Button16.configure(font=font9)
    Button16.configure(foreground="#0c0000")
    Button16.configure(highlightcolor="#ff0000")
    Button16.configure(takefocus="0")
    Button16.configure(text='''READ RULES''')
    Button16["command"] = rules

    Message4 = Message(root)
    Message4.place(relx=0.01, rely=0.37, relheight=0.23, relwidth=0.17)
    Message4.configure(text='''turn = PLayer/computer''')
    Message4.configure(width=227)

    Button14 = Button(root)
    Button14.place(relx=0.88, rely=0.83, height=60, width=122)
    Button14.configure(activebackground="#d9d9d9")
    Button14.configure(background="#567")
    Button14.configure(foreground="#030")
    Button14.configure(takefocus="0")
    Button14.configure(text='''RESTART GAME''')

    Button15 = Button(root)
    Button15.place(relx=0.88, rely=0.74, height=60, width=122)
    Button15.configure(activebackground="#d9d9d9")
    Button15.configure(background="#ff0000")
    Button15.configure(font=font9)
    Button15.configure(foreground="#0c0000")
    Button15.configure(highlightcolor="#ff0000")
    Button15.configure(takefocus="0")
    Button15.configure(text='''EXIT''')
    Button15["command"] = exitOption

    # ======================================================

    # Lables for cards in Houses

    TLabel1 = ttk.Label(Frame14)
    TLabel1.place(relx=0.06, rely=0.11, height=80, width=54)
    TLabel1.configure(background="#d9d9d9")
    TLabel1.configure(foreground="#000000")
    TLabel1.configure(relief=FLAT)
    TLabel1.configure(width=54)

    TLabel2 = ttk.Label(Frame14)
    TLabel2.place(relx=0.23, rely=0.23, height=80, width=54)
    TLabel2.configure(background="#d9d9d9")
    TLabel2.configure(foreground="#000000")
    TLabel2.configure(relief=FLAT)

    TLabel3 = ttk.Label(Frame14)
    TLabel3.place(relx=0.4, rely=0.34, height=80, width=54)
    TLabel3.configure(background="#d9d9d9")
    TLabel3.configure(foreground="#000000")
    TLabel3.configure(relief=FLAT)

    TLabel4 = ttk.Label(Frame14)
    TLabel4.place(relx=0.57, rely=0.44, height=80, width=54)
    TLabel4.configure(background="#d9d9d9")
    TLabel4.configure(foreground="#000000")
    TLabel4.configure(relief=FLAT)

    TLabel6 = ttk.Label(Frame15)
    TLabel6.place(relx=0.23, rely=0.28, height=80, width=54)
    TLabel6.configure(background="#d9d9d9")
    TLabel6.configure(foreground="#000000")
    TLabel6.configure(relief=FLAT)

    TLabel7 = ttk.Label(Frame15)
    TLabel7.place(relx=0.4, rely=0.39, height=80, width=54)
    TLabel7.configure(background="#d9d9d9")
    TLabel7.configure(foreground="#000000")
    TLabel7.configure(relief=FLAT)

    TLabel8 = ttk.Label(Frame15)
    TLabel8.place(relx=0.57, rely=0.5, height=80, width=54)
    TLabel8.configure(background="#d9d9d9")
    TLabel8.configure(foreground="#000000")
    TLabel8.configure(relief=FLAT)  # backgroundImg.place(x=0, y=0, relwidth=1, relheight=1)

    root.mainloop()


#======================================================================================================================
#======================================================================================================================#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#==============================================STARTING MAIN PROGRAM ========================================================================#======================================================================================================================
if __name__ == '__main__':
    vp_start_gui()






