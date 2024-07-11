
from tkinter import *
from tkinter import ttk


def print_okey():
    print('clicked')



window = Tk()
window.title('Typing Speed')
window.geometry('1000x600+150+50')
window.resizable(False,False)


#styles
f1 = ttk.Style()
f1.configure('Danger.TFrame', background='snow2', borderwidth=1, relief='raised')

f2 = ttk.Style()
f2.configure('s.TFrame', background='ivory2', borderwidth=1, relief='raised')

#frames
main_frame= ttk.Frame(window,style='Danger.TFrame',width=200,height=200)
main_frame.pack_propagate(False)
subframe = ttk.Frame(main_frame,width=250,height=100,style='s.TFrame')
subframe.pack_propagate(False)

title_frame = ttk.Frame(window,style='Danger.TFrame',width=200,height=200)


operation = ttk.Frame(window,style='Danger.TFrame',width=200,height=200)

#subframes



#widgets












#positioning
#mainframe position
main_frame.pack(side='left',expand=False,fill='y')
subframe.pack()
ttk.Label(subframe,text='top').pack(side='top',expand=True)
ttk.Label(subframe,text='center',).pack(side='top',expand=True)
ttk.Label(subframe,text='bottom',).pack(expand=True)

title_frame.pack(side='top',expand = False,fil='x')


operation.pack(side='bottom',expand = True,fil='both')







window.mainloop()