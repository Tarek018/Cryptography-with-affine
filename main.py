from crypteAffine import crypteAffine
from decrypteAffine import decrypteAffine
import os
import tkinter as tk
from tkinter import ACTIVE, DISABLED, NORMAL, filedialog, messagebox, simpledialog
import re
import subprocess



crypte = crypteAffine()
decrypte = decrypteAffine()



root = tk.Tk()
root.geometry("600x600") 

def open_the_encryption_page():
    global root
    global crypte
    crypte.UI(root)
def open_the_decryption_page():
    global root
    global decrypte
    decrypte.UI(root)

encrypt_btn = tk.Button(root, text="Encrypt", command=open_the_encryption_page, state=NORMAL, height=5, width=20, cursor="hand2")
encrypt_btn.pack(padx=50, pady=50, side="left")

decrypt_btn = tk.Button(root, text="Decrypt", command=open_the_decryption_page, state=NORMAL, height=5, width=20, cursor="hand2")
decrypt_btn.pack(padx=50, pady=50, side="left")



root.mainloop() 