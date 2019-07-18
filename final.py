from tkinter import *
from googletrans import Translator
import speech_recognition as sr
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

root=Tk()
root.geometry('1500x1500')
root.title("Speech to text")
# This script is intended to translate a text to multiple languages which can be used to improve search results.
Label(root,text="Enter the text to be converted",font=("arial",20,"bold")).place(x=450,y=150)
textBox=Text(root, height=10, width=40)
textBox.place(x=480,y=200)
#st="hello"
#   textBox.insert(chars,'bangalore')
g=""
tkvar = StringVar(root)
 
# Dictionary with options
choices = {
        'Afrikaans':'af',
'Albanian':'sq',
'Arabic':'ar',
'Azerbaijani':'az',
'Basque':'eu',				
'Bengali':'bn',
'Belarusian':'be', 			
'Bulgarian':'bg',
'Catalan':'ca',
'Chinese Simplified':'zh-CN',
'Chinese Traditional':'zh-TW',
'Croatian':'hr',
'Czech':'cs',
'Danish':'da',
'Dutch':'nl',
'English':'en',
'Esperanto':'eo',
'Estonian':'et',
'Filipino':'tl',
'Finnish':'fi',
'French':'fr',
'Galician':'gl',
'Georgian':'ka',
'German':'de',
'Greek':'el',
'Gujarati':'gu',
'Haitian Creole':'ht',
'Hebrew':'iw',
'Hindi':'hi',
'Hungarian':'hu',
'Icelandic':'is',
'Indonesian':'id',
'Malayalam':'ml',
'Irish':'ga',
'Italian':'it',
'Japanese':'ja',
'Kannada':'kn',
'Latin':'la'


    }
tkvar.set('kannada') # set the default option
 
popupMenu = OptionMenu(root, tkvar, *choices)
Label(root, text="Choose a language").place(x=100,y=150)
popupMenu.place(x=100,y=170)
 
# on change dropdown value
def change_dropdown(*args):
    global g
    p=tkvar.get()
    g=choices[p]
    print(g)
tkvar.trace('w', change_dropdown)
def record():
    global l
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #print ('say something')
        audio=r.listen(source)
    try:
        textBox.insert('1.0',r.recognize_google(audio,language=g))
    except:
        pass
btn=Button(root,text="record",command=record).pack()

t=""
x=0
y=500
def new_window():
    root1=Toplevel()
    root1.geometry('1500x1500')

    #input="Muhammad shahbaz khan "
    global t
    
    l=t.split()
    q=0
    p=-1
    photo=[x for x in range(len(t))]
    j=0
    k=0
    for i in l:
        p=p+1
        q=0
    
        for j in i:
            if j=='\'' or j=='?' or j==':' or j==',' or j=='.':
                Label(root1,text=j).grid(row=p,column=q)
                q=q+1
    
            elif j!=' ':
            
                photo[k]=PhotoImage(file=j+'.gif')
                photo[k]=photo[k].subsample(2)

                labelphoto=Label(root1,image=photo[k]).grid(row=p,column=q)
                q=q+1
                k=k+1
            else:
                pass
    root1.mainloop()
#b=Button(root,text="click for new window",command=new_window).pack()

def get_text():
    text=textBox.get("1.0",END+"-1c")
    return text
def convert_to_American():
    
  #  text = input("enter the text to be converted\n")
    global t
    destination_languages = {
            
            'English':'en'
            
        }
        
        
    tar=destination_languages["English"]
    translator = Translator()
    text=get_text()
    t=translator.translate(text, dest=tar).text
    t=t.lower()
    s_t=['what is your name','what\'s your name', 'how are you','what','how do you feel','i am fine','i am sorry','i dont understand','i love you','i miss you','keep in touch','how old are you','nice to meet you','no thank you','please slow down','time is up','what do you think','what happened','where are you from','where do you live','who i he','who is she','you good']
    if t in s_t:
        video_name = t+'.mp4'
        video = imageio.get_reader(video_name)
        def stream(label):

            for image in video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image
        #nw = Tk()
        root3=Toplevel()
        root3.geometry('1000x1000')
        my_label = Label(root3)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()
        root3.mainloop()
    else:
        
        
        global y
        #t=translator.translate(text, dest=tar).text
        Label(root,text=t,font="arial 20").place(x=100,y=y)
        y=y+35
        root1=Toplevel()
        root1.geometry('1500x1500')
        root1.title("American Sign Aplhabets")
        #input="Muhammad shahbaz khan "

        l=t.split()
        q=0
        p=-1
        photo=[w for w in range(len(t))]
        j=0
        k=0
        for i in l:
            p=p+1
            q=0
        
            for j in i:
                if j=='\'' or j=='?' or j==':' or j==',' or j=='.':
                    Label(root1,text=j).grid(row=p,column=q)
                    q=q+1
        
                elif j!=' ':
                
                    photo[k]=PhotoImage(file=j+'.gif')
                    photo[k]=photo[k].subsample(2)

                    labelphoto=Label(root1,image=photo[k]).grid(row=p,column=q)
                    q=q+1
                    k=k+1
                else:
                    pass
        root1.mainloop()    

        #print(translator.translate(text, dest=tar).text)
def convert_to_British():
    text=get_text()
    destination_languages = {
       
        'English':'en'
    }
   
    
    tar=destination_languages["English"]
    translator = Translator()
   
    
    global t
    global y
    t=translator.translate(text, dest=tar).text
    Label(root,text=t,font="arial 20").place(x=100,y=y)
    y=y+30
    root1=Toplevel()
    root1.geometry('1500x1500')
    root1.title("British Sign Alphabets")
    l=t.split()
    q=0
    p=-1
    photo=[x for x in range(len(t))]
    j=0
    k=0
    for i in l:
        p=p+1
        q=0
        for j in i:
            if j=='\'' or j=='?' or j==':' or j==',' or j=='.':
                Label(root1,text=j).grid(row=p,column=q)
                q=q+1
    
            elif j!=' ':
                
                photo[k]=PhotoImage(file='bsl'+j+'.gif')
            #photo[k]=photo[k].zoom(10)
                photo[k]=photo[k].subsample(3)
                labelphoto=Label(root1,image=photo[k]).grid(row=p,column=q)
                q=q+1
                k=k+1
    root.mainloop()
    

btn=Button(root,text="convert to American sign Language",command=convert_to_American).place(x=450,y=400)
btn=Button(root,text="convert to British sign Language",command=convert_to_British).place(x=690,y=400)

root.mainloop()
