#!/usr/bin/env python3
"""
ROX - XOR Header Key Analyzer

Author: Jheff AT
Version: 1.0.0

Educational cryptanalysis utility that attempts to recover
simple XOR key patterns by comparing encrypted file bytes
against known binary file signatures such as JPEG, PNG, PDF,
ZIP, EXE and more headers.

<<Dict.bin>> should contain potential XOR keys to test against the file's header bytes. 
The script identifies repeated patterns in the decrypted output
to suggest likely keys and their corresponding decrypted headers. 
This can be useful for analyzing files that have been obfuscated
with a single-byte XOR cipher, especially when the original file 
type is unknown.        

"""
import string
from glob import glob
from sys import argv

__author__ = "Jheff AT"
__version__ = "1.0.0"
__email__ = "jheff.at@gmail.com"

def banner():
    print("""        ╔════════════════════════════╗
        ║  ██████╗  ██████╗ ██╗  ██╗ ║
        ║  ██╔══██╗██╔═══██╗╚██╗██╔╝ ║
        ║  ██████╔╝██║   ██║ ╚███╔╝  ║
        ║  ██╔══██╗██║   ██║ ██╔██╗  ║
        ║  ██║  ██║╚██████╔╝██╔╝ ██╗ ║
        ║  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ║
        ║                            ║
        ║  XOR Header Key Analyzer   ║
        ╚════════════════════════════╝""")
    print("\nAuthor: Jheff AT" + " | Version: " + __version__ + " Copyright (c) 2026 | Contact: " + __email__  + "\n")
    print("This tool attempts to recover XOR keys by analyzing the first 50")
    print("bytes of files against a dictionary of potential keys." )
    print("\nUsage: rox <file_pattern>")
    print("""Example: 
                rox *.jpg
                rox *.*
                rox videoclip.mp4\n""")
def rox(filex):
    dic=string.ascii_letters+string.digits+"!@#$%^&*()_+-=~`[]{}|;:'\",.<>/? "
    g=""
    d=open(filex,"rb").read(50)
    dik=open("dict.bin","rb") 
    lx=[] 
    for k  in dik:
        keymatched=''
        for c ,s in zip(d,k):
            g=chr(c^s)
            if g in dic:
                keymatched+=g    
        
        needle=keymatched[0:5]
        if keymatched.count(needle) > 1:
            positions = []
            start = 0
            while True:
                idx = keymatched.find(needle, start)
                if idx == -1:
                    break
                positions.append(idx)
                start = idx + 1          
            lx.append(f"🔑Encryption Key Recovered--->  {keymatched[0:positions[1]]}" )     
    return lx
def main():
    if glob("dict.bin")==0:
        print("Error: 'dict.bin' not found. Please ensure it is in the same directory as this script.")
        exit(1)
    g=argv
    if len(g)==2:
        l=glob(g[1])
        if len(l)==0:
            banner()
            exit("\nError:No files found matching the pattern.")
        banner()
        for i in l:
            print(f" 🔍Analyzing encrypted file {i.upper()}...")
            result=rox(i)       
            print("\n".join(f"     {i}. {item}" for i, item in enumerate(result, 1)) if result else "       -No matches found.")
    else:
        banner()

        

if __name__ == "__main__":    
    main()
    
