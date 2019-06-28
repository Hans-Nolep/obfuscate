# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

print "\033[1;34m _______________________ "
print "\033[1;34m|                       |"
print "\033[1;34m|\033[1;33m Bash encryt & decrypt\033[1;34m |"
print "\033[1;34m|_______________________|\n"
print "\033[1;36mCoded by : Orang/Manusia"

banner2 = """
{}[{}1{}]{} Encript
{}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.rename("tes.sh", out)
       print (sukses + "Selesai..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File tidak ada!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Selesai..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File tidak ada!")


takok = raw_input(W + "Pilih" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Salah input")
