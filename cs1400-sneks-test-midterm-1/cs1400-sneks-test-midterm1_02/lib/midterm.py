import hashlib
import re
import sys
from lib.magic import *
def k(z):
    return int(re.findall("\d",z)[-1])%len(X)==0
def xyz(a, b):
    if len(a)<3 or len(b)!=9 or (len(b)==9 and b[0]!="D" and not b[1:].isdecimal()):
        print("Invalid login information. Please input your correct Name and D Number.")
        sys.exit()
    a.encode(encoding="utf-8",errors="strict")
    m = hashlib.sha256(b.encode())
    a.zfill(5)
    return m.hexdigest()
def qwerty(y):
    return X[k(y)]
def generate(name, dnumber):
    asdf(xyz(name, dnumber), qwerty)
