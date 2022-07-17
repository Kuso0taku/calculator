from tkinter import *

class App:
    def __init__(self):
        self.w = Tk()
        w = self.w

        self.ent = Entry(w, width=9, font='Arial 35', fg='green', bg='black', justify=RIGHT)

        self.btnC = Button(w, width=3, text='C', font='arial 20', fg='yellow', bg='black', command=self.clickC)
        self.btnBS = Button(w, width=3, text='←', font='arial 20', fg='yellow', bg='black', command=self.clickBS)
        self.btnPlus = Button(w, width=3, text='+', font='arial 20', fg='purple', bg='black', command=self.clickPlus)
        self.btnMinus = Button(w, width=3, text='-', font='arial 20', fg='purple', bg='black', command=self.clickMinus)

        self.btnSeven = Button(w, width=3, text='7', font='arial 20', fg='purple', bg='black', command=self.clickSeven)
        self.btnEight = Button(w, width=3, text='8', font='arial 20', fg='purple', bg='black', command=self.clickEight)
        self.btnNine = Button(w, width=3, text='9', font='arial 20', fg='purple', bg='black', command=self.clickNine)
        self.btnDivide = Button(w, width=3, text='÷', font='arial 20', fg='purple', bg='black', command=self.clickDivide)

        self.btnFour = Button(w, width=3, text='4', font='arial 20', fg='purple', bg='black', command=self.clickFour)
        self.btnFive = Button(w, width=3, text='5', font='arial 20', fg='purple', bg='black', command=self.clickFive)
        self.btnSix = Button(w, width=3, text='6', font='arial 20', fg='purple', bg='black', command=self.clickSix)
        self.btnMultiply = Button(w, width=3, text='×', font='arial 20', fg='purple', bg='black', command=self.clickMultiply)

        self.btnOne = Button(w, width=3, text='1', font='arial 20', fg='purple', bg='black', command=self.clickOne)
        self.btnTwo = Button(w, width=3, text='2', font='arial 20', fg='purple', bg='black', command=self.clickTwo)
        self.btnThree = Button(w, width=3, text='3', font='arial 20', fg='purple', bg='black', command=self.clickThree)

        self.btnZero = Button(w, width=7, text='0', font='arial 20', fg='purple', bg='black', command=self.clickZero)
        self.btnDot = Button(w, width=3, text='.', font='arial 20', fg='purple', bg='black', command=self.clickDot)
        self.btnEq = Button(w, height=3, width=3, text='=', font='arial 20', fg='red', bg='black', command=self.clickEq)

    def window(self):
        w = self.w

        w['bg'] = 'black'
        w.title('Calculator')
        w.geometry('232x336')
        w.resizable(False, False)
        w.bind('<Key>', self.board)
        w.mainloop()

    def place(self):
        self.ent.place(relx=0, rely=0)
        self.btnC.place(relx=0, rely=0.1675)
        self.btnBS.place(relx=0.25, rely=0.1675)
        self.btnPlus.place(relx=0.5, rely=0.1675)
        self.btnMinus.place(relx=0.75, rely=0.1675)

        self.btnSeven.place(relx=0, rely=0.3325)
        self.btnEight.place(relx=0.25, rely=0.3325)
        self.btnNine.place(relx=0.5, rely=0.3325)
        self.btnDivide.place(relx=0.75, rely=0.3325)

        self.btnFour.place(relx=0, rely=0.5)
        self.btnFive.place(relx=0.25, rely=0.5)
        self.btnSix.place(relx=0.5, rely=0.5)
        self.btnMultiply.place(relx=0.75, rely=0.5)

        self.btnOne.place(relx=0, rely=0.6675)
        self.btnTwo.place(relx=0.25, rely=0.6675)
        self.btnThree.place(relx=0.5, rely=0.6675)
        self.btnEq.place(relx=0.75, rely=0.6675)

        self.btnZero.place(relx=0, rely=0.8325)
        self.btnDot.place(relx=0.5, rely=0.8325)

    def clickC(self):
        self.ent.delete(0, 'end')

    def clickBS(self):
        y = self.ent.get()
        self.ent.delete(len(y) - 1, 'end')

    def clickPlus(self):
        self.ent.insert('end', '+')

    def clickMinus(self):
        self.ent.insert('end', '-')

    def clickSeven(self):
        self.ent.insert('end', '7')

    def clickEight(self):
        self.ent.insert('end', '8')

    def clickNine(self):
        self.ent.insert('end', '9')

    def clickDivide(self):
        self.ent.insert('end', '/')

    def clickFour(self):
        self.ent.insert('end', '4')

    def clickFive(self):
        self.ent.insert('end', '5')

    def clickSix(self):
        self.ent.insert('end', '6')

    def clickMultiply(self):
        self.ent.insert('end', '*')

    def clickOne(self):
        self.ent.insert('end', '1')

    def clickTwo(self):
        self.ent.insert('end', '2')

    def clickThree(self):
        self.ent.insert('end', '3')

    def clickZero(self):
        self.ent.insert('end', '0')

    def clickDot(self):
        self.ent.insert('end', '.')

    def clickEq(self):
        y = self.ent.get()
        self.ent.delete(0, 'end')
        self.ent.insert(0, str(eval(y)))

    def board(self, event):
        l = 'c Shift_L Shift_R Alt_L Alt_R Control_L Control_R Caps_Lock Num_Lock BackSpace Win_L Win_R App Tab quoteleft plus minus slash asterisk period 1 2 3 4 5 6 7 8 9 0 Return'.split()
        if event.keysym == 'Return':
            self.clickEq()
        if event.keysym == 'c':
            self.clickC()
        if not event.keysym in l:
            self.clickBS()
            if event.keysym == 'equal':
                self.clickEq()

    def main(self):
        self.place()
        self.window()

if __name__ == '__main__':
    app = App()
    app.main()
