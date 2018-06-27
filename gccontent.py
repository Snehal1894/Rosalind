# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Template
# and open the template in the editor.
from __future__ import division

def filewrite():
    f1=open("/home/snehal/Downloads/Rosalind/gc.txt","r")
    f2=open("/home/snehal/Downloads/Rosalind/test1.txt","w")
    lns=f1.readlines()
    s=""
    for l in lns:
        if ">" in l:
            f2.write(s+"\n")
            f2.write(l)
            s=""
        else:
            s=s+l.rstrip("\n")
    f2.write(s+"\n")
    f2.close()
    
def GCcontent(s):
    cnt=s.count("G")+s.count("C")
    return (cnt/(len(s)-1))*100

#filewrite()
cnt=0
s=""
f1=open("/home/snehal/Downloads/Rosalind/test1.txt","r")
lines=f1.readlines()

for i in range(1,len(lines),2):
    cnt1=GCcontent(lines[i])
    if cnt1>cnt:
        cnt=cnt1
        s=lines[i-1].replace(">","")
        
print s+str(cnt)
       

    
