from tkinter import *
import winsound

root = Tk()
root.title("Notes") # title bar
root.attributes('-topmost', True)
root.geometry("200x100") # size
root.configure(background="white") # background
lbl1 = Label(root, text="Play", font=("Ariel Bold", 50)) # where words will appear
lbl1.configure(background="white") # Making the text colour fit
lbl1.place(relx=.5, rely=.40, anchor="center") # in the middle

# top row

def q(event=None): 
    winsound.Beep(207, 200) # g#3
    lbl1.config(text = "g#3")
def a(event=None): 
    winsound.Beep(220, 200) # a3
    lbl1.config(text = "a3")
def w(event=None): 
    winsound.Beep(233, 200) # a3#
    lbl1.config(text = "a#3")
def s(event=None): 
    winsound.Beep(247, 200) # b3
    lbl1.config(text = "b3")
def d(event=None): 
    winsound.Beep(261, 200) # c3
    lbl1.config(text = "c3")
def e(event=None): 
    winsound.Beep(277, 200) # c#4
    lbl1.config(text = "c#4")
def f(event=None): 
    winsound.Beep(293, 200) # d4
    lbl1.config(text = "d4")
def r(event=None): 
    winsound.Beep(311, 200) # d#4
    lbl1.config(text = "d#4")
def g(event=None): 
    winsound.Beep(330, 200) # e4
    lbl1.config(text = "e4")
def h(event=None): 
    winsound.Beep(349, 200) # f4
    lbl1.config(text = "f4")
    
# second row

def t(event=None): 
    winsound.Beep(370, 200) # f#4
    lbl1.config(text = "f#4")
def j(event=None): 
    winsound.Beep(392, 200) # g4
    lbl1.config(text = "g4")
def y(event=None): 
    winsound.Beep(415, 200) # g#4
    lbl1.config(text = "g#4")
def k(event=None): 
    winsound.Beep(440, 200) # a4
    lbl1.config(text = "a4")
def u(event=None): 
    winsound.Beep(466, 200) # a#4
    lbl1.config(text = "a#4")
def l(event=None): 
    winsound.Beep(494, 200) # b4
    lbl1.config(text = "b4")
def z(event=None): 
    winsound.Beep(523, 200) # c5
    lbl1.config(text = "c5")
def i(event=None): 
    winsound.Beep(554, 200) # c#5
    lbl1.config(text = "c#5")
def x(event=None): 
    winsound.Beep(587, 200) # d5
    lbl1.config(text = "d5")
    
# third row

def o(event=None): 
    winsound.Beep(622, 200) # d#5
    lbl1.config(text = "d#5")
def c(event=None): 
    winsound.Beep(659, 200) # e5
    lbl1.config(text = "e5")
def v(event=None): 
    winsound.Beep(698, 200) # f5
    lbl1.config(text = "f5")
def p(event=None): 
    winsound.Beep(740, 200) # f#5
    lbl1.config(text = "f#5")
def b(event=None): 
    winsound.Beep(784, 200) # g5
    lbl1.config(text = "g5")
def n(event=None): 
    winsound.Beep(831, 200) # g#5
    lbl1.config(text = "a5")
def m(event=None): 
    winsound.Beep(988, 200) # a5
    lbl1.config(text = "b5")

# binding keys to the notes
    
root.bind('<q>', q) 
root.bind('<w>', w) 
root.bind('<e>', e) 
root.bind('<r>', r) 
root.bind('<t>', t) 
root.bind('<y>', y) 
root.bind('<u>', u)
root.bind('<i>', i) 
root.bind('<o>', o) 
root.bind('<p>', p) 

root.bind('<a>', a) 
root.bind('<s>', s) 
root.bind('<d>', d) 
root.bind('<f>', f) 
root.bind('<g>', g) 
root.bind('<h>', h) 
root.bind('<j>', j) 
root.bind('<k>', k)
root.bind('<l>', l)

root.bind('<z>', z)
root.bind('<x>', x)
root.bind('<c>', c)
root.bind('<v>', v)
root.bind('<b>', b)
root.bind('<n>', n)
root.bind('<m>', m)

root.lift()
root.focus_force()
root.mainloop()
