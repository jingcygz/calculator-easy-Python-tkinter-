from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def more():
    global win
    win = Tk()
    win.geometry("500x500")
    win.title('计算器附属窗口')
    a = "计算器附属窗口"

    def ci():
        try:
            num = float(ent3.get()) ** float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("error", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def yu():
        try:
            num = float(ent3.get()) % float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("error", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def zheng():
        try:
            num = float(ent3.get()) // float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("error", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def exit():
        b = '是否退出？'
        a = messagebox.askquestion("询问？", '%s' % b)
        if a == 'yes':
            win.destroy()
        else:
            pass

    lb4 = Label(win, text='计算器附属窗口')
    lb4.pack()

    lb5 = Label(win, text="数字一")
    lb5.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

    lb6 = Label(win, text="数字二")
    lb6.place(relheight=0.1, relwidth=0.5, rely=0.6, relx=0.1)

    bt6 = Button(win, text="次方", command=ci)
    bt6.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

    bt7 = Button(win, text="取余", command=yu)
    bt7.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

    bt8 = Button(win, text="取整", command=zheng)
    bt8.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

    bt9 = Button(win, text="退出", command=exit)
    bt9.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

    ent3 = Entry(win)
    ent3.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

    ent4 = Entry(win)
    ent4.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

    bt10 = Button(win, text="更多", command=more)
    bt10.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

    messagebox.showinfo("请切换至", '%s' % a)


def more1():
    global t
    t = Tk()
    t.geometry('500x500')
    t.title("计算器")
    t.iconbitmap(default="./calculator-icon_34473.ico")
    lb1 = Label(t, text="计算器")
    lb1.pack()

    def jia():
        try:
            num = float(ent1.get()) + float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("error", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def jian():
        try:
            num = float(ent1.get()) - float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("error", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def cheng():
        try:
            num = float(ent1.get()) * float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            messagebox.showerror("确定？", '%s' % a)
        else:
            messagebox.showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def chu():
        while 1:
            try:
                num = float(ent1.get()) / float(ent2.get())
                if float(ent2.get()) == 0:
                    a = "输入的数字不能为零"
                    messagebox.showerror("error", '%s' % a)
                    ent2.delete(0, END)
                    break
            except:
                a = "输入的数字格式不正确,请重新输入"
                messagebox.showerror("error", '%s' % a)
                ent1.delete(0, END)
                ent2.delete(0, END)
                break
            else:
                messagebox.showinfo("得数是", '%f' % num)
                ent1.delete(0, END)
                ent2.delete(0, END)
                break

    def exit():
        b = '是否退出？'
        a = messagebox.askquestion("error", '%s' % b)
        if a == 'yes':
            t.destroy()
        else:
            pass

    lb2 = Label(t, text="数字一")
    lb2.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

    lb3 = Label(t, text="数字二")
    lb3.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

    bt1 = Button(t, text="加", command=jia)
    bt1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

    bt2 = Button(t, text="减", command=jian)
    bt2.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

    bt3 = Button(t, text="乘", command=cheng)
    bt3.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

    bt5 = Button(t, text='除', command=chu)
    bt5.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

    bt4 = Button(t, text="更多", command=more)
    bt4.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

    bt9 = Button(t, text="退出", command=exit)
    bt9.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

    ent1 = Entry(t)
    ent1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

    ent2 = Entry(t)
    ent2.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

    t.mainloop()


if __name__ == '__main__':
    more1()
