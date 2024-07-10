from tkinter import *
from tkinter import ttk


def print_okey():
    print('clicked')



window = Tk()
window.title('Typing Speed')
window.geometry('1000x600+150+50')
window.resizable(False,False)

#main_frame
main_frame = Frame(window,bg='white')
# f1 = ttk.Style()
# f1.configure('Danger.TFrame', background='grey', borderwidth=5, relief='raised')

# f1 = ttk.Style()
# f1.configure('Danger.TFrame', background='grey', borderwidth=5, relief='raised')

# frm_1 = ttk.Frame(window, width=200, height=300, style='Danger.TFrame').grid(column=0,row=0)
# button = ttk.Button(frm_1, text='Okay', command=print_okey).grid(column=0,row=0)


# frm_2 = ttk.Frame(window,width=400,height=150).grid(column=1,row=0)

# frm_3 = ttk.Frame(window,width=400,height=150).grid(column=1,row=1)

window.mainloop()