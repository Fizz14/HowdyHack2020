#Blasterjacks submission :D
#SecretCode generator
#Huge thanks to Nathan R and William Z for mentering!



import tkinter as tk
import main as m
import ctypes


def sel():
   label.config(text = str(var.get()))

def run():
    print("run button clicked!")
    
    
    methodstring = keystring.get()
    print(methodstring)
    secretstring = mstring.get()
    print(secretstring)
    message.delete(0,"end")
    
    print(m.exe_method(methodstring))
    
    if(var.get() == "encryption:"):
        message.insert(0,m.exe_encrypt(secretstring))
        print(m.exe_encrypt(secretstring))
    else:
        message.insert(0,m.exe_decrypt(secretstring))
        print(m.exe_decrypt(secretstring))

    

def copy_output():
    print("copy_output button clicked!")
    secretstring = mstring.get()
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(secretstring)

def copy_key():
    print("copy_key button clicked!")
    methodstring = keystring.get()
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(methodstring)


def paste_output():
    print("paste_output button clicked!")
    pastestring = root.clipboard_get()
    message.delete(0,"end") # clear message contents
    message.insert(0,pastestring)

def paste_key():
    print("paste_key button clicked!")
    pastestring = root.clipboard_get()
    key.delete(0,"end") # clear key contents
    key.insert(0,pastestring)


def help():
    ctypes.windll.user32.MessageBoxW(0, "Enter a key and a message, then select either 'Encrypt' or 'Decrypt', and finally, click 'Run' to transform your message. Keys are built by stringing operations together, in the form 'operation_number:parameter, parameter;operation_number:parameter, parameter;'. There are three operations: \n\n1) Move the characters up or down ASCII keys. First parameter is amount to move up or down, second is to what character to apply it. e.g. 'apple' becomes 'bqqmf'. \n\n2) Takes one parameter, which pushes the string laterally by that number of characters, e.g. 'paper' becomes 'erpap'. \n\n3) Switches two sets of characters, found by position from two parameters. e.g. 'scraps' becomes 'csrapc'. \n\nWith these three operations, it's possible to turn any message into any encryption, and back again. :D\n\nExample Keys: \n1:-3,2;3:3,5;2:-15; \n3:2,4;1:23;2:-5;1:40,10;2:-5;1:80,10; \n3:0,1;2:-2;3:0,1:2:-1;1:-24;", "Help", 0)
    
def about():
    
    ctypes.windll.user32.MessageBoxW(0, "This was an entry to Howdyhack 2020 by Xavier, Cole Newby, and Joseph Buskmiller, to fit the spy theme. It is simple software to encrypt and decrypt text based on a key. It uses tkinter and ctypes. \n\nSpecial thanks to Nathan R. and William Z. for mentering us!", "What is this?", 0)


# Start Menu
root = tk.Tk()
root.geometry("500x500")
#root.resizable(False,False)
root.title("Blasterjack's Encrypter")
root.iconbitmap('large.ico')
root['bg']= '#dfe0e2'

# setting radio button values to integer
var = tk.StringVar(value="encryption:")

# frame
frametop = tk.Frame(root)
frametop.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

#button image
b_up = tk.PhotoImage(file="button_up.png")
b_down = tk.PhotoImage(file="button_down.png")


# top buttons
send_button = tk.Radiobutton(frametop, text="Encrypt", variable=var, value="encryption:", command=sel, indicatoron = 0)
receive_button = tk.Radiobutton(frametop, text="Decrypt", variable=var, value="decryption:", command=sel, indicatoron = 0)
about_this_app_button = tk.Button(frametop, text ="What is this?", bg='white', bd = 1, command=about)

send_button.config(image=b_up)
receive_button.config(image=b_up)


# Message entry
mstring = tk.StringVar()
message = tk.Entry(frametop, textvariable=mstring)
message.insert(0,"Type your message to encrypt/decrypt here. . .")

# Key entry
keystring = tk.StringVar()
key = tk.Entry(frametop, textvariable=keystring)
key.insert(0,"Type your key here. . .")

# Run button
run_button = tk.Button(frametop, text = "Run", command=run)

# Operations button
operations_button = tk.Button(frametop, text = "Help", command=help)

# copy message button
copy_message_button = tk.Button(frametop, text = "Copy Message", command=copy_output)
copy_message_button.config(image=b_up)

# copy key button
copy_key_button = tk.Button(frametop, text = "Copy Key", command=copy_key)

# paste message button
paste_message_button = tk.Button(frametop, text = "Paste Message", command=paste_output)

# paste key button
paste_key_button = tk.Button(frametop, text = "Paste Key", command=paste_key)

send_button.pack()
receive_button.pack()
message.pack()
key.pack()
about_this_app_button.pack()
operations_button.pack()
paste_key_button.pack()
copy_key_button.pack()
paste_message_button.pack()
copy_message_button.pack()
run_button.pack()

send_button.place(relx=0,rely=0, relheight = 0.1, relwidth = 0.5)
receive_button.place(relx=0.5, rely= 0, relheight = 0.1, relwidth = 0.5)

message.place(relx=0.666,rely=0.300, relheight=0.1, relwidth=0.55, anchor=tk.E)
key.place(relx=0.666, rely=0.633, relheight=0.1, relwidth=0.55,anchor=tk.E)

copy_message_button.place(relx=0.666,rely=0.3,relheight = 0.05, relwidth = 0.1,anchor=tk.NW)
paste_message_button.place(relx=0.666, rely= 0.3,relheight = 0.05, relwidth = 0.1,anchor=tk.SW)

copy_key_button.place(relx=0.666,rely=0.633,relheight = 0.05, relwidth = 0.1, anchor=tk.NW)
paste_key_button.place(relx=0.666, rely= 0.633,relheight = 0.05, relwidth = 0.1, anchor=tk.SW)

about_this_app_button.place(relx=0.333,rely=0.9,relheight=0.05, relwidth = 0.1, anchor=tk.CENTER)
operations_button.place(relx=0.666, rely= 0.9,relheight=0.05, relwidth = 0.1,anchor=tk.CENTER)

run_button.place(relx=0.5,rely=0.8, relheight=0.05, relwidth=0.1, anchor=tk.CENTER)






#message.place(x=)

# run

run = 1







root.mainloop()