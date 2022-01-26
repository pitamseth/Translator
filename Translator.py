from tkinter import *
from googletrans import Translator, constants
import requests
import tkinter.messagebox as tmsg
root = Tk()
root.minsize(500,535)
root.maxsize(500,535)
root.title("Language translator")
root.configure(bg="aqua")

input_lang = StringVar()
output_lang = StringVar()
opt = StringVar()

def check_internet():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
    except:
        tmsg.showerror("Error","No internet connection!!!")

def convert():
    out_str.delete('1.0','end')
    try:
        translators = Translator()
        translation = translators.translate(inp_str.get('1.0','end'), dest=opt.get())
        out_str.insert(END,translation.text)
    except:
        check_internet()

def start():
    check_internet()
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    root.configure(bg='green')
    global main_frame
    main_frame = Frame(root, bg="gray")
    main_frame.pack(padx=10, pady=5, fill=BOTH)
    Label(main_frame, text="Enter the text in English", bg="purple", font=('tacoma',15,'bold')).pack(padx=5, pady=5)
    inp_frame = Frame(main_frame)
    inp_frame.pack()
    scrollbar = Scrollbar(inp_frame)
    scrollbar.pack(fill=Y, side=RIGHT)
    global inp_str
    inp_str = Text(inp_frame, height=6, width=45, padx=10, wrap=WORD, yscrollcommand=scrollbar.set)
    inp_str.pack(pady=5, padx=5, side=TOP)
    inp_str.configure(font=("tacoma", 15, "bold"))
    inp_str.tag_configure("tag_name", justify='left')
    inp_str.insert(END,"Write something")
    scrollbar.config(command=inp_str.yview)
    mid_frame = Frame(main_frame, bg="gray")
    mid_frame.pack(side=TOP, pady=5, padx=5)
    option = ["Bengali","Hindi","Telugu","Marathi","Kannada","Japanese","Malayalam","Nepali","Chinese (Traditional)"]
    opt.set("Bengali")
    drop = OptionMenu(mid_frame, opt, *option)
    drop.pack(side=LEFT, padx=10)
    drop.config(bg="gray", font=("tacoma", 10, "bold"))
    Button(mid_frame, text="Convert", font=("tacoma", 10, "bold"), bg="red", command=convert).pack(side=LEFT, padx=10)
    global out_str
    out_frame = Frame(main_frame)
    out_frame.pack()
    scrollbar1 = Scrollbar(out_frame)
    scrollbar1.pack(fill=Y, side=RIGHT)
    out_str = Text(out_frame, height=6, width=45, padx=10, pady=10, wrap=WORD, yscrollcommand=scrollbar1.set)
    out_str.pack(pady=5, padx=5, side=TOP)
    out_str.configure(font=("tacoma", 15, "bold"))
    out_str.tag_configure("tag_name", justify='left')
    scrollbar1.config(command=out_str.yview)
    Button(root, text="Exit", font=('tacoma',10,'bold'), command=exit, bg='pink').pack(side=BOTTOM, anchor="e", padx=5, pady=5)

starting_frame = Frame(root, bg="aqua")
starting_frame.pack(padx=50, pady=50)
Label(starting_frame, text="Convert English \nto any language", font=('tacoma',20,'bold'), bg="aqua", fg='green').pack(padx=10, pady=20)
Button(root, text="Start", font=('tacoma',10,'bold'), command=start, bg='pink').pack(padx=10, pady=10)
root.mainloop()