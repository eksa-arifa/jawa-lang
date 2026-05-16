#!/usr/bin/env python3
import sys
import os
from jawa_lang.logic.parseSyntax import parseSyntax

def jawaInterpreter():
    if len(sys.argv) < 2:
        print("Penggunaan: jawa <file.jawa>")
        return

    locateFile = sys.argv[1]

    if locateFile in ["--version", "-V"]:
        print("jawa-lang versi 0.1.5")
        return

    if not locateFile.endswith(".jawa"):
        print(locateFile + " " + "Bukan jawa language")
        return

    if not os.path.exists(locateFile):
        print(f"File {locateFile} ora ditemokake")
        return

    with open(locateFile, 'r') as f:
        fread = f.read()

    h = fread.split('\n')
    result = map(parseSyntax, h)
    res = list(result)

    ctoe = ""
    for r in res:
        ctoe += r + '\n'
    
    os.system("python3 -c '"+ctoe+"'")

if __name__ == "__main__":
    jawaInterpreter()
