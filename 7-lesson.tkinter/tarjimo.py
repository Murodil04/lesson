# googletrans paketini yuklab olish pip insall googletrans==3.1.0a0
# Bepul va cheksiz xizmat
# API dan foydalanish
# Avtomatik tilni aniqlash
# 106 ta til mavjud
# https://cloud.google.com/translate/docs/languages
# pip insall pyinstaller
# pyinstaller tarjimon.py-onefile
# py2applet-makesetup MYAPP.py(change.myapp to yourname file.py)
# python3 setup.py py2app-A


from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
from tkmacosx import Button

root=Tk()
root.title('Google tarjimon dasturi...')
root.geometry('590x370')

#1
frame1=Frame(root,width=590,height=370,relief=RIDGE,borderwidth=5,bg='#4287f5')
frame1.place(x=0,y=0)

#3
def tarjimon():
    lang1=src_lang.get('1.0','end-1c')
    cl=choose_language.get()
    if lang1=="":
        messagebox.showerror('Tarjimon dasturi','Iltimos text kiriting:')
    else:
        trans_lang.delete(1.0,'end')
        translator=Translator()
        try:
            output=translator.translate(lang1,dest=cl)
            trans_lang.insert('end',output.text)
        except:
            messagebox.showerror('Tarjimon dasturi','Tanlangan tilda xatolik bor')

def clear():
    src_lang.delete(1.0,'end')
    trans_lang.delete(1.0,'end')

#4
a=StringVar
auto_select=ttk.Combobox(frame1,width=27,textvariable=a,state='randomly',font=('Verdana',10,'bold'))
auto_select['values']=('Auto Select',)
auto_select.place(x=15,y=60)
auto_select.current(0)

#5
I=StringVar()
choose_language=ttk.Combobox(frame1,width=27,textvariable=I,state='randomly',font=("Verdana",10,'bold'))
choose_language['values']=(
    'uz'
)
choose_language.current(0)
choose_language.place(x=350,y=60)

#2
Label(root,text='Tarjimon dasturi',font=("Verdana 20 bold"),fg='black',bg='#4287f5').pack(pady=10)

src_lang=Text(frame1,width=25,height=8,borderwidth=2,relief=RIDGE,font=('Arial 16'),bg='white',fg='black')
src_lang.place(x=10,y=100)

trans_lang=Text(frame1,width=25,height=8,borderwidth=2,relief=RIDGE,font=('Arial 16'),bg='white',fg='black')
trans_lang.place(x=300,y=100)

translateBtn=Button(frame1,command=tarjimon,text='Tarjima',relief=RAISED,borderwidth=2,font=('Verdana',15,'bold'),bg='white',fg='green',borderless=1,cursor='hand2')
translateBtn.place(x=185,y=300)

clearBtn=Button(frame1,command=clear,text='Tozalash',relief=RAISED,borderwidth=2,font=("Verdana",15,'bold'),bg='white',fg='green',borderless=1,cursor='hand2')
clearBtn.place(x=300,y=300)
root.mainloop()