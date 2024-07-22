import tkinter
from tkinter import *
from tkinter import ttk
import ttkthemes as tt
import time as t
import threading
###########################################CODE############################################
#   variables


timelimit = 10
remainingtime = timelimit

totalwords = 0
wrongwords = 0

wpm=0
accuracy = 0



###################################################back##############################################################
def start_timer():
    global timer
    entry.focus()
    entry.config(state=NORMAL)
    start_btn.config(state=DISABLED)
    for time in range(1,timelimit+1):
        timer = time
        timer_value['text'] = timer
        t.sleep(1)
        window.update()
    entry.config(state=DISABLED)
    reset_btn.config(state=NORMAL)


def count():
    global wrongwords
    global timer
    global timer_mt
    para_words = pg['text'].split()
    while timer !=timelimit:
        enteredpara = entry.get("1.0","end-1c").split()
        print(len(enteredpara))
        totalwords = len(enteredpara)
    for pair in list(zip(para_words,enteredpara)):
        if pair[0]!= pair[1]:
            wrongwords+=1
    timer_mt = int(timer)/60

    w_pm =(totalwords-wrongwords)/timer_mt
    wpm_value['text']=w_pm
    #accuracy
    gross_wpm = totalwords/timer_mt
    accuracy_ = (w_pm/gross_wpm)*100
    accuracy_value['text'] = round(accuracy_)

def start():
    thr1 = threading.Thread(target=start_timer)
    thr1.start()
    thr2 = threading.Thread(target=count)
    thr2.start()

def reset():
    global remainingtime
    global timer
    reset_btn.config(state=DISABLED)
    start_btn.config(state=NORMAL)
    entry.config(state=NORMAL)
    entry.delete(1.0,tkinter.END)
    entry.config(state=DISABLED)
    remainingtime = timelimit
    timer=0
    timer_value['text']=0
    wpm_value['text'] = 0
    accuracy_value['text'] = 0





##########################################GUI###############################################

window = tt.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title('Typing Speed')
window.geometry('1000x600+150+50')
window.resizable(False,False)







#styles
f1 = ttk.Style()
f1.configure('Danger.TFrame', background='snow2', borderwidth=1, relief='raised')
f3 = ttk.Style()
f3.configure(style='')

f2 = ttk.Style()
f2.configure('s.TFrame', background='ivory2', borderwidth=1, relief='raised')
title_window = ttk.Label(window,text = 'TYPING TEST' ,background='yellow',font=('Arial 35 bold'),relief='flat')
title_window.pack(side='top')
#frames

#side frame
side_frame= ttk.Frame(window, style='Danger.TFrame', width=200, height=200,padding=10)
side_frame.pack_propagate(False)
# subframe = ttk.Frame(side_frame, width=250, height=100, style='s.TFrame')
# subframe.pack_propagate(False)
start_btn = ttk.Button(side_frame,text='Start',state=NORMAL,command=start)


reset_btn = ttk.Button(side_frame,text='Reset',command=reset)
reset_btn.config(state=DISABLED)


timer = ttk.Label(side_frame,text='timer',padding=10)
timer_value = ttk.Label(side_frame,text='60')
wpm = ttk.Label(side_frame,text='words per minute')
wpm_value = ttk.Label(side_frame,text='0')
accuracy = ttk.Label(side_frame,text='accuracy')
accuracy_value = ttk.Label(side_frame,text='0')


#text frame
text_frame = ttk.Frame(window,style='Danger.TFrame',width=200,height=200,padding=20)
text_frame.pack_propagate(False)
para = "At first the professor scowled with concern. But then he said, that's all right. Run to my house. Tell my wife to give you one of my shirts. 'Mrs. Esputa quickly fetched one of her husband's white shirts. But when Philip put it on, she began to exclaim, 'Oh, dear! Gracious!' The shirt was so large that Philip was almost lost in it. Hastily Mrs. Esputa found a box of pins. In a twinkling, her nimble fingers pinned enough tucks in the shirt to make it fit Philip. They both heaved a big sigh of relief when the job was finished. "
pg = ttk.Label(text_frame,text=para,wraplength=750,justify='left')

#input frame
input_frame = ttk.Frame(window, style='Danger.TFrame', width=200, height=200,padding=20)
entry = Text(input_frame,height=8,width=110)
entry.config(state=DISABLED)
#subframes



#widgets












#positioning
#mainframe position
side_frame.pack(side='left', expand=False, fill='y')
start_btn.pack(side='top',fill='y')
timer.pack(side='top',expand=True)
timer_value.pack(side='top')
wpm.pack(side='top',expand=True)
wpm_value.pack(side='top',expand=True)
accuracy.pack(side='top',expand=True)
accuracy_value.pack(side='top',expand=True)
reset_btn.pack(side='bottom',fill='y')
# subframe.pack()



#text frame position


text_frame.pack(side='top',expand = False,fil='x')
pg.pack()



#input frame position
input_frame.pack(side='bottom', expand = True, fil='both')
entry.pack()


window.mainloop()


