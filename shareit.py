#!/usr/bin/python

import socket
from findIP import Network
from Tkinter import *
import tkFileDialog as filedialog

def send0OrReceive1(args):
    button1.configure(state='disabled')
    button2.configure(state='disabled')
    if args == 0:
        for item in l.curselection():
            send_file(l.get(item)[0], l.get(item)[1])
    elif args == 1:
        receive_file()
    root.destroy()

def send_file(ip_receiver, name_receiver):
    file_path = filedialog.askopenfilename(initialdir=".", title="Select file to send to " + name_receiver)
    if file_path.find('/') != -1:
        file_name = file_path.split('/')[-1]
    else:
        file_name = file_path
    file_name_length = len(file_name)
    digits = len(str(file_name_length))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_receiver, port))
    s.send(str(digits).encode())
    s.send(str(file_name_length).encode())
    s.send(file_name.encode())
    f = open(file_path, "rb")
    chunk = f.read(1024)
    while chunk:
        s.send(chunk)
        chunk = f.read(1024)

    f.close()
    s.close()

def receive_file():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    while True:
        c, addr = s.accept()
        print('{} connected'.format(addr))

        digits = c.recv(1).decode()
        file_name_length = c.recv(int(digits)).decode()
        file_name = c.recv(int(file_name_length)).decode()
        print('Receiving file: ' + file_name)
        file_path = "./Received/" + file_name
        f = open(file_path, "wb")
        chunk = c.recv(1024)
        while chunk:
            print(1)
            f.write(chunk)
            chunk = c.recv(1024)
        f.close()
        c.close()
        print('Done Receiving. File at: ' + file_path)
    s.close()

manually_entered_ip = '192.168.43.103'
(ip, name), neighbours = (manually_entered_ip, 'My Self'), [('192.168.43.103', 'Alice'),
('192.168.43.103', 'Bob'), ('192.168.43.103', 'Cat')]
# If nmap not installed, comment below line and un-comment above 3 lines
# (ip, name), neighbours = Network().networkscanner()
port = 12345

root = Tk()
root.title("Share it")


button2 = Button(root, text="Recieve", command=lambda:send0OrReceive1(1))
button2.pack()

Label(text="OR").pack()

button1 = Button(root, text="Send", command=lambda:send0OrReceive1(0))
button1.pack(pady=20)

Label(text="Select devices to send").pack()
l = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
for i in range(len(neighbours)):
    l.insert(i, neighbours[i])
l.pack()

root.geometry("400x400+120+120")
root.mainloop()

