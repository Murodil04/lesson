# GUI Graphic User Interface
# tkinter
from tkinter import*
# root=Tk()
# root.mainloop()

#
# root.title('Tkinterda dastur tuzish')
# root.geometry(600*400+500+150)
# root.resizable(False,False)
# # root.maxsize()
# root.mainloop

root=Tk()
def changeLabel():
    lb['text']=input_val.get()


lb=Label(root,text='Tarjimon dasturi',font='Verdana 20 bold',
fg='white',bg='indigo',padx=40,pady=50)
lb2=Label(root,text='Tarjomon dasturi2')
lb.pack()

input_val=Entry(root,font='Verdana 20 bold')
input_val.place(x=150,y=200)

btn=Button(root,text='Click me',fg='white',font='Verdena 20 bold',bg='black',command=changeLabel)
btn.place(x=180,y=150)
root.mainloop()
