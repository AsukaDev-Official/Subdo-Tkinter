#!/usr/bin/env python3
import tkinter
import tkinter.messagebox
from tkinter import *
import requests, json

root = tkinter.Tk()
root.title('Subdomain Scanner')

header = Label(root, text='Asukadev Official\nSubdomain Scanner\nCoded : Tegar Dev').pack()

L1 = Label(root, text="Url : ")
L1.pack()
global input, input2
input = StringVar()
input2 = StringVar()
E1 = Entry(root, bd =5, textvariable = input)
E1.pack()
E1.focus_set()
L2 = Label(root, text='save to : ').pack()
E2 = Entry(root, bd =5, textvariable = input2)
E2.pack()
E2.focus_set()

def show():
    url = input.get()
    save = input2.get()
    api = 'http://jamet1337.ml/api/subdo.php?url='
    req = requests.get(api+url)
    jeson = json.loads(req.text)
    List = jeson['hasil']
    list = "Subdomain : \n" + List
    file = open(save, 'w')
    file.write(list)
    file.close()
    hasil = Label(root, text='save to : '+save).pack()
    tkinter.messagebox.showinfo("Subdo Scanner",list)

btn = tkinter.Button(root, text="Scan", padx=5, pady=5, width=10,
    command=show)
btn.pack(pady=10)

root.geometry('300x300+300+250')
root.mainloop()
