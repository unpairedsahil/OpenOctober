import socket, os
import onetimepad as otp
from tkinter import *
from tkinter import messagebox
s = socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(1)
c,addr = s.accept()
def Encrypt_Window():
    master = Tk()
    master.title("Encryption - Server")
    f1 = Frame(master, height = 200, width = 400).pack()
    Button(master, text = "Encrypt Strings?", width=25, command=Encrypt_String,background="orange",fg="black").place(x=100, y=50)
    Button(master, text = "Encrypt Files?", width=25, command=Encrypt_File,background="orange",fg="black").place(x=100, y=100)
def Encrypt_String():
    def Encrypt():
        messagebox.showinfo("Server Site", "Encrypted file is created")
        file = open("encryptedmsg.txt", "w")
        encrypt = otp.encrypt(e1.get(), e2.get())
        file.write(encrypt)
        file.close()
        FILE_TRANSFER_SERVER2CLIENT()
    master = Tk()
    master.title("Encryption of Strings - Server")
    f1 = Frame(master, height = 200, width = 400).pack()
    Label(master, text="Enter a String that must be Encrypted",background="black",fg="orange").place(x=0,y=30)
    e1 = Entry(master, textvariable=StringVar(), fg="black", bg="white")
    e1.place(x=250, y=30)
    Label(master, text="Enter a Key for Encryption",background="black",fg="orange").place(x=0,y=60)
    e2 = Entry(master, textvariable=StringVar(), fg="black", bg="white")
    e2.place(x=250, y=60)
    Button(master, text = "Encrypt", width=25, command=Encrypt,background="orange",fg="black").place(x=100, y=100)
def Encrypt_File():
    def Encrypt():
        messagebox.showinfo("Server Site", "Encrypted file is created")
        reader_file = open(str(e3.get()), "r")
        file = open("encryptedmsg.txt", "w")
        file.write(otp.encrypt(reader_file.read(), e4.get()))
        file.close()
        FILE_TRANSFER_SERVER2CLIENT()
    master = Tk()
    master.title("Encryption of Files - Server")
    f1 = Frame(master, height = 200, width = 400).pack()
    Label(master, text="Enter the file name that must be Encrypted",background="black",fg="orange").place(x=0,y=30)
    e3 = Entry(master, textvariable=StringVar(), fg="black", bg="white")
    e3.place(x=250, y=30)
    Label(master, text="Enter a Key for Encryption",background="black",fg="orange").place(x=0,y=60)
    e4 = Entry(master, textvariable=StringVar(), fg="black", bg="white")
    e4.place(x=250, y=60)
    Button(master, text = "Encrypt", width=25, command=Encrypt,background="orange",fg="black").place(x=100, y=100)
def File_Checker():
    res = os.path.isfile('./encryptedmsg.txt')
    return(res)


def Decrypt_Window():
    FILE_TRANSFER_CLIENT2SERVER()
    def Decrypt():
        file = open('encryptedmsg.txt', "r")
        decrypt = otp.decrypt(str(file.read()), e4.get())
        temp = str(decrypt)
        #Label(top, text = "Message is "+temp, fg="black").place(x=150, y=150)
        messagebox.showinfo("Message", temp)
        file.close()
    top = Tk()
    top.title("Decryption - Server")
    f1 = Frame(top, height = 200, width = 400).pack()
    if (File_Checker()):
        Label(top, text="The Message Exists ",background="black",fg="orange").place(x=0,y=30)
        Label(top, text="Enter the Key for Decryption",background="black",fg="orange").place(x=0,y=60)
        e4 = Entry(top, textvariable=StringVar(), fg="black", bg="white")
        e4.place(x=250, y=60)
        Button(top, text = "Decrypt", width=25, command=Decrypt,background="Orange",fg="black").place(x=200, y=110)
    else:
        Label(top, text="A Message doesn't exist. Try again").place(x=0,y=30)
        
    #e3 = Entry(top, textvariable=StringVar(), fg="black", bg="white")
    #e3.place(x=250, y=30)
def FILE_TRANSFER_CLIENT2SERVER():
    f1 = open("encryptedmsg.txt", "w")
    f1.write(c.recv(2048).decode())
    print("File Transfer Successful")
    f1.close()
    '''f1 = open("Demo1.txt", "r")
    print("New File (Demo 1) Contents are ")
    print(f1.read())'''
def FILE_TRANSFER_SERVER2CLIENT():
    #filename = c.recv(2048).decode()
    #print("Client requests file",filename)
    f = open('encryptedmsg.txt', "r")
    c.send(f.read().encode())
    f.close()
def GUI():
    root = Tk()
    root.title("Python Project - Cryptography Server")
    f = Frame(root, height = 300, width = 800,background="Orange").pack()
    Label(root, text="Cryptography of Strings using Python",background="black",fg="orange").place(x=300,y=0)
    Label(root, text="Cryptography is the art of communication between two users via coded messages.",background="black",fg="orange").place(x=0,y=30)
    Label(root, text="The science of cryptography emerged with the basic motive of providing security to the confidential messages transferred from one party to another.",background="black",fg="orange").place(x=0,y=60)
    Label(root, text="Cryptography is defined as the art and science of concealing the message to introduce privacy and secrecy as recognized in information security.",background="black",fg="orange").place(x=0,y=90)   
    Button(root, text = "Encrypt Data", width=25, command=Encrypt_Window).place(x=200, y=210)
    Button(root, text = "Decrypt Data", width=25, command=Decrypt_Window).place(x=450, y=210)
    Button(root, text = "Close", width=25, command=root.destroy).place(x=325, y=250)
GUI()
