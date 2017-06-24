from Tkinter import *
import Tkinter
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkMessageBox


url='http://www.espncricinfo.com/ci/engine/match/index.html?view=live'
r=requests.get(url)
html=r.text
match=[]
inning_1=[]
inning_2=[]
status=[]
date=[]

soup=BeautifulSoup(html,'html.parser')

info = soup.find(name='section',attrs={'id':'live-match-data'})
matches = info.find_all(name='section',attrs={'class':'default-match-block'})

i=0
while i<len(matches):    
    match.append(matches[i].find(name='span',attrs={'class':'match-no'}).get_text())
    inning_1.append(matches[i].find(name='div',attrs={'class':'innings-info-1'}).get_text())
    inning_2.append(matches[i].find(name='div',attrs={'class':'innings-info-2'}).get_text())
    status.append(matches[i].find(name='div',attrs={'class':'match-status'}).get_text())
    date.append(matches[i].find(name='span',attrs={'class':'bold'}).get_text())
    i+=1

################################################################################################    

root=Tk()

mb= Menubutton (root,text="Select Match",relief=RAISED)
mb.menu = Menu(mb,tearoff=0)
mb["menu"]=mb.menu

for x in range(len(matches)):
    mb.menu.add_checkbutton ( label=match[x] , command = lambda x=x: features(x) )

def features(x):       
        def match_name():
            tkMessageBox.showinfo('Name of match', match[x])
        M=Tkinter.Button(root, text='Name of match' , command=match_name , height=1, width=20).grid()
        
        
        def date_of():
            tkMessageBox.showinfo('Date',date[x])
        D=Tkinter.Button(root, text='Date' , command=date_of , height=1, width=20).grid()
        
        
        def status_1():
            tkMessageBox.showinfo('Status',status[x])
        S=Tkinter.Button(root, text='Status' , command=status_1 , height=1, width=20).grid()


        def inning_1_a():
            tkMessageBox.showinfo('First Innings',inning_1[x])
        I_1=Tkinter.Button(root, text='First Innings' , command=inning_1_a , height=1, width=20).grid()
        

        def inning_2_a():
            tkMessageBox.showinfo('Second Innings',inning_2[x])
        I_2=Tkinter.Button(root, text='Second Innings' , command=inning_2_a , height=1, width=20).grid()
        
mb.pack()
root.mainloop()











