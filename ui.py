


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
title_window = ttk.Label(window,text = 'TYPING TEST' ,font=('Arial 35 bold'),relief='flat').pack(side='top')
#frames

#side frame
side_frame= ttk.Frame(window, style='Danger.TFrame', width=200, height=200,padding=10)
side_frame.pack_propagate(False)
# subframe = ttk.Frame(side_frame, width=250, height=100, style='s.TFrame')
# subframe.pack_propagate(False)
start_btn = ttk.Button(side_frame,text='Start').pack(side='top',fill='y')

reset_btn = ttk.Button(side_frame,text='Reset').pack(side='bottom',fill='y')

timer = ttk.Label(side_frame,text='timer',padding=10).pack(side='top')
timer_value = ttk.Label(side_frame,text='0').pack(side='top')
wpm = ttk.Label(side_frame,text='words per minute').pack(side='top')
timer_value = ttk.Label(side_frame,text='0').pack(side='top')
accuracy = ttk.Label(side_frame,text='accuracy').pack(side='top')
timer_value = ttk.Label(side_frame,text='0').pack(side='top')


#text frame
text_frame = ttk.Frame(window,style='Danger.TFrame',width=200,height=200,padding=20)
text_frame.pack_propagate(False)
paragraph = ttk.Label(text_frame,text='ram',wraplength=1000,justify='left')

#input frame
input_frame = ttk.Frame(window, style='Danger.TFrame', width=200, height=200,padding=20)
entry = Text(input_frame,height=8,width=110)
#subframes



#widgets












#positioning
#mainframe position
side_frame.pack(side='left', expand=False, fill='y')

# subframe.pack()



#text frame position


text_frame.pack(side='top',expand = False,fil='x')
paragraph.pack()



#input frame position
input_frame.pack(side='bottom', expand = True, fil='both')
entry.pack()






window.mainloop()