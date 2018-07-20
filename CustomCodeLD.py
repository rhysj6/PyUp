#from CustomCode import *

#Please refer to the documentation if you are stuck
def printc(text_to_print,no_of_prints):
    print(text_to_print * no_of_prints)
def scrclr():
    print("" *50)

def scrclrc(lines):
    print(""*lines)

def wait(wt):
    import time
    time.sleep(wt)

def w2f(filename,texttowrite):
    text1 = open(filename,"w+")
    text1.write(texttowrite)
    text1.close()

def rff(filename,pos = True):
    text1 = open(filename, "w+")
    if pos = True:
        string = text1.read()

    else:
        string = text1.read(pos)
    text1.close
    return string
def encrypt(decrypted_string_var,key):
    encrypted_list_var = [""]
    for c in decrypted_string_var:
        x=ord(c)
        x = x + key
        c2 = chr(x)
        encrypted_list_var.append(c2)
    encrypted_string_var = "".join(encrypted_list_var)
    return encrypted_string_var
def decrypt(encrypted_string_var,key):
    decrypted_list_var = [""]
    for c in encrypted_string_var:
        x=ord(c)
        x = x - key
        c2 = chr(x)
        decrypted_list_var.append(c2)
    decrypted_string_var = "".join(decrypted_list_var)
    return decrypted_string_var
def checkLicenceC (filename,key,mode):
    text1 = open(filename, "w+")
    Licence = text1.read()
    text1.close
    if Licence == key:
        if mode=="a":
            print("Licence Accepted")
    else:
        if mode == "a":
            input("Licence Denied! Press Enter to exit.")
        pass
def checkLicence (filename):
    text1 = open(filename, "r")
    Licence = text1.read()
    text1.close
    if Licence == "True":
        print("Licence Accepted")
    else:
        input("Licence Denied! Press Enter to exit.")
        while True:
            wait(1)
def BackgroundHandler():
    checkLicence("BackGroundHandlerLog.txt")

def makeFolder(foldername,mode):
    import os
    os.mkdir(foldername)
    if mode=="a":
        os.chdir(foldername)

def getPageCode(page):
    import urllib.request
    x = urllib.request.urlopen(page).read().decode("utf-8"))
    return x

